def transcribe(seq, i):
    if 'U' in seq or 'u' in seq:
        print('It is uracil in the sequence. Invalid alphabet, try again!')
        i = 1
        return seq, i
    seq = seq.replace('T', 'U')
    seq = seq.replace('t', 'u')
    i = 0
    return seq, i


def complement(seq, i):
    if 'U' in seq or 'u' in seq:
        i = 0
        seq_1 = ''.join([nucl_dict_RNA[n] for n in seq])
    else:
        i = 0
        seq_1 = ''.join([nucl_dict_DNA[n] for n in seq])
    return seq_1, i


def reverse(seq, i):
    i = 0
    return seq[::-1], i


def reverse_complement(seq, i):
    if 'U' in seq or 'u' in seq:
        i = 0
        seq_1 = ''.join([nucl_dict_RNA[n] for n in seq])
    else:
        i = 0
        seq_1 = ''.join([nucl_dict_DNA[n] for n in seq])
    return seq_1[::-1], i


def seq_check(seq, i):
    i = 0
    for n in seq:
        if n not in ('AaGgCcTtUu'):
            i = 1
            print("Invalid alphabet, try again.")
            break
    if ('T' in seq or 't' in seq) and ('U' in seq or 'u' in seq):
        print("There are U and T in the sequence, try again.")
        i = 1
    return i


func_dict = {"transcribe": transcribe,
             "complement": complement,
             "reverse": reverse,
             "reverse complement": reverse_complement}

nucl_dict_DNA = {'A': 'T', 'a': 't', 'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g', 'T': 'A', 't': 'a'}
nucl_dict_RNA = {'A': 'U', 'a': 'u', 'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g', 'U': 'A', 'u': 'a'}


if __name__ == '__main__':
    while True:
        com = input("Enter command: ")
        if com == "exit":
            print("Goodbye")
            break
        i = 1  # i = 1 means error in sequence, i = 0 -- ok
        if com in func_dict:
            while i:
                seq = input("Enter sequence: ")
                if seq_check(seq, i):
                    continue
                seq, i = func_dict[com](seq, i)
            print(seq)
        else:
            print("Unknown command. Try again or print 'exit'.")
