import streamlit as st
from functions import get_x, get_y
import plotly.express as px

st.title("In Search for Happiness")
x = st.selectbox(label="Select the data for X-axis", options=["GDP", "Happiness", "Generosity"])
y = st.selectbox(label="Select the data for Y-axis", options=["GDP", "Happiness", "Generosity"])
st.subheader(f"{x} and {y}")

# Gets the dat from functions
data_x = get_x(x)
data_y = get_y(y)

# Gives the scatter graph
figure = px.scatter(x=data_x, y=data_y, labels={"x": f"{x}", "y": f"{y}"})
# Return the graph
st.plotly_chart(figure, kind="scatter")
