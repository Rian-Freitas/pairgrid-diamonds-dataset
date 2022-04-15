import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing the dataset and cleaning

diamonds_db = pd.read_csv("diamonds.csv")

pd.DataFrame.dropna(diamonds_db, inplace=True)
pd.DataFrame.drop_duplicates(diamonds_db, inplace=True)

# Creating de plotting function

def plot_hists(feature):

    # Just to ensure the variable inserted is really a feature, not a datapoint component
    if feature not in {'x','y','z'}:
        fig, ax =plt.subplots(1,2, figsize=(15,5))
        sns.histplot(diamonds_db, x=feature, stat='density', bins=50, ax=ax[0])
        sns.histplot(diamonds_db, x=feature, hue='cut', palette='viridis', stat='density', bins=50, ax=ax[1])
        fig.show()
    else:
        raise TypeError("Insert a dataset feature, datapoint components are not acceptable.")