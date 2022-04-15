import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp

# Importing the dataset and cleaning

diamonds_db = pd.read_csv('diamonds.csv')

pd.DataFrame.dropna(diamonds_db, inplace=True)
pd.DataFrame.drop_duplicates(diamonds_db, inplace=True)

# Creating the Pearson Correlation Coefficient plotting function

def correlate(x,y, **kwargs):
    pearsoncorr = sp.stats.pearsonr(diamonds_db[x.name], diamonds_db[y.name])[0]
    label = f'R = {round(pearsoncorr, 2)}'
    ax = plt.gca()
    ax.annotate(label, xy = (0.3, 0.5), size=10, xycoords=ax.transAxes, backgroundcolor='white')

g = sns.PairGrid(diamonds_db, hue='cut', palette='viridis')
g.map_diag(sns.histplot, bins=50)
g.map_lower(sns.scatterplot)
g.map_upper(correlate)
g.add_legend
