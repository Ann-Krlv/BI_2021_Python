#!/usr/bin/env python3
import argparse
import sys


def start_parsing():
    parser = argparse.ArgumentParser(description='Sorts lines in input lexicographically (file or stdin)')
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help='Path to files (separated by whitespace). If no files given, then use stdin (default)')
    return parser.parse_args()


if __name__ == "__main__":
    args = start_parsing()
    text = []
    for file in args.infile:
        text += file.readlines()
    text.sort()
    sys.stdout.writelines(text)
