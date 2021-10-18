# check correct GC-percentage
def gc_filter(seq, percent_range):
    if type(percent_range) == int:
        percent_range = (0, int(percent_range))  # define percent_range as tulip with two integers
    gc_percent = (seq.count('G') + seq.count('C')) * 100/ len(seq)
    if percent_range[0] <= gc_percent <= percent_range[1]:
        return True
    else:
        return False


# check correct length of the read
def length_filter(seq, len_range):
    if type(len_range) == int:
        len_range = (0, int(len_range))
    if len_range[0] <= len(seq) <= len_range[1]:
        return True
    else:
        return False


# check average quality of the read (use phred33 scale)
def quality_filter(q_seq, quality):
    sum_quality = sum([ord(i)-33 for i in q_seq])
    if sum_quality/len(q_seq) >= quality:
        return True
    else:
        return False


# call check-functions and write the result of filtering (with failed reads)
def save_check_and_write(inf, pass_file, fail_file, gc_bounds, len_bounds, q_treshold):
    passed = []
    failed = []
    for i in range(1, len(inf), 4):
        if gc_filter(inf[i], gc_bounds) and length_filter(inf[i], len_bounds) and quality_filter(inf[i+2], q_treshold):
            passed.append(''.join([inf[i - 1], inf[i], inf[i + 1], inf[i + 2]]))
        else:
            failed.append(''.join([inf[i - 1], inf[i], inf[i + 1], inf[i + 2]]))
    with open(pass_file, 'w') as ouf:
        ouf.write(''.join(passed))
    with open(fail_file, 'w') as ouf:
        ouf.write(''.join(failed))


# call check-functions and write the result of filtering (without failed reads)
def not_save_check_and_write(inf, pass_file, gc_bounds, len_bounds, q_treshold):
    passed = []
    for i in range(1, len(inf), 4):
        if gc_filter(inf[i], gc_bounds) and length_filter(inf[i], len_bounds) and quality_filter(inf[i+2], q_treshold):
            passed.append(''.join([inf[i - 1], inf[i], inf[i + 1], inf[i + 2]]))
    with open(pass_file, 'w') as ouf:
        ouf.write(''.join(passed))


def main(input_fastq,
         output_file_prefix,
         gc_bounds=(0, 100),
         length_bounds=(0, 2**32),
         quality_threshold=0,
         save_filtered=False):

    inf = []
    with open(input_fastq) as in_file:
        for line in in_file:
            inf.append(line)

    if save_filtered:
        pass_file = output_file_prefix + '_passed.fastq'
        fail_file = output_file_prefix + '_failed.fastq'
        save_check_and_write(inf, pass_file, fail_file, gc_bounds, length_bounds, quality_threshold)
    else:
        pass_file = output_file_prefix + '_passed.fastq'
        not_save_check_and_write(inf, pass_file, gc_bounds, length_bounds, quality_threshold)


if __name__ == '__main__':
    input_fastq = input()
    output_file_prefix = input()
    main(input_fastq, output_file_prefix, gc_bounds=(20, 70), length_bounds=(30, 110), quality_threshold=30, save_filtered=True)
