#!/usr/bin/env python3
import argparse
import sys
import re


def start_parsing():
    parser = argparse.ArgumentParser(description='Find text sample or regexp in input (file(s) or stdin)')
    parser.add_argument('regexp', type=str, help='Text to find (can work with python3 regular expressions)')
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help="Path to files (separated by whitespace). If no files given, then use stdin (default)")
    return parser.parse_args()


if __name__ == "__main__":
    args = start_parsing()
    pattern = re.compile(fr'(^.*{args.regexp}.*)\n', re.MULTILINE)
    for text in args.infile:
        results = pattern.findall(text.read())
        if len(args.infile) > 1:
            sys.stdout.write(f'==> {text.name} <==\n')
        sys.stdout.write('\n'.join(results))
        sys.stdout.write('\n')
