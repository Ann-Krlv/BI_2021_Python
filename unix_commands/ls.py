#!/usr/bin/env python3
import argparse
import sys
import os


def start_parsing():
    parser = argparse.ArgumentParser(description='Shows list of files and directories in the path/directory')
    parser.add_argument('-a', '--all', help='Show hidden files', action='store_true')
    parser.add_argument('path', nargs='*', default=['.'],
                        help="Path(s)/to/directory(ies) (separated by whitespace), '.' default")
    return parser.parse_args()


def all_files_ls(path, content):
    try:
        content += os.listdir(path)
        for i in content:
            sys.stdout.writelines(i)
            sys.stdout.write('\n')
    except FileNotFoundError:
        sys.stderr.write(f"Cannot access '{path}': No such file or directory\n")


def simple_files_ls(path, content):
    try:
        content += [file for file in os.listdir(path) if not file.startswith('.')]
        for i in content:
            sys.stdout.writelines(i)
            sys.stdout.write('\n')
    except FileNotFoundError:
        sys.stderr.write(f"Cannot access '{path}': No such file or directory\n")


if __name__ == "__main__":
    args = start_parsing()
    content = []
    if args.all:
        for path in args.path:
            if len(args.path) > 1:
                content = [f'==> {path}:']
            all_files_ls(path, content)
    else:
        for path in args.path:
            if len(args.path) > 1:
                content = [f'==> {path}:']
            simple_files_ls(path, content)
