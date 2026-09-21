from __future__ import annotations

import argparse
from pathlib import Path

from statement_synth.generate import write_pdf


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="statement-synth",
        description="Generate synthetic bank-statement PDFs for offline OCR testing.",
    )
    parser.add_argument("--pages", type=int, default=1)
    parser.add_argument("--rows", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=Path, default=Path("statement.pdf"))
    parser.add_argument("--bank-name", default="Example National Bank")
    parser.add_argument(
        "--layout",
        choices=("standard", "dense"),
        default="standard",
        help="PDF layout preset (default: standard)",
    )
    args = parser.parse_args(argv)

    if args.pages < 1 or args.rows < 1:
        parser.error("--pages and --rows must be >= 1")

    out = write_pdf(
        args.out,
        pages=args.pages,
        rows=args.rows,
        seed=args.seed,
        bank_name=args.bank_name,
        layout=args.layout,
    )
    print(f"Wrote {out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
