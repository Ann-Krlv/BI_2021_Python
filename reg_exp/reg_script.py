import re
import seaborn as sns

with open('README.md', 'w') as readme:
    intro = '# Regexp HomeWork\nScript "reg_script.py" has created the results below.\n'
    task1 = '## Task 1\n Results are in the files "ftps" (all link cases) and "ftps_unique" (unique links)\n'
    readme.write(intro)
    readme.write(task1)

#  Task 1

pattern1 = re.compile(r'\b(ftp\.[^;\s]*)[;\s]?')
# \non_word_char (ftp. [everything, except ';' and spaces]*) [; or spaces]?

with open('references', 'r') as ftp_raw:
    results = pattern1.findall(ftp_raw.read())
with open('ftps', 'w') as ftps:
    for i in results:
        ftps.write(f'{i}\n')
with open('ftps_unique', 'w') as ftps_uq:
    results_uq = set(results)
    for i in results_uq:
        ftps_uq.write(f'{i}\n')


#  Task 2

pattern2 = re.compile(r'\d+')
# just one or more digit(s)

with open('2430AD', 'r') as text:
    numbers = pattern2.findall(text.read())
with open('README.md', 'a') as res:
    res.write('## Task 2\nAll numbers in the text\n\n')
    for i in numbers:
        res.write(f'* {i}\n')

#  Task 3

pattern3 = re.compile(r'\b\w*[Aa]+\w*\b')
# distinct word (\b) with [A or a]+ and surrounded by any or not letter/digit/_ symbols (\w*)

with open('2430AD', 'r') as text:
    words_A = pattern3.findall(text.read())

words_A = set([i.lower() for i in words_A])
with open('README.md', 'a') as res:
    res.write('## Task 3\nAll words with "a" character\n\n')
    for i in words_A:
        res.write(f'{i} ')

#  Task 4

pattern4 = re.compile(r'[A-Z]+[^!?.]*!')
# start with upper case [A-Z], end with "!". Any (*) symbols between except '!', '?' or '.' [^!?.]

with open('2430AD', 'r') as text:
    sentences = pattern4.findall(text.read())
with open('README.md', 'a') as res:
    res.write('\n ## Task 4\nAll sentences that end with "!"\n\n')
    for i in sentences:
        res.write(f'* {i}\n')

#  Task 5

pattern5 = re.compile(r'\b\w+\b')
# just every word: one or more (+) letter, digit or _ between word separators (\b)

with open('2430AD', 'r') as text:
    words = pattern5.findall(text.read())

all_words = set([i.lower() for i in words])
len_list = [len(i) for i in all_words]

# histogram plot
plot = sns.histplot(len_list, discrete=True)
plot.set_title('Length distribution for unique words in 2431AD')
plot.set_xticks(range(1, max(len_list)))
plot.figure.savefig('word_len.png')

with open('README.md', 'a') as readme:
    readme.write('## Task 5\n')
    readme.write('![plot](word_len.png)')
