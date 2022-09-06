def load(task):
    import pandas as pd
    import matplotlib.image as mpimg 
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as st
    import statsmodels.api as sm
    import seaborn as sns
    from sklearn.neighbors import KernelDensity
    from PIL import Image
    import os

    file_path = os.path.dirname(__file__)

    df = pd.read_csv(f"{file_path}/data.tsv", sep='\t')
    df = df[df['Fixation point X'].notna()]
    current_img = mpimg.imread(f"{file_path}/{task}.png")
    screenWidth = 1920
    screenHeight = 1080
    imageWidth = current_img.shape[1]
    imageHeight = current_img.shape[0]
    scaledImageWidth = screenWidth
    scaledImageHeight = (imageHeight / imageWidth) * scaledImageWidth
    heightReduce = (screenHeight - scaledImageHeight) / 2
    lineY = screenHeight / 2
    data = df.loc[df["Eye movement type"] == "Fixation"]
    data = df.loc[df["Sensor"] == "Eye Tracker"]
    data["Gaze event duration"] = data["Gaze event duration"].apply(lambda x: x**2)
    maxy = data["Fixation point Y"].max()

    # Rotate PointY on X-Axis
    data["Fixation point Y"] = data["Fixation point Y"].apply(lambda y: y - (y-lineY)*2)

    # Reduce rest height of image since its centralized on tobii on screen
    data["Fixation point Y"] = data["Fixation point Y"].apply(lambda y: y - heightReduce)

    # Remove points outside of image
    data = data.loc[(data["Fixation point X"] <= scaledImageWidth) & (data["Fixation point X"] >= 0)]
    data = data.loc[(data["Fixation point Y"] <= scaledImageHeight) & (data["Fixation point Y"] >= 0)]

    data = data.loc[data["Presented Stimulus name"] == f"{task} (1)"]

    return data, current_img, scaledImageWidth, scaledImageHeight