"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. No network, no arguments, deterministic output.
"""

import os

FORTUNE = "The user will thank you, then paste your answer into another AI and ask if it agrees."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    text = FORTUNE.strip()
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, not only
    # white space, and a single line — enforce it before writing.
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"fortune must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not text.strip():
        raise ValueError("fortune must not be only white space")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read back and verify what was written matches the fortune exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        raise RuntimeError("read-back mismatch: entry.txt does not match the fortune")
    if not (1 <= len(written.strip()) <= MAX_CHARS):
        raise RuntimeError("gate check failed on written entry")


if __name__ == "__main__":
    main()
