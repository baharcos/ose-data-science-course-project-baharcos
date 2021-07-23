import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from auxiliary.colors import get_colors
from auxiliary.colors import plot_colors

colors = get_colors('categorical', 12)

def participation_share_plot(data, title, column):
    
    """Function that takes a subseted treatment data and plots the share 
    of students who take-up the offered treatment
    
    Args:
        data(pd.DateFrame)
        title(str)
        column(str)
    
    Returns: 
        plt.subplot """
    
    width = 0.35
    sns.set_palette(colors)
    fig, ax = plt.subplots()

    rslt = data.groupby('sex')[column].value_counts(normalize=True).sort_index()
    y_female, y_male = rslt['F'].to_numpy(), rslt['M'].to_numpy()
    labels = rslt.index.get_level_values(1).unique().sort_values()

    x = np.array(range(len(y_female)))

    ax.bar(x - width / 2, y_female, width, label="female")
    ax.bar(x + width / 2, y_male, width, label="male")

    ax.set_xticks(x)
    ax.set_xticklabels(['nontakers', 'participants'])

    ax.legend()
    ax.set_title(title)
    ax.set_ylabel('Share')