import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

### function to generate histogram
def make_histplot(data: pd.Series, var_name: str):
    """
    Function to create a histogram of a variable
    
    :param data: List or series containing the numerical variable's data
    :param var_name: Name of the variable
    """

    data_mean = np.mean(data)
    data_median = np.median(data)

    plt.figure(figsize = (10, 6))
    ax = sns.histplot(x = data, color = "blue", alpha = 0.5)

    for c in ax.containers:
        labels = ["{:.1%}".format(val.get_height() / len(data)) for val in c]
        ax.bar_label(c, labels = labels)
    
    plt.axvline(data_mean, color = "red", linestyle = "dashed", label = "Mean")
    plt.axvline(data_median, color = "green", linestyle = "dashed", label = "Median")
    plt.title("{} distribution".format(var_name), fontsize = 16)
    plt.xlabel(var_name, fontsize = 12)
    plt.ylabel("Frequency", fontsize = 12)
    plt.legend()
    plt.show()
    plt.clf()


def make_countplot(data: pd.Series, var_name: str):
    plt.figure(figsize = (10, 6))
    ax = sns.countplot(x = data, palette = "bright", stat = "percent")

    for c in ax.containers:
        ax.bar_label(c, fmt = "{:.1f}%")
    
    plt.title("Proportions by category", fontsize = 16)
    plt.xlabel(var_name.title(), fontsize = 12)
    plt.ylabel("Category proportion", fontsize = 12)
    plt.show()
    plt.clf()