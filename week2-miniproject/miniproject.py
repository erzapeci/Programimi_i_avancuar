import sys  # For handling command-line arguments and system-related functions
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical and array-based operations
from scipy import stats  # For statistical functions such as z-score and mode

# Function to load data from a CSV file
def load_data(file_path):
    """
    Reads data from a CSV file and returns it as a pandas DataFrame.

    :param file_path: A string representing the path to the CSV file.
    :return: A pandas DataFrame containing the data from the CSV file.
    """
    try:
        # Try reading the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        # If an error occurs (e.g., file not found), print a message and exit.
        print(f"Error reading file: {e}")
        sys.exit(1)

# Function to calculate basic statistics for a given column
def calculate_stats(df, column):
    """
    Calculates and prints basic statistics (mean, median, mode, standard deviation)
    for a specified column in the DataFrame.

    :param df: The pandas DataFrame containing the data.
    :param column: The name of the column to analyze (string).
    """
    # Check if the specified column exists in the DataFrame.
    if column not in df.columns:
        print(f"Column '{column}' not found in the data.")
        return

    # Extract the data from the specified column.
    data = df[column]
    print(f"Statistics for {column}:")

    # Calculate and display the mean using NumPy.
    print(f"Mean: {np.mean(data):.2f}")

    # Calculate and display the median using NumPy.
    print(f"Median: {np.median(data):.2f}")

    # Calculate and display the mode using SciPy.
    # 'stats.mode' returns an array, so we take the first element [0][0].
    print(f"Mode: {stats.mode(data, keepdims=True)[0][0]}")

    # Calculate and display the standard deviation using NumPy. ddof=1 for sample standard deviation.
    print(f"Standard Deviation: {np.std(data, ddof=1):.2f}")

# Function to generate a text-based histogram
def generate_text_histogram(df, column, bins=10):
    """
    Generates and prints a text-based histogram for a specified column.

    :param df: The pandas DataFrame containing the data.
    :param column: The name of the column to analyze (string).
    :param bins: The number of bins to use in the histogram (integer, default=10).
    """
    # Check if the specified column exists in the DataFrame.
    if column not in df.columns:
        print(f"Column '{column}' not found in the data.")
        return

    # Extract the data from the specified column.
    data = df[column]

    # Use NumPy to compute the histogram values and bin edges.
    hist, bin_edges = np.histogram(data, bins=bins)
    print(f"Histogram for {column}:")

    # Loop through each bin and print out a '#' character for each count.
    for i in range(len(hist)):
        # bin_edges[i] is the lower bound, bin_edges[i+1] is the upper bound of the bin
        # hist[i] is the number of data points in that bin.
        print(f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f}: {'#' * hist[i]}")

# Function to calculate Pearson correlation between two columns
def find_correlation(df, col1, col2):
    """
    Finds and prints the Pearson correlation coefficient between two columns in the DataFrame.

    :param df: The pandas DataFrame containing the data.
    :param col1: The name of the first column (string).
    :param col2: The name of the second column (string).
    """
    # Check if both columns exist in the DataFrame.
    if col1 not in df.columns or col2 not in df.columns:
        print("One of the columns was not found in the data.")
        return

    # Compute and print the correlation coefficient.
    correlation = df[col1].corr(df[col2])
    print(f"Correlation between {col1} and {col2}: {correlation:.2f}")

# Function to detect outliers in a column based on Z-scores
def detect_outliers(df, column, threshold=2.0):
    """
    Identifies outliers using the Z-score method and prints rows containing outliers.

    :param df: The pandas DataFrame containing the data.
    :param column: The name of the column to analyze (string).
    :param threshold: The Z-score threshold above which data points are considered outliers (float).
    """
    # Check if the specified column exists in the DataFrame.
    if column not in df.columns:
        print(f"Column '{column}' not found in the data.")
        return

    # Compute Z-scores for each value in the column.
    z_scores = np.abs(stats.zscore(df[column]))

    # Identify rows where the Z-score exceeds the threshold.
    outliers = df[z_scores > threshold]
    print(f"Outliers for {column} (Threshold={threshold}):")
    print(outliers)

# Main function to handle command-line arguments and run the appropriate analysis
def main():
    """
    Main function to handle command-line arguments and execute the appropriate analysis.
    """
    if len(sys.argv) < 4:
        print("Usage: python data_analysis.py <file> <command> <column> [options]")
        return

    # Parse command-line arguments.
    file_path = sys.argv[1]
    command = sys.argv[2]
    column = sys.argv[3]

    # Load the CSV data.
    df = load_data(file_path)

    # Execute the command based on user input.
    if command == "stats":
        calculate_stats(df, column)
    elif command == "histogram":
        bins = int(sys.argv[4]) if len(sys.argv) > 4 else 10
        generate_text_histogram(df, column, bins)
    elif command == "correlation":
        if len(sys.argv) < 5:
            print("Usage: python data_analysis.py <file> correlation <column1> <column2>")
            return
        find_correlation(df, column, sys.argv[4])
    elif command == "outliers":
        threshold = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
        detect_outliers(df, column, threshold)
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
