#!/usr/bin/env python3
"""Write one funny out-of-office line to /output/entry.txt. Stdlib only."""
import os

LINE = "I am out of office, and so is my inbox. It left a note saying it will reply when I do — which is never, or Monday, whichever comes second."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
