import numpy as np
import pandas as pd
from itertools import combinations 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Plot Distributions of given features 
def PlotDists(features_to_plot):
    fig = plt.figure(figsize=(22,30))

    for i in range(features_to_plot.shape[1]):
        ax = fig.add_subplot(7, 3, i+1)
        sns.distplot(features_to_plot[features_to_plot.columns.values[i]], ax=ax)

# Plot features versus targets
def PlotFeaturesTargets(features_to_plot,targets_to_plot,data_to_plot):
    '''
    features_to_plot: Pandas DataFrame of features
    targets_to_plot:  Pandas DataFrame of targets
    data_to_plot:     Pandas DataFrame of entire dataset (features and targets)
    '''
    fig = plt.figure(figsize=(18,30))

    num_features = features_to_plot.shape[1]

    # will have 3 cols, so to calculate number of rows we need:
    num_rows = np.ceil( num_features/3. )


    for i in range(num_features):
        axis = fig.add_subplot(num_rows, 3, i+1)
        plot = sns.scatterplot(x=features_to_plot.iloc[:,i], y=targets_to_plot.iloc[:,0], data=data_to_plot, ax=axis)
    plt.show()

# Plot each feature against each other feature
def PlotFeatures(data_to_plot):
    '''
    data_to_plot: Pandas Dataframe that holds the features to be plottted against each other and the targets for the color
    Targets need to be the last column in the data frame
    There are only seven colors, so if there are more than seven targets new colors need to be added.
    '''
    fig = plt.figure(figsize=(18,100))
    
    features_to_plot = data_to_plot.iloc[:,:-1]
    targets_to_plot = data_to_plot.iloc[:,-1:]
    
    num_features = features_to_plot.shape[1]
    
    # Calculate combination. n = num_features : p = 2, since we want to plot 2 features against each other
    combinations_to_plot = list(combinations(features_to_plot, 2))
    # num_plots tells us how many plots to make
    num_plots = len(combinations_to_plot)    

    # will have 3 cols, so to calculate number of rows we need:
    num_rows = np.ceil( num_plots/3. ) # Will round up
    
    # Palette for each target (0,1,2)
    colors = ['#E69600','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7'] # These are seven color-blind friendly colors
    colors = colors[:len(np.unique(targets_to_plot))]
    # ['#fc8d59','#ffffbf','#91bfdb'] These are three distinct color-blind friendly colors
    palette = sns.color_palette(colors)

    for i in range(num_plots):
        axis = fig.add_subplot(num_rows, 3, i+1)
        plot = sns.relplot(x=combinations_to_plot[i][0], y=combinations_to_plot[i][1], hue=data_to_plot.columns.values[-1], palette=palette,data=data_to_plot, ax=axis)
        plt.close(plot.fig) # close figure that seaborn creates when sns.relplot is called 
    plt.show()
