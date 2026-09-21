from pathlib import Path

from statement_synth.generate import build_transactions, write_pdf


def test_build_transactions_reproducible():
    a = build_transactions(1, 5, seed=7)
    b = build_transactions(1, 5, seed=7)
    assert [(t.day, t.description, t.debit, t.credit, t.balance) for t in a] == [
        (t.day, t.description, t.debit, t.credit, t.balance) for t in b
    ]


def test_write_pdf(tmp_path: Path):
    out = write_pdf(tmp_path / "x.pdf", pages=1, rows=3, seed=1)
    assert out.exists()
    assert out.stat().st_size > 500


def test_dense_layout_is_reproducible(tmp_path: Path):
    first = write_pdf(tmp_path / "first.pdf", rows=5, seed=7, layout="dense")
    second = write_pdf(tmp_path / "second.pdf", rows=5, seed=7, layout="dense")

    assert first.read_bytes() == second.read_bytes()
