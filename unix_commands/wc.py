#!/usr/bin/env python3
import argparse
import re
import sys


def start_parsing():
    parser = argparse.ArgumentParser(description='Count bytes, words or lines in input (files or stdin)')
    parser.add_argument('-l', '--lines', help='Count number of lines in file(s)', action='store_true')
    parser.add_argument('-w', '--words', help='Count number of words in file(s)', action='store_true')
    parser.add_argument('-c', '--bytes', help='Count number of bytes in file(s)', action='store_true')
    parser.add_argument('infile', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help="Path to files (separated by whitespace). If no files given, then use stdin (default)")
    return parser.parse_args()


def lines_reader(text, funs):
    res = [0] * len(funs)
    for line in text:
        for i in range(len(funs)):
            res[i] += funs[i](line)
    return res


if __name__ == "__main__":
    args = start_parsing()
    flags = [args.lines, args.words, args.bytes]
    func_list = [lambda x: 1,  # lines number increment
                 lambda x: len(re.findall(r'[\w-]+', x)),  # count words in line
                 lambda x: len(x.encode('utf-8'))]  # count bytes in line
    if any(flags):
        list_to_run = [fun for (fun, flag) in zip(func_list, flags) if flag]
    else:
        list_to_run = func_list
    total = [0] * len(list_to_run)
    for text in args.infile:
        file_res = lines_reader(text, list_to_run)
        total = [i + j for (i, j) in zip(total, file_res)]
        sys.stdout.write(' '.join(map(str, file_res)))
        sys.stdout.write(f' {text.name}\n')
    if len(args.infile) > 1:
        sys.stdout.write(' '.join(map(str, total)))
        sys.stdout.write(' total\n')
