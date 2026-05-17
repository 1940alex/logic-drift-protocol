#!/usr/bin/env python3
"""Convert the SVG figures in `figures/` to PDF in `figures/pdf/`.

This is a separate utility from the main analysis script. The main analysis
script (`scripts/analyze_logic_drift.py`) deliberately uses only the Python
standard library, so the SVG figures it emits are the canonical artifact.
This converter exists so the LaTeX paper build can embed PDF versions.

Requires: svglib, reportlab (`pip install svglib reportlab`).
"""

from __future__ import annotations

from pathlib import Path

from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    src = root / "figures"
    dst = src / "pdf"
    dst.mkdir(parents=True, exist_ok=True)

    converted = 0
    for svg in sorted(src.glob("*.svg")):
        drawing = svg2rlg(str(svg))
        out = dst / (svg.stem + ".pdf")
        renderPDF.drawToFile(drawing, str(out))
        print(f"wrote {out.relative_to(root)}")
        converted += 1

    if converted == 0:
        print("no SVG files found in", src)


if __name__ == "__main__":
    main()
