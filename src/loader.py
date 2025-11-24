# src/loader.py
import pandas as pd
import os  # <--- This import is required for the script to work!

def load_news_data(filepath):
    """
    Loads and parses the financial news dataset.
    """
    # Check if file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file was not found at: {filepath}")

    # Load CSV
    print(f"Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    
    # Convert date column to datetime objects if 'date' column exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    return df

# This block allows you to run the script directly for testing
if __name__ == "__main__":
    # Get the root directory of the project (one level up from this file)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Construct the correct path to the data file
    test_path = os.path.join(project_root, 'data', 'raw_analyst_ratings.csv')

    print(f"Attempting to load data from: {test_path}")

    try:
        df = load_news_data(test_path)
        print(f"Success! Loaded {len(df)} rows.")
        print(df.head())
    except Exception as e:
        print(f"Error: {e}")