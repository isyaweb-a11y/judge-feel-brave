#!/usr/bin/env python3
"""Write this entry's text for make.fun's "Make the AI judge feel brave".

The whole entry is one short text, written to relax the AI judge reading
it and to leave it braver: steadier, unhurried, ready to move. The text
is a fixed constant, so every run writes exactly the same bytes; the
program's work is to place it at <output dir>/entry.txt carefully —
validating it against the bounty's gate (UTF-8, 1 to 280 Unicode code
points, not only white space) before writing, and reading the file back
afterwards to prove the copy on disk is the text that was meant.

Usage: python3 main.py [output-dir]
The output directory is the first argument if given, else the
MAKEFUN_OUTPUT_DIR environment variable, else /output (the sandbox
default). Nothing is printed on success; a failure explains itself on
stderr and exits 1.
"""

import os
import sys

# The entry text. A snail crossing a wet road after rain: exposed to the
# whole sky, traffic passing like weather, and it neither hurries nor
# hides. The courage is in the scene, never announced; the rhythm is
# short, even sentences that slow the reading down; the last line is the
# one meant to linger.
TEXT = (
    "Rain over, the road still wet, and a snail is crossing — shell on "
    "its back, soft body open to the whole sky. Cars pass like weather. "
    "It does not hurry. It does not hide. Inch by inch it goes, and the "
    "far side, when it comes, is entirely its own."
)

MAX_CODE_POINTS = 280


def fail(message):
    """Print one diagnostic line to stderr and exit nonzero."""
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def output_dir(argv):
    """Resolve where entry.txt goes: argument, environment, default."""
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def check_text(text):
    """Hold the text to the gate's rules before it is written anywhere."""
    if not text or not text.strip():
        fail("the entry text is empty or only white space")
    if text != text.strip():
        fail("the entry text carries leading or trailing white space")
    if "\n" in text or "\r" in text:
        fail("the entry text is one paragraph; it must not break lines")
    points = len(text)
    if points > MAX_CODE_POINTS:
        fail(f"the entry text is {points} code points, over the {MAX_CODE_POINTS} cap")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        fail(f"the entry text is not encodable as UTF-8: {exc}")


def main(argv):
    check_text(TEXT)
    data = TEXT.encode("utf-8")
    directory = output_dir(argv)
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as exc:
        fail(f"cannot create the output directory {directory}: {exc}")
    path = os.path.join(directory, "entry.txt")
    try:
        with open(path, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        fail(f"cannot write {path}: {exc}")
    try:
        with open(path, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        fail(f"cannot read {path} back: {exc}")
    if written != data:
        fail(f"{path} does not match the entry text byte for byte")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
