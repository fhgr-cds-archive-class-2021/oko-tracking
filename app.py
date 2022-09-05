import streamlit as st
import pandas as pd
import numpy as np

# import data tsv with panda
df = pd.read_csv('Project_oko_tracking Metrics.tsv', sep='\t')
df.head()