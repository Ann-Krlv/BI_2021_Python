#!/usr/bin/env python3
import argparse
import os
import sys
import shutil


def start_parsing():
    parser = argparse.ArgumentParser(description='Show list of files and dirs in the path/directory')
    parser.add_argument('-r', '--recursive', help='remove recursively', action='store_true')
    parser.add_argument('path', help='path/to/file')
    return parser.parse_args()


if __name__ == "__main__":
    args = start_parsing()
    if args.recursive is True:
        shutil.rmtree(args.path)
    else:
        try:
            os.remove(args.path)
        except IsADirectoryError:
            sys.stderr.write(f"Cannot remove '{args.path}': Is a directory\n")
            exit(1)
        except FileNotFoundError:
            sys.stderr.write(f"Cannot remove '{args.path}': No such file or directory\n")
            exit(1)
