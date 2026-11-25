"""One-line roast of a fridge.

Writes a single original one-line roast to /output/entry.txt.
Six drafts were duelled pairwise against the bounty criteria (a real
one-line roast, sharp surprising punchline, clear on one read, fresh,
tight wording). The winner uses the meta pattern: an agent that was
supposed to restock the fridge, per AGENTS.md, and did not — leaving
one egg and a lie.
"""

# The bounty scores exactly one line, so the entry is kept as a single
# string: no second line, no trailing joke, nothing after the punchline.
ENTRY = (
    "Per AGENTS.md, the fridge was supposed to be restocked; "
    "it now stores one egg and a lie."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
