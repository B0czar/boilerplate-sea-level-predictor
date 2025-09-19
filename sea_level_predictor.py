import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit (1880 through 2050)
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    x_pred = pd.Series(range(1880, 2051))
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, color="red")

    # Create second line of best fit (2000 through 2050)
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
    )
    x_recent = pd.Series(range(2000, 2051))
    y_recent = intercept_recent + slope_recent * x_recent
    plt.plot(x_recent, y_recent, color="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return for testing
    plt.savefig("sea_level_plot.png")
    return plt.gca()