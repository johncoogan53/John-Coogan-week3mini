"""importing polars for data manipulation and pyplot for plotting"""
import pythonproject.src.lib1 as lib1
import matplotlib.pyplot as plt

df = lib1.load_data_from_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
print(lib1.summary_statistics(df))

plt.scatter(df["disp"], df["mpg"], alpha=0.5)
plt.title("Vehicle MPG vs Displacement")
plt.xlabel("Displacement")
plt.ylabel("MPG")
plt.show()
