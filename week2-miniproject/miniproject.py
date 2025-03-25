import sys  # For handling command-line arguments and system-related functions
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical and array-based operations
from scipy import stats  # For statistical functions such as z-score and mode

def load_data(file_path):
    """
    Reads data from a CSV file and returns it as a pandas DataFrame.

    :param file_path: A string representing the path to the CSV file.
    :return: A pandas DataFrame containing the data from the CSV file.
    """
    try:
        # Use pandas to read the CSV file.
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        # If an error occurs (e.g., file not found), print a message and exit.
        print(f"Error reading file: {e}")
        sys.exit(1)

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

    # Calculate the mean using NumPy.
    print(f"Mean: {np.mean(data):.2f}")

    # Calculate the median using NumPy.
    print(f"Median: {np.median(data):.2f}")

    # Calculate the mode using SciPy. 
    # 'stats.mode' returns an array, so we take the first element [0][0].
    print(f"Mode: {stats.mode(data, keepdims=True)[0][0]}")

    # Calculate the standard deviation using NumPy. ddof=1 for sample standard deviation.
    print(f"Standard Deviation: {np.std(data, ddof=1):.2f}")

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

    # Use the built-in DataFrame method .corr() to compute correlation.
    correlation = df[col1].corr(df[col2])
    print(f"Correlation between {col1} and {col2}: {correlation:.2f}")

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

    # Extract the data from the specified column.
    data = df[column]

    # Compute the Z-score for each value in the column.
    # zscore() returns an array of z-scores for each element.
    z_scores = np.abs(stats.zscore(data))

    # Filter the DataFrame to rows where the z-score is greater than the threshold.
    outliers = df[z_scores > threshold]
    print(f"Outliers for {column} (Threshold={threshold}):")
    print(outliers)

def main():
    """
    Main function to handle command-line arguments and execute the appropriate analysis.
    
    Usage:
      python data_analysis.py <file> <command> <column> [options]

    Commands:
      stats <column>
      histogram <column> <bins>
      correlation <column1> <column2>
      outliers <column_name> <threshold>
    """
    # Check if there are enough command-line arguments.
    if len(sys.argv) < 4:
        print("Usage: python data_analysis.py <file> <command> <column> [options]")
        return
    
    # Extract the arguments.
    file_path = sys.argv[1]
    command = sys.argv[2]
    column = sys.argv[3]

    # Load the CSV data into a DataFrame.
    df = load_data(file_path)
    
    if command == "stats":
        # Calculate and print basic statistics.
        calculate_stats(df, column)
    elif command == "histogram":
        # Generate a text-based histogram. 
        # If user specified a bin size, parse it; otherwise default to 10.
        bins = int(sys.argv[4]) if len(sys.argv) > 4 else 10
        generate_text_histogram(df, column, bins)
    elif command == "correlation":
        # For correlation, we need two columns: the one provided in sys.argv[3] 
        # and an additional one in sys.argv[4].
        if len(sys.argv) < 5:
            print("Usage: python data_analysis.py <file> correlation <column1> <column2>")
            return
        find_correlation(df, column, sys.argv[4])
    elif command == "outliers":
        # Detect outliers based on a threshold if provided; default = 2.0.
        threshold = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
        detect_outliers(df, column, threshold)
    else:
        # If the command is not recognized, print a message.
        print("Unknown command.")

# Entry point for the script when called from the command line.
if __name__ == "__main__":
    main()

# Below this point is a simple demonstration if the script is run directly (not from the command line).
if __name__ == "__main__":
    # Create a test DataFrame in memory for demonstration purposes.
    data = {
        "column1": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "column2": [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    }
    df = pd.DataFrame(data)

    # Demonstrate the 'calculate_stats' function on "column1".
    calculate_stats(df, "column1")
    print("\n")
    
    # Demonstrate the 'generate_text_histogram' function on "column1".
    generate_text_histogram(df, "column1", bins=5)
    print("\n")
    
    # Demonstrate the 'find_correlation' function between "column1" and "column2".
    find_correlation(df, "column1", "column2")
    print("\n")
    
    # Demonstrate the 'detect_outliers' function on "column1" with threshold=1.5.
    detect_outliers(df, "column1", threshold=1.5)
    print("\n")
