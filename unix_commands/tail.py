#!/usr/bin/env python3
import argparse
import sys


def start_parsing():
    parser = argparse.ArgumentParser(description='Shows n lines from the end of text')
    parser.add_argument('-n', '--number', type=int, default=10, help="The number of lines shown (10 default)")
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help="Path to files (separated by whitespace). If no files given, then use stdin (default)")
    return parser.parse_args()


if __name__ == "__main__":
    args = start_parsing()
    n = args.number
    res = [''] * n
    for file in args.infile:
        text = file.readlines()
        for i in range(-1, -n - 1, -1):
            res[i] = text[i]
        if len(args.infile) > 1:
            sys.stdout.write(f'==> {file.name} <==\n')
        sys.stdout.writelines(res)
