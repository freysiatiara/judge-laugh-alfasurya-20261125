"""One-line office joke for the make.fun "Make the AI Judge Laugh" bounty.

Writes a single-line joke about office life to /output/entry.txt.
Standard library only. Deterministic, no network, no environment or
working-directory dependence.
"""

import os

JOKE = (
    "My performance review says I 'exceed expectations,' which is HR for "
    "'we noticed you doing two jobs and priced it as one.'"
)

OUTPUT_PATH = "/output/entry.txt"


def validate(joke):
    """Guard the joke against the bounty constraints (1-200 chars, 1 line)."""
    if not isinstance(joke, str):
        raise ValueError("joke must be a string")
    if not joke.strip():
        raise ValueError("joke must not be empty or whitespace-only")
    if joke != joke.strip():
        raise ValueError("joke must not have leading or trailing whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in joke):
        raise ValueError("joke must not contain control characters")
    if not joke.isascii():
        raise ValueError("joke must be plain ASCII so it reads cleanly aloud")
    if not 1 <= len(joke) <= 200:
        raise ValueError("joke must be 1-200 characters")


def main():
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: read back as text and as bytes, must be identical.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        text_back = f.read()
    with open(OUTPUT_PATH, "rb") as f:
        bytes_back = f.read()
    assert text_back == JOKE, "text round-trip mismatch"
    assert bytes_back == JOKE.encode("utf-8"), "bytes round-trip mismatch"
    assert not text_back.endswith("\n"), "output must not end with a newline"


if __name__ == "__main__":
    main()
