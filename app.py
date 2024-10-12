import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Set the title of the web app
st.title('Car Listings Dashboard')

# Header
st.header('Exploratory Data Analysis of Car Listings')

# Histogram of car prices
st.subheader('Distribution of Car Prices')
price_hist = px.histogram(df, x='price', nbins=50, title='Distribution of Car Prices')
st.plotly_chart(price_hist)

# Checkbox to show scatter plot
show_scatter = st.checkbox('Show Scatter Plot of Price vs. Odometer')

if show_scatter:
    st.subheader('Scatter Plot: Price vs. Odometer')
    scatter_plot = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer', color='fuel')
    st.plotly_chart(scatter_plot)

# Additional insights or analysis can be added here
st.write("You can explore the distribution of various car attributes and make data-driven decisions.")
