import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(14, 6))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    first_result = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    year = range(1880, 2051, 1)
    adjusted_level = first_result.intercept + first_result.slope * year
    plt.plot(year, adjusted_level)

    # Create second line of best fit
    df_alter = df[(df["Year"] >= 2000)]
    second_result = linregress(x=df_alter["Year"], y=df_alter["CSIRO Adjusted Sea Level"])
    year = range(2000, 2051, 1)
    adjusted_level = second_result.intercept + second_result.slope * year
    plt.plot(year, adjusted_level)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()