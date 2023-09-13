"""importing polars for data manipulation and pyplot for plotting"""
import polars as pl
import matplotlib.pyplot as plt

df = pl.read_csv("https://www.statlearning.com/s/Auto.csv", ignore_errors=True)
print(df.describe())

plt.scatter(df["displacement"], df["mpg"], alpha=0.5)
plt.title("Vehicle MPG vs Displacement")
plt.xlabel("Displacement")
plt.ylabel("MPG")
plt.show()
