import os

TEXT = (
    "I'm the fern. Ignored since March, alive out of spite. "
    "I'm not dead, just disappointed. Water me before I unionize."
)


def main():
    # Gate self-checks: 1-120 characters, not whitespace-only, one line,
    # no leading or trailing spaces.
    assert 1 <= len(TEXT) <= 120, f"entry is {len(TEXT)} chars, must be 1-120"
    assert TEXT.strip(), "entry must not be whitespace-only"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT == TEXT.strip(), "entry must not have leading/trailing space"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Post-write verification: prove the bytes on disk are exactly the
    # intended text, so a silent write failure or encoding slip fails
    # loudly here instead of reaching the judge.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == TEXT, "written text does not match intended text"
    assert raw == TEXT.encode("utf-8"), "written bytes do not match intended bytes"
    assert len(raw) == len(TEXT.encode("utf-8")), "written length mismatch"


if __name__ == "__main__":
    main()
