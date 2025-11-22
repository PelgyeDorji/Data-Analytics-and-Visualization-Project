import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px #for interactive maps and charts

st.title("Earthquake Magnitude and Frequency: Global Patterns")

@st.cache_data #loads data once, and remembers it and skips reloading.
def load_data():
    return pd.read_csv('data/cleaned_earthquakes.xls')

df = load_data() # runs the function and saves the table as df.


min_mag = st.sidebar.slider("Min Magnitude", 4.0, 7.0, 4.0)
#adds a sliding bar on the left side for picking minimum magnitude
continents = st.sidebar.multiselect(
    "Continent",
    df['continent'].unique(),
    default=df['continent'].unique()
)
# adds checkboxes for continents to be shown.


filtered_df = df[(df['magnitude'] >= min_mag) & (df['continent'].isin(continents))]


fig1 = px.scatter_geo(
    filtered_df,
    lat='latitude',
    lon='longitude',
    size='magnitude',
    color='continent',
    title='Earthquake Locations and Magnitudes'
)
# px.scatter_geo() is to build map.
# uses the filtered_df.
# pins dots on the map in accordance to the latitude and the longitude.
# size="" makes the dots bigger for stronger quakes.
# color="" colors dots for continent
# title= labels the chart
st.plotly_chart(fig1, use_container_width=True)


fig2 = px.bar(
    filtered_df.groupby('continent')['magnitude'].mean().reset_index(),
    x='continent',
    y='magnitude',
    title='Average Magnitude by Continent'
)
st.plotly_chart(fig2, use_container_width=True)


