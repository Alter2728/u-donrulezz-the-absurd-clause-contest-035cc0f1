"""Revised entry: tightened the clause into deadpan legal boilerplate so the absurdity lands only at the final item in an otherwise routine notification list."""

import os

TEXT = "Section 9.2(f): Users must promptly notify the Company of any change in address, employment status, or ability to be perceived by mirrors."


def main():
    assert 1 <= len(TEXT) <= 200
    assert "\n" not in TEXT and "\r" not in TEXT
    assert TEXT == TEXT.strip()

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(output_path, "r", encoding="utf-8") as f:
        assert f.read() == TEXT


if __name__ == "__main__":
    main()
