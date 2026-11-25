import os

ENTRY = "My smart fridge updated its firmware at 3 a.m. and now it refuses to open until I accept the new terms and conditions."


def main():
    text = ENTRY.strip()
    # Self-gate mirroring the sealed scorer: UTF-8 text, 1-200 chars,
    # single line, not only whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
