import argparse
import re
import sys
import os


def start_parsing():
    parser = argparse.ArgumentParser(description='Show list of files and dirs in the path/directory')
    parser.add_argument('-a', '--all', help='show hidden files', action='store_true')
    parser.add_argument('path', nargs='?', default='.')
    return parser.parse_args()


if __name__ == "__main__":
    args = start_parsing()
    if args.all:
        content = os.listdir(args.path)
    else:
        content = [file for file in os.listdir(args.path) if not file.startswith('.')]
    for i in content:
        sys.stdout.write(i)
        sys.stdout.write('\n')
