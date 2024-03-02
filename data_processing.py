import pandas as pd

def load_trade_data(file_path):
    """
    Load trade data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file containing trade data.
        
    Returns:
        pd.DataFrame: DataFrame containing the loaded trade data.
    """
    try:
        data = pd.read_csv(file_path)
        # Assuming the file contains columns for timestamp, price, and volume
        # Conversion and cleaning steps can be added here
        return data
    except Exception as e:
        print(f"Error loading trade data: {e}")
        return pd.DataFrame()

def load_market_depth_data(file_path):
    """
    Load market depth data from a CSV file.
    
    Parameters:
        file_path (str): Path to the CSV file containing market depth data.
        
    Returns:
        pd.DataFrame: DataFrame containing the loaded market depth data.
    """
    try:
        data = pd.read_csv(file_path)
        # Assuming the file contains columns for bid/ask prices and quantities
        # Conversion and cleaning steps can be added here
        return data
    except Exception as e:
        print(f"Error loading market depth data: {e}")
        return pd.DataFrame()
