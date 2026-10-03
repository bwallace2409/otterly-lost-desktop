"""Otterly Lost Desktop — A local helper for Otterly Lost river folders, otter-home saves, and cute photo albums."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='otterly_lost_desktop',
        description='A local helper for Otterly Lost river folders, otter-home saves, and cute photo albums.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Otterly Lost Desktop')
    print('Keep the river home on disk before a story beat.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
