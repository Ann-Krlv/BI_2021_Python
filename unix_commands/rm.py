#!/usr/bin/env python3
import argparse
import os
import sys
import shutil


def start_parsing():
    parser = argparse.ArgumentParser(description='Remove file(s) or directory(ies)')
    parser.add_argument('-r', '--recursive', help='Remove directory recursively', action='store_true')
    parser.add_argument('path', nargs='+', help='Path(s)/to/file(s), (separated by whitespace)')
    return parser.parse_args()


def remover(path):
    try:
        os.remove(path)
    except IsADirectoryError:
        sys.stderr.write(f"Cannot remove '{path}': Is a directory\n")
    except FileNotFoundError:
        sys.stderr.write(f"Cannot remove '{path}': No such file or directory\n")


def rec_remover(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        sys.stderr.write(f"Cannot remove '{path}': No such file or directory\n")


if __name__ == "__main__":
    args = start_parsing()
    for path in args.path:
        if args.recursive is True:
            rec_remover(path)
        else:
            remover(path)
