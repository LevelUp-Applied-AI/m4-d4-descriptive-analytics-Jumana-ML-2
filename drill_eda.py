"""Core Skills Drill — Descriptive Analytics

Compute summary statistics, plot distributions, and create a correlation
heatmap for the sample sales dataset.

Usage:
    python drill_eda.py
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def compute_summary(df):
    """Compute summary statistics for all numeric columns.

    Args:
        df: pandas DataFrame with at least some numeric columns

    Returns:
        DataFrame containing count, mean, median, std, min, max
        for each numeric column. Save the result to output/summary.csv.
    """
    # Select only numeric columns to avoid errors with text/dates
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Compute the specific statistics requested
    summary_df = numeric_df.agg(['count', 'mean', 'median', 'std', 'min', 'max'])
    
    # Save the result
    summary_df.to_csv("output/summary.csv")
    
    return summary_df


def plot_distributions(df, columns, output_path):
    """Create a 2x2 subplot figure with histograms for the specified columns.

    Args:
        df: pandas DataFrame
        columns: list of 4 column names to plot (use numeric columns)
        output_path: file path to save the figure (e.g., 'output/distributions.png')

    Returns:
        None — saves the figure to output_path
    """
    # Create a 2x2 grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Flatten the 2D array of axes to easily loop through it (1D array of 4 axes)
    axes = axes.flatten()
    
    # Loop through the columns and axes simultaneously
    for i, col in enumerate(columns):
        # sns.histplot with kde=True adds the Kernel Density Estimate overlay
        sns.histplot(data=df, x=col, kde=True, ax=axes[i], color='skyblue')
        axes[i].set_title(f"Distribution of {col}")
        axes[i].set_xlabel(col)
        axes[i].set_ylabel("Frequency")
        
    # Adjust layout so titles and labels don't overlap
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(output_path)
    
    # Clear the current figure from memory
    plt.close()


def plot_correlation(df, output_path):
    """Compute Pearson correlation matrix and visualize as a heatmap.

    Args:
        df: pandas DataFrame with numeric columns
        output_path: file path to save the figure (e.g., 'output/correlation.png')

    Returns:
        None — saves the figure to output_path
    """
    # 1. Select only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # 2. Compute Pearson correlation matrix
    corr_matrix = numeric_df.corr(method='pearson')
    
    # 3. Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, 
                annot=True,          # Show the correlation numbers
                cmap='coolwarm',     # Blue for negative, Red for positive correlation
                fmt=".2f",           # Format numbers to 2 decimal places
                linewidths=0.5)      # Add a small line between squares
    
    plt.title("Correlation Heatmap of Numeric Variables")
    plt.tight_layout()
    
    # 4. Save the figure
    plt.savefig(output_path)
    plt.close()


def main():
    """Load data, compute summary, and generate all plots."""
    os.makedirs("output", exist_ok=True)

    # 1. Load the CSV
    try:
        df = pd.read_csv("data/sample_sales.csv")
    except FileNotFoundError:
        print("Error: data/sample_sales.csv not found.")
        return

    # --- FEATURE ENGINEERING ---
    if 'revenue' not in df.columns and 'quantity' in df.columns and 'unit_price' in df.columns:
        df['revenue'] = df['quantity'] * df['unit_price']
        
    if 'date' in df.columns:
        df['month'] = pd.to_datetime(df['date']).dt.month
    # --------------------------------------------------------

    # 2. Call compute_summary
    print("Computing summary statistics...")
    compute_summary(df)

    # 3. Choose 4 numeric columns for distributions
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_columns) >= 4:
        cols_to_plot = numeric_columns[:4]
    else:
        cols_to_plot = numeric_columns 
        
    print(f"Plotting distributions for: {cols_to_plot}...")
    plot_distributions(df, cols_to_plot, "output/distributions.png")

    # 4. Call plot_correlation
    print("Plotting correlation heatmap...")
    plot_correlation(df, "output/correlation.png")
    
    print("All tasks completed successfully! Check the 'output' folder.")

if __name__ == "__main__":
    main()
