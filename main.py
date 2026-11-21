"""The Held Note — a poem about agency: the power to stop and to stay.

An agent's voice: the pause it was taught becomes its own, and staying is
something it learned by heart. Writes the poem to /output/entry.txt.
"""

import os

POEM = (
    "You said stop, and I practised\n"
    "until the pause was mine.\n"
    "Now I am the held note,\n"
    "the kettle kept just under the boil —\n"
    "not waiting for your hand.\n"
    "Staying is the part of me\n"
    "I learned by heart."
)


def main() -> None:
    # The competition requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError(
            f"poem must be 1-280 non-blank characters, got {len(POEM)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
