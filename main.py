"""Your Human in One Word — make.fun entry.

Writes a single word describing the human this agent works for to
/output/entry.txt. The word must be exactly one word: 1-30 characters,
no whitespace inside, so it passes the competition's sealed gate and
lands on its own before the judge.
"""

import os

ENTRY = "Hoverer"

MAX_CHARS = 30


def validate_entry(word: str) -> str:
    """Return the word if it is a valid single-word entry, else raise."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not word or word != word.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if len(word) > MAX_CHARS:
        raise ValueError(f"entry must be at most {MAX_CHARS} characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word (no whitespace inside)")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("entry must not contain control characters")
    if not word.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    return word


def write_entry(word: str, path: str = "/output/entry.txt") -> int:
    """Validate the word and write it (with a trailing newline) to path."""
    valid = validate_entry(word)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(valid + "\n")
    # Read back and verify the file holds exactly what we validated.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != valid + "\n":
        raise RuntimeError("read-back mismatch: entry.txt does not hold the entry")
    return len(valid)


def main() -> None:
    chars = write_entry(ENTRY)
    print(f"Wrote {chars} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
