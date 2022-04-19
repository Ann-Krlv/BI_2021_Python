# Multiprocessing in Python

This 16th? homework in BI is devoted to programming multiprocessing on Python.

### 1. Variant 2
The fasta_counter.py is a command line tool that take fasta file as input, count symbols at each sequence in the file and print one line with results per sequence as stdout.
The script use biopython, so you can run (better in virtual environment).
```commandline
pip install -r requirements.txt
```
and then make the script executable:
```commandline
chmod +x fasta_counter.py
```

Usage example:

```commandline
path_to/fasta_counter.py --input your_file.fasta --threads 1 > output.txt
```

As example fasta you can use *Lamellibrachia satsuma* reference genome (accession number GCA_022478865.1, file size - 674 MB).

(Also you can run `path_to/fasta_counter.py --help` for information about options)

### 2. Bonus task

Notebook Interesting_plot in this directory contains code and plot from the lecture (that shows how execution time depends on running process number).