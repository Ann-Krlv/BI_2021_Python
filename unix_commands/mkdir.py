#!/usr/bin/env python3
import argparse
import sys
import os


def start_parsing():
    parser = argparse.ArgumentParser(description='Creates directory (directories)')
    parser.add_argument('-p', '--parents', action='store_true', help='Creates parents directories if they not exist')
    parser.add_argument('path', nargs='+', help='Path(s)/to/file(s) to create (separated by whitespace)')
    return parser.parse_args()


def create_with_parents(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        sys.stderr.write(f"Cannot create directory '{path}': File exists\n")


def simple_creation(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        sys.stderr.write(f"Cannot create directory '{path}': File exists\n")
    except FileNotFoundError:
        sys.stderr.write(f"Cannot create directory '{path}': No such file or directory\n")


if __name__ == "__main__":
    args = start_parsing()
    if args.parents is True:
        for path in args.path:
            create_with_parents(path)
    else:
        for path in args.path:
            simple_creation(path)
