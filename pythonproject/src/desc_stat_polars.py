"""importing polars for data manipulation and pyplot for plotting"""
import matplotlib.pyplot as plt
import polars as pl


def load_data_from_csv(file_path):
    """Load the desired CSV data file for descriptive statistics
    takes a str file path to the CSV file
    returns a pd.DataFrame"""

    try:
        data = pl.read_csv(file_path, ignore_errors=True)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None


def summary_statistics(dataframe):
    """Takes the DataFrame and calls the describe function on it
    Args:
        DataFrame
    Returns:
        DataFrame containing summary statistics"""

    return dataframe.describe()


def main():
    """This is a main function for loading
    the csv and performing descriptive stats with visualization"""
    data_cars = load_data_from_csv(
        "https://gist.githubusercontent.com/"
        "seankross/a412dfbd88b3db70b74b/raw/"
        "5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    print(summary_statistics(data_cars))

    plt.scatter(data_cars["disp"], data_cars["mpg"], alpha=0.5)
    plt.title("Vehicle MPG vs Displacement")
    plt.xlabel("Displacement")
    plt.ylabel("MPG")
    plt.show()


if __name__ == "__main__":
    main()
