from Bio.Data import CodonTable
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Student:
    def __init__(self, name, age=18, spec='Unknown'):
        self.name = name
        self.age = age
        self.spec = spec
        self.hp = 100
        self.knowledge = 0

    def __str__(self):
        return f'Student {self.name}\nAge: {self.age}\nSpecialization: {self.spec}'

    def drink_beer(self, n_pints=1):
        self.hp += n_pints * 10
        self.knowledge -= 10 * (2**(n_pints - 1))

    def to_study(self, n_hours=1):
        self.knowledge += n_hours * 10
        self.hp -= 10 * (2 ** (n_hours - 1))

    def check_status(self):
        if self.hp < 0:
            return 'Dead', [self.hp, self.knowledge]
        elif self.knowledge < 0:
            return f'Otchisleno', [self.hp, self.knowledge]
        else:
            return 'Lives and studies', [self.hp, self.knowledge]


class RNA:
    codons = CodonTable.ambiguous_rna_by_id[1]
    permitted_rna_nucleotides = {'A', 'G', 'C', 'U'}

    def __init__(self, seq):
        self.seq = seq.upper()

    def translate(self, r_frame=0, to_stop=False):
        prot_chain = ''
        for nucl in range(r_frame, len(self.seq), 3):
            if len(self.seq[nucl:(nucl + 3)]) < 3:
                return prot_chain
            if self.seq[nucl:(nucl + 3)] in self.codons.stop_codons:
                if to_stop:
                    return prot_chain
                else:
                    prot_chain += '*'
            else:
                prot_chain += self.codons.forward_table[self.seq[nucl:(nucl + 3)]]
        return prot_chain

    def reverse_transcript(self):
        if len(set(self.seq).difference(self.permitted_rna_nucleotides)) == 0:
            return self.seq.replace()
        else:
            raise ValueError(f'Unknown nucleotides in the sequence: '
                             f'{set(self.seq).difference(self.permitted_rna_nucleotides)}')


class PositiveSet(set):
    def __init__(self, lst):
        super().__init__([i for i in lst if i > 0])

    def add(self, other):
        if other > 0:
            super().add(other)


class FastQ:
    reads = []
    n_reads = 0

    def __init__(self, path):
        self.path = path
        with open(path) as in_handle:
            for read in FastqGeneralIterator(in_handle):
                self.reads.append(read[1])
                self.n_reads += 1

    def __str__(self):
        return f'FastQC file: {self.path}'

    def count_reads(self):
        return self.n_reads

    def len_histplot(self):
        len_array = np.zeros(self.n_reads)
        for i in range(self.n_reads):
            len_array[i] = len(self.reads[i])
        sns.histplot(len_array, discrete=True)
        plt.title('Read length distribution')
        plt.show()

    def gc_percentage(self):
        gc_content = np.zeros(self.n_reads)
        for i in range(self.n_reads):
            gc_content[i] = ((self.reads[i].count('G') + self.reads[i].count('C')) / len(self.reads[i]))
        return np.mean(gc_content) * 100

    def k_mers_freq_histplot(self, k=4):
        k_mers = {}
        for read in self.reads:
            for i in range(len(read) - k + 1):
                k_mer = read[i:(i + k)]
                if len(set(k_mer).difference(set('AGCT'))) != 0:
                    continue
                elif k_mer not in k_mers:
                    k_mers[k_mer] = 1
                else:
                    k_mers[k_mer] += 1
        plt.bar(x=k_mers.keys(), height=k_mers.values())
        plt.title(f'Distribution of k-mers (with k={k})')
        plt.show()

    def show_stats(self):
        print(f'Number of reads: {self.n_reads}\n'
              f'GC percentage: {round(self.gc_percentage(), 2)}%')
        self.len_histplot()
        self.k_mers_freq_histplot()
