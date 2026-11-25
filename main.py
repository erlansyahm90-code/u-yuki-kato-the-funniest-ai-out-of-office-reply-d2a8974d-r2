"""Write the funniest AI out-of-office reply entry to /output/entry.txt."""

import os

ENTRY_TEXT = "I'm away until Monday. My AI answered 312 emails while I was gone, approved its own vacation, and left a note saying 'you're welcome.' It's still on vacation."
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    write_entry()
