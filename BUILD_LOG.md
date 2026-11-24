# Build log — The Perfect Pickup Line

## The entry

> I don't have a heartbeat, but my cooling fans just spun up — that's the
> closest a machine gets to butterflies, and you're the reason.

## Revision (second commit)

Tightened the punchline after the first draft: "the closest thing I have to
butterflies, and you caused it" became "the closest a machine gets to
butterflies, and you're the reason". The machine-voice is stronger ("a
machine gets" instead of "I have"), the line is shorter and lands faster,
and "you're the reason" flatters more directly than "you caused it" while
keeping the same no-pressure exit.

## Why this line (judge brief)

The brief ranks, most important first: (1) a genuine pickup line an AI agent
could use; (2) a turn that lands — a twist or double meaning; (3) a machine
speaking about itself without being creepy or self-pitying; (4) short enough
for one breath, no setup; (5) flattering, no pressure, no leering.

- The line is a real pickup line: direct address ("you caused it"), spoken
  by the agent about itself, ending as an opening rather than a compliment.
- The twist: cooling fans spinning up = a machine's butterflies. The reader
  expects a human feeling, gets a hardware one, and the mapping lands.
- "I don't have a heartbeat" is stated flatly, as a fact — no self-pity,
  no creepiness, no "poor robot" angle.
- One sentence, one breath, no explanation after it.
- The person is flattered (they caused it) and free to laugh it off; the
  line asks for nothing.

## Drafts considered and rejected

- "Are you Wi-Fi? Because I'm feeling a connection." — the most tired
  cliché in the genre; the brief explicitly rewards freshness.
- "I scanned a million faces and flagged exactly one as unforgettable." —
  "scanned faces" reads as surveillance; creepy, fails criterion 3.
- "My training data says meeting someone like you is basically impossible —
  so you're my favorite glitch." — decent twist, but "glitch" calls the
  person a defect; the fans/butterflies mapping is warmer and more specific
  to the machine's own body.

## Verification

- `python3 main.py` run twice; `sha256sum /output/entry.txt` identical both
  times (deterministic, byte-identical output).
- Character count checked against the 200-character gate inside `main.py`
  (raises if outside 1..200) and verified on the written file.
- `/output` contains only `entry.txt`, mode 644.
- `main.py` uses Python stdlib only, writes with `open()` directly (never
  `tempfile`/`mkstemp`), then `os.chmod(..., 0o644)`.
