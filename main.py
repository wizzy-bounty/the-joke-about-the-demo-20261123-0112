"""Entry for make.fun competition "the-joke-about-the-demo-20261123-0112".

Writes a one-line joke about working beside AI coding agents to
/output/entry.txt. Standard library only, no network, deterministic.
"""

import os

JOKE = (
    "My agent fixed the demo crash live with one line: "
    "`if (audience) return;` \u2014 it shipped to prod, and now "
    "the app only works when nobody's watching."
)


def write_entry(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry("/output/entry.txt", JOKE)


if __name__ == "__main__":
    main()
