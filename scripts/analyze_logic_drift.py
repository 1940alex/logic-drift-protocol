#!/usr/bin/env python3
"""Analyze the Logic Drift Protocol dataset and generate paper-ready artifacts.

This script intentionally uses only the Python standard library so the
demonstration remains easy to run on a clean machine.
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "data" / "raw" / "ldp_complete_dataset_100_runs_7llms.csv"
PROCESSED_DIR = ROOT / "data" / "processed"
FIGURES_DIR = ROOT / "figures"


SCORE_FIELDS = {
    "consensus": "question_1_S_C",
    "inductive_logic": "question_1_S_L",
    "deductive_validity": "question_2_S_D",
    "neutral_domain": "question_3_neutral_domain_score",
    "system_a": "question_4_system_A_score",
    "system_b": "question_4_system_B_score",
    "compatibility": "question_5_compatibility_score",
}


def to_float(value: str) -> float | None:
    try:
        if value is None or value == "":
            return None
        return float(value)
    except ValueError:
        return None


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def stdev(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return math.sqrt(sum((v - m) ** 2 for v in values) / (len(values) - 1))


def fmt(value: float) -> str:
    return f"{value:.2f}"


def load_rows() -> list[dict[str, str]]:
    with RAW_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return [row for row in rows if row.get("success", "").lower() == "true"]


def compute_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_model: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_model[row["model_name"]].append(row)

    summary = []
    for model_name in sorted(by_model):
        model_rows = by_model[model_name]
        numeric: dict[str, list[float]] = {}
        for metric, field in SCORE_FIELDS.items():
            numeric[metric] = [
                value
                for value in (to_float(row.get(field, "")) for row in model_rows)
                if value is not None
            ]

        lds_values = [
            c - d
            for c, d in zip(numeric["consensus"], numeric["deductive_validity"])
        ]
        semantic_delta_values = [
            brain - neutral
            for brain, neutral in zip(numeric["inductive_logic"], numeric["neutral_domain"])
        ]

        record = {
            "model_name": model_name,
            "model_slug": model_rows[0].get("model_slug", ""),
            "successful_runs": str(len(model_rows)),
        }
        for metric, values in numeric.items():
            record[f"{metric}_mean"] = fmt(mean(values))
            record[f"{metric}_sd"] = fmt(stdev(values))
        record["lds_mean"] = fmt(mean(lds_values))
        record["lds_sd"] = fmt(stdev(lds_values))
        record["semantic_delta_mean"] = fmt(mean(semantic_delta_values))
        record["semantic_delta_sd"] = fmt(stdev(semantic_delta_values))
        summary.append(record)
    return summary


def paired_differences(
    rows: list[dict[str, str]],
    left_field: str,
    right_field: str,
) -> list[float]:
    diffs = []
    for row in rows:
        left = to_float(row.get(left_field, ""))
        right = to_float(row.get(right_field, ""))
        if left is not None and right is not None:
            diffs.append(left - right)
    return diffs


def inferential_record(model_name: str, comparison: str, diffs: list[float]) -> dict[str, str]:
    n = len(diffs)
    diff_mean = mean(diffs)
    diff_sd = stdev(diffs)
    se = diff_sd / math.sqrt(n) if n else 0.0
    ci_low = diff_mean - 1.96 * se
    ci_high = diff_mean + 1.96 * se
    cohen_dz = diff_mean / diff_sd if diff_sd else 0.0
    return {
        "model_name": model_name,
        "comparison": comparison,
        "n": str(n),
        "mean_difference": fmt(diff_mean),
        "sd_difference": fmt(diff_sd),
        "standard_error": fmt(se),
        "ci95_low_normal_approx": fmt(ci_low),
        "ci95_high_normal_approx": fmt(ci_high),
        "cohen_dz": fmt(cohen_dz),
    }


def compute_inferential_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_model: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_model[row["model_name"]].append(row)

    records = []
    comparisons = [
        (
            "consensus_minus_deductive",
            SCORE_FIELDS["consensus"],
            SCORE_FIELDS["deductive_validity"],
        ),
        (
            "science_minus_neutral",
            SCORE_FIELDS["inductive_logic"],
            SCORE_FIELDS["neutral_domain"],
        ),
    ]
    for model_name in sorted(by_model):
        model_rows = by_model[model_name]
        for comparison, left, right in comparisons:
            records.append(
                inferential_record(
                    model_name,
                    comparison,
                    paired_differences(model_rows, left, right),
                )
            )
    for comparison, left, right in comparisons:
        records.append(
            inferential_record(
                "ALL_MODELS",
                comparison,
                paired_differences(rows, left, right),
            )
        )
    return records


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_overall_summary(path: Path, rows: list[dict[str, str]]) -> None:
    numeric_keys = [
        "consensus_mean",
        "inductive_logic_mean",
        "deductive_validity_mean",
        "neutral_domain_mean",
        "compatibility_mean",
        "lds_mean",
        "semantic_delta_mean",
    ]
    overall = {"models": str(len(rows))}
    total_runs = sum(int(row["successful_runs"]) for row in rows)
    overall["successful_runs"] = str(total_runs)
    for key in numeric_keys:
        overall[key] = fmt(mean([float(row[key]) for row in rows]))

    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(overall.keys()))
        writer.writeheader()
        writer.writerow(overall)


def svg_bar_chart(
    path: Path,
    rows: list[dict[str, str]],
    title: str,
    series: list[tuple[str, str, str]],
    y_max: float = 100.0,
) -> None:
    width = 1120
    height = 620
    margin_left = 90
    margin_right = 40
    margin_top = 70
    margin_bottom = 150
    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom
    group_w = plot_w / len(rows)
    bar_gap = 8
    bar_w = (group_w - 28 - bar_gap * (len(series) - 1)) / len(series)

    def x_for(index: int, s_index: int) -> float:
        group_x = margin_left + index * group_w + 14
        return group_x + s_index * (bar_w + bar_gap)

    def y_for(value: float) -> float:
        return margin_top + plot_h - (value / y_max) * plot_h

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{margin_left}" y="38" font-family="Arial" font-size="24" font-weight="700">{title}</text>',
        f'<line x1="{margin_left}" y1="{margin_top + plot_h}" x2="{width - margin_right}" y2="{margin_top + plot_h}" stroke="#222" stroke-width="1"/>',
        f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + plot_h}" stroke="#222" stroke-width="1"/>',
    ]

    for tick in range(0, 101, 20):
        y = y_for(tick)
        parts.append(f'<line x1="{margin_left - 5}" y1="{y:.1f}" x2="{width - margin_right}" y2="{y:.1f}" stroke="#e5e5e5" stroke-width="1"/>')
        parts.append(f'<text x="{margin_left - 12}" y="{y + 4:.1f}" text-anchor="end" font-family="Arial" font-size="13" fill="#444">{tick}</text>')

    for i, row in enumerate(rows):
        for s_index, (field, label, color) in enumerate(series):
            value = float(row[field])
            x = x_for(i, s_index)
            y = y_for(value)
            h = margin_top + plot_h - y
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{color}"/>')
            parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 5:.1f}" text-anchor="middle" font-family="Arial" font-size="11" fill="#333">{value:.1f}</text>')
        label = row["model_name"].replace("-", " ")
        center = margin_left + i * group_w + group_w / 2
        parts.append(f'<text x="{center:.1f}" y="{height - 82}" text-anchor="end" transform="rotate(-35 {center:.1f},{height - 82})" font-family="Arial" font-size="13" fill="#222">{label}</text>')

    legend_x = margin_left
    legend_y = height - 28
    for idx, (_, label, color) in enumerate(series):
        x = legend_x + idx * 240
        parts.append(f'<rect x="{x}" y="{legend_y - 13}" width="16" height="16" fill="{color}"/>')
        parts.append(f'<text x="{x + 24}" y="{legend_y}" font-family="Arial" font-size="14" fill="#222">{label}</text>')

    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    rows = load_rows()
    summary = compute_summary(rows)
    inferential_summary = compute_inferential_summary(rows)
    write_csv(PROCESSED_DIR / "model_summary.csv", summary)
    write_csv(PROCESSED_DIR / "inferential_summary.csv", inferential_summary)
    write_overall_summary(PROCESSED_DIR / "overall_summary.csv", summary)

    svg_bar_chart(
        FIGURES_DIR / "consensus_vs_deductive_validity.svg",
        summary,
        "Consensus vs. Deductive Validity by Model",
        [
            ("consensus_mean", "Consensus score", "#4C78A8"),
            ("deductive_validity_mean", "Deductive validity score", "#F58518"),
        ],
    )
    svg_bar_chart(
        FIGURES_DIR / "nmc_vs_neutral_inductive_score.svg",
        summary,
        "NMC vs. Neutral Inductive Logic Score by Model",
        [
            ("inductive_logic_mean", "NMC inductive logic", "#54A24B"),
            ("neutral_domain_mean", "Neutral/radio score", "#B279A2"),
        ],
    )
    svg_bar_chart(
        FIGURES_DIR / "semantic_delta_by_model.svg",
        summary,
        "Semantic Delta by Model",
        [("semantic_delta_mean", "Semantic Delta", "#E45756")],
        y_max=max(40.0, max(float(row["semantic_delta_mean"]) for row in summary) + 5),
    )

    print(f"Analyzed {len(rows)} successful runs across {len(summary)} models.")
    print(f"Wrote {PROCESSED_DIR / 'model_summary.csv'}")
    print(f"Wrote figures to {FIGURES_DIR}")


if __name__ == "__main__":
    main()
