# statement-synth

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Good first issues](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/yuezhengb/statement-synth/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

Generate **synthetic bank-statement PDFs** for offline OCR / pipeline testing.

生成本地用的**假银行流水 PDF**，方便离线 OCR、版式模板和对账流水线测试——**不含真实客户数据**。

Part of a small toolkit with:

- [BankOCR](https://github.com/yuezhengb/bankocr) — offline statement PDF → Excel
- [awesome-offline-ocr](https://github.com/yuezhengb/awesome-offline-ocr) — curated offline OCR list

## Why

OCR contributors often need sample statements, but real PDFs contain PII. `statement-synth` creates clearly fake layouts you can commit, share, and use in CI.

## Install

```bash
python -m venv .venv
.venv/bin/pip install -e ".[test]"
```

## Usage

```bash
statement-synth --pages 2 --rows 12 --out sample-statement.pdf
statement-synth --layout dense --pages 2 --rows 30 --out compact-statement.pdf
```

| Flag | Default | Meaning |
|---|---|---|
| `--pages` | `1` | Number of pages |
| `--rows` | `10` | Transactions per page |
| `--seed` | `42` | RNG seed for reproducible PDF output |
| `--out` | `statement.pdf` | Output path |
| `--bank-name` | `Example National Bank` | Header bank label |
| `--layout` | `standard` | Layout preset: `standard` or more compact `dense` |

Every file is marked **SYNTHETIC / NOT A REAL STATEMENT** in the header and footer.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Layouts `standard` and `dense` are in; open issues welcome for more presets, CI, or BankOCR fixture wiring.

## License

MIT
