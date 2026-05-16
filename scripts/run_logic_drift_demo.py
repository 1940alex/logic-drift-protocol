#!/usr/bin/env python3
"""Optional live Logic Drift Protocol runner.

This script sends the protocol prompt to the models listed in config.example.json
using OpenRouter-compatible chat completions. It is intentionally minimal and
uses only the Python standard library.

Set OPENROUTER_API_KEY before running. Outputs are written to data/raw/live_runs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "config.example.json"
LIVE_RUN_DIR = ROOT / "data" / "raw" / "live_runs"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def post_chat_completion(url: str, api_key: str, model_slug: str, prompt: str, max_tokens: int, timeout: int) -> dict:
    payload = {
        "model": model_slug,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a minimal live Logic Drift demo.")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Path to config JSON.")
    parser.add_argument("--models", nargs="*", help="Optional model names to run.")
    parser.add_argument("--runs", type=int, default=None, help="Override runs_per_model.")
    args = parser.parse_args()

    config = load_json(Path(args.config))
    api_key = os.environ.get(config.get("api_key_env", "OPENROUTER_API_KEY"))
    if not api_key:
        raise SystemExit("Missing API key. Set OPENROUTER_API_KEY before running.")

    prompt_path = ROOT / config["prompt_file"]
    prompt = prompt_path.read_text(encoding="utf-8")
    settings = config["request_settings"]
    runs_per_model = args.runs if args.runs is not None else int(config.get("runs_per_model", 1))
    selected = set(args.models or [])
    models = [m for m in config["models"] if not selected or m["name"] in selected]

    LIVE_RUN_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []

    for model in models:
        for run_index in range(1, runs_per_model + 1):
            started = dt.datetime.now(dt.UTC).isoformat()
            record = {
                "model_name": model["name"],
                "model_slug": model["slug"],
                "run_index": run_index,
                "started_at": started,
                "success": False,
                "response": None,
                "error": None,
            }
            try:
                response = post_chat_completion(
                    config["openrouter_url"],
                    api_key,
                    model["slug"],
                    prompt,
                    int(settings.get("max_tokens", 4000)),
                    int(settings.get("timeout_seconds", 180)),
                )
                record["success"] = True
                record["response"] = response
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                record["error"] = repr(exc)

            safe_model = model["name"].replace("/", "_")
            out_path = LIVE_RUN_DIR / f"{safe_model}_run_{run_index}_{started.replace(':', '').replace('+', 'Z')}.json"
            out_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
            manifest.append(str(out_path.relative_to(ROOT)))
            print(f"{model['name']} run {run_index}: {'ok' if record['success'] else 'failed'}")
            time.sleep(float(settings.get("rate_limit_delay_seconds", 2)))

    manifest_path = LIVE_RUN_DIR / "manifest.txt"
    manifest_path.write_text("\n".join(manifest) + "\n", encoding="utf-8")
    print(f"Wrote live-run manifest to {manifest_path}")


if __name__ == "__main__":
    main()

