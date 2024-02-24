import pandas as pd

df = pd.read_csv("happy.csv")


# Gets the x-axis data as per the user option
def get_x(x):
    if x == "GDP":
        x_data = df["gdp"]
    elif x == "Happiness":
        x_data = df["happiness"]
    else:
        x_data = df["generosity"]
    return x_data


# Gets the y-axis data as per the user option
def get_y(y):
    if y == "GDP":
        y_data = df["gdp"]
    elif y == "Happiness":
        y_data = df["happiness"]
    else:
        y_data = df["generosity"]
    return y_data
