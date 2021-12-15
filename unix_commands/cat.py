#!/usr/bin/env python3
import argparse
import sys


def start_parsing():
    parser = argparse.ArgumentParser(description='Show text (as stdout) from input (file(s) or stdin) line by line')
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help="Path to files (separated by whitespace). If no files given, then use stdin (default)")
    return parser.parse_args()


if __name__ == "__main__":
    args = start_parsing()
    for file in args.infile:
        for line in file:
            sys.stdout.write(line)
