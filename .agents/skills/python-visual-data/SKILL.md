---
name: python-visual-data
description: >-
  Experiential Python for visual data analytics, aesthetic color palette extraction,
  Plotly interactive charts, and Streamlit dashboard building. Use for hands-on,
  visual data exploration without dry blackboard mathematics.
---

# Experiential Python: Visual Data & Interactive Analytics

This skill enables experiential learning of Python through tangible, visual outputs.

## 1. Aesthetic Image Color Palette Extractor
Extract the dominant, harmonious hex color palette from an image:
```python
from colorthief import ColorThief
import matplotlib.pyplot as plt

def get_aesthetic_palette(image_path, num_colors=5):
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=num_colors)
    hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in palette]
    return hex_colors
```

## 2. Interactive Sports Analytics with Plotly
Plot table tennis stroke velocities and impact trajectories in 3D:
```python
import plotly.express as px
import pandas as pd

def plot_athletic_performance(df):
    fig = px.scatter_3d(
        df, 
        x="paddle_angle_deg", 
        y="ball_spin_rpm", 
        z="shot_velocity_kph", 
        color="result",
        title="3D Athletic Stroke Dynamics"
    )
    fig.show()
```

## 3. Instant Streamlit Web Apps
Deploy an interactive web app in 15 lines of code:
```bash
pip install streamlit plotly
streamlit run app.py
```
```python
import streamlit as st
import plotly.express as px

st.title("⚡ Table Tennis Match Intelligence")
slider_val = st.slider("Select Reaction Time Threshold (ms)", 80, 250, 120)
st.write(f"Analyzing shots under {slider_val}ms reaction window...")
```
