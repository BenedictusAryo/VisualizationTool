# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 14:41:28 2019

@author: Benedict Aryo

VisualizationTool tools for visualization in jupyter notebook
"""
# Import library
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import matplotlib.gridspec as gridspec
import itertools

def plot_boundary(X, y, models, labels):
    """Plot decision Boundary for Ensamble Visualization
        need to defined models (list), title(list)"""
    #Ukuran Grid models (3,3)
    gs = gridspec.GridSpec(3, 3)
    #Ukuran Plotsize
    fig = plt.figure(figsize=(15,12))
    
    for clf, lab, grd in zip(models,
                         labels,
                         itertools.product([0, 1, 2], repeat=2)):
        #Training si model
        clf.fit(X, y)
        ax = plt.subplot(gs[grd[0], grd[1]])
        fig = plot_decision_regions(X=X, y=y, clf=clf, legend=2)
        plt.title(lab)

    plt.show()