import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets


# Task 1

train_df = pd.read_csv('train.csv')
train_df.head()

train_df.plot(x='pos', y=['A', 'C', 'T', 'G'], kind='bar')
train_df.plot(x='pos', y=['A_fraction', 'C_fraction', 'T_fraction', 'G_fraction'], kind='bar', stacked=True)

# Task 2

train_part = train_df.query('matches > matches.mean()')[['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]
train_part.to_csv('train_part.csv', index=False)
pd.read_csv('train_part.csv').head()

# Task 3

wine_df = datasets.load_wine(as_frame=True).frame  # load dataset

wine_df.head()
wine_df.info()  # features' type
wine_df.iloc[:, :13].describe()  # summary with mean, std etc.

# Pivot table
wine_df.pivot_table(index=['target'],
                    values=['alcohol', 'magnesium', 'total_phenols', 'flavanoids',
                            'color_intensity', 'hue'],
                    aggfunc=np.mean).rename(columns={'target': 'class',
                                                     'alcohol': 'mean_alcohol',
                                                     'magnesium': 'mean_magnesium',
                                                     'total_phenols': 'mean_total_phenols',
                                                     'flavanoids': 'mean_flavanoids',
                                                     'color_intensity': 'mean_color_intensity',
                                                     'hue': 'mean_hue'})
# distribution of classes
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(wine_df.target, discrete=True, ax=ax)
plt.xticks([0, 1, 2])

# 13 plots with distribution of each feature
fig2, axs = plt.subplots(3, 5)
axs = axs.ravel()
for i, ax in enumerate(axs):
    sns.kdeplot(wine_df.iloc[:, i], ax=ax)
    if i == 12:
        break

# pairplot
sns.pairplot(wine_df, hue='target', palette="tab10")

# Task 4 (not complete)


def read_gff(path):
    df = pd.read_csv(path, sep='\t', skiprows=1, header=None)
    df.columns = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
    return df


def read_bed6(path):
    i = 0
    with open(path) as f:
        line = f.readline()
        while line.startswith('browser') or line.startswith('track'):
            i += 1
            line = f.readline()
    df = pd.read_csv(path, sep=r'[\t ]+', skiprows=i, header=None, engine='python', comment='#')
    possible_cols = ['chrom', 'start', 'end', 'name', 'score', 'strand', 'thickStart', 'thickEnd',
                     'itemRgb', 'blockCount', 'blockSizes', 'blockStarts']
    df.columns = possible_cols[:df.shape[1]]
    return df


gff = read_gff('rrna_annotation.gff')
gff.head()
bed = read_bed6('alignment.bed')
bed.head()

# change attributes
gff.attributes = gff.attributes.str.extract(pat=r'(\d+S)')

# RNA metrics
rna_types = gff.pivot_table(index=['seqid', 'attributes'],
                            values='phase',
                            aggfunc='count').rename(columns={'phase': 'number'})

sns.histplot(x='seqid', hue='attributes', data=gff, multiple='dodge')
