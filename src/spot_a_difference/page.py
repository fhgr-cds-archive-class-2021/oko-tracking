import streamlit as st
from .loader import load
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def get_heatmap(**kwargs):
    data = kwargs.get("data")
    showScatter = kwargs.get("showScatter")
    current_img = kwargs.get("current_img")
    scaledImageWidth = kwargs.get("scaledImageWidth")
    scaledImageHeight = kwargs.get("scaledImageHeight")

    fig = plt.figure()

    x = data["Fixation point X"].to_list()
    y = data["Fixation point Y"].to_list()
    plt.xlim([0, max(x)])
    plt.ylim([0, max(y)])
    ext = [0, scaledImageWidth, 0, scaledImageHeight]
    plt.imshow(current_img, zorder=0, extent=ext)

    xmin, xmax = np.min(x), np.max(x)
    ymin, ymax = np.min(y), np.max(y)
    values = np.vstack([x, y])

    # Gaussian KDE.
    kernel = stats.gaussian_kde(values, bw_method=.1)
    # Grid density (number of points).
    gd_c = complex(0, 50)
    # Define x,y grid.
    x_grid, y_grid = np.mgrid[xmin:xmax:gd_c, ymin:ymax:gd_c]
    positions = np.vstack([x_grid.ravel(), y_grid.ravel()])
    # Evaluate kernel in grid positions.
    k_pos = kernel(positions)

    kde = np.reshape(k_pos.T, x_grid.shape)
    plt.imshow(np.rot90(kde), cmap=plt.get_cmap('RdYlBu_r'), extent=ext, zorder=1, alpha=0.6)
    if showScatter:
        plt.scatter(x, y, s=1, zorder=2, color='white')
    return fig

def page():
    col1, col2 = st.columns(2)
    
    with col1:
        taskSelection = st.selectbox(
            "Please choose a task", ["Task1", "Task2"]
        )

    with col2:
        showScatter = st.checkbox('Show/hide scatter plot')

    data, current_img, scaledImageWidth, scaledImageHeight = load(taskSelection)
    fig = get_heatmap(
        data=data,
        showScatter=showScatter,
        current_img=current_img, 
        scaledImageWidth=scaledImageWidth,
        scaledImageHeight=scaledImageHeight
    )
    st.pyplot(fig.figure)
