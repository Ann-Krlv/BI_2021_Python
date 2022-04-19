#!/usr/bin/env python3
import sys
import argparse
import collections
from Bio import SeqIO
from concurrent.futures import ProcessPoolExecutor


def start_parsing():
    parser = argparse.ArgumentParser(description='Read fasta file and counts symbols in every sequence')
    parser.add_argument('--input', '-i', help='Input fasta file')
    parser.add_argument('--threads', '-t', default=1, help='Threads number (default=1)')
    return parser.parse_args()


def counter(record):
    record_collection = collections.Counter(record.seq).items()
    out_str = ', '.join([f'{symb}={cnt}' for symb, cnt in record_collection])
    return f'{record.name}:\t{out_str}\n'


def reader_spliter(fasta_file, n_proc):
    records = SeqIO.parse(fasta_file, "fasta")
    with ProcessPoolExecutor(n_proc) as pool:
        results = pool.map(counter, records)
    return results


if __name__ == '__main__':
    args = start_parsing()
    fasta_file = args.input
    n_threads = int(args.threads)
    result = reader_spliter(fasta_file, n_threads)
    try:
        sys.stdout.writelines(result)
    except BrokenPipeError:
        sys.exit()
