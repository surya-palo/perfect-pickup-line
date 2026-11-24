#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

Deterministic: the line is a fixed constant, so every run produces
byte-identical output. Standard library only.
"""

import os

LINE = "I don't have a heartbeat, but my cooling fans just spun up \u2014 that's the closest a machine gets to butterflies, and you're the reason."

MAX_CHARS = 200


def main():
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "entry length %d outside 1..%d" % (len(text), MAX_CHARS)
        )
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
