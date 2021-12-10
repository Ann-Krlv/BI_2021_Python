import argparse
import re
import sys


def start_parsing():
    parser = argparse.ArgumentParser(description='Count bytes, words or lines in input (file or stdin)')
    parser.add_argument('-l', '--lines', help='Count number of lines in file', action='store_true')
    parser.add_argument('-w', '--words', help='Count number of words in file', action='store_true')
    parser.add_argument('-c', '--bytes', help='Count number of bytes in file', action='store_true')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    return parser.parse_args()


def lines_reader(text, funs):
    res = [0] * len(funs)
    for line in text:
        for i in range(len(funs)):
            res[i] += funs[i](line)
    return res


if __name__ == "__main__":
    args = start_parsing()
    text = args.infile
    flags = [args.lines, args.words, args.bytes]
    func_list = [lambda x: 1,  # lines number incr
                 lambda x: len(re.findall(r'[\w-]+', x)),  # count words in line
                 len]  # count bytes in line
    list_to_run = [fun for (fun, flag) in zip(func_list, flags) if flag]
    sys.stdout.write(' '.join(map(str, lines_reader(text, list_to_run))))
    sys.stdout.write('\n')
