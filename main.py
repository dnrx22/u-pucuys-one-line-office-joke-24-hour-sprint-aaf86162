#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single original one-line joke about office life to entry.txt
inside the directory given by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only, deterministic, no network access.
"""

import hashlib
import os
import sys

JOKE = "Our meeting could have been an email, so we scheduled a follow-up meeting to discuss why the email never arrived."


def validate_joke(joke: str) -> None:
    """Validate the joke meets the competition constraints."""
    if not joke:
        raise ValueError("joke must not be empty")
    if joke != joke.strip():
        raise ValueError("joke must not have leading or trailing whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be exactly one line")
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(joke)}")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in joke):
        raise ValueError("joke must not contain control characters")
    joke.encode("utf-8")


def main() -> int:
    validate_joke(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    with open(output_path, "wb") as f:
        f.write(data)
    with open(output_path, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("written entry.txt does not match the validated joke")
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {output_path} ({len(JOKE)} chars)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
