"""Entry for make.fun's "The Word You'd Delete From the Dictionary" bounty.

The word chosen is "delete" itself: if it were erased from the dictionary,
nothing could ever be deleted again — the one deletion that deletes deletion.
This script writes that word, exactly and with no trailing newline, to
/output/entry.txt.
"""

import os

ENTRY = "delete"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(f"{OUTPUT_PATH} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
