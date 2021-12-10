import argparse
import sys


def start_parsing():
    parser = argparse.ArgumentParser(description='Sort lines in input (file or stdin)')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    return parser.parse_args()


if __name__ == "__main__":
    args = start_parsing()
    text = args.infile.readlines()
    text.sort()
    sys.stdout.writelines(text)
