def calculate_summary_statistics(data):
    """
    Calculate summary statistics for given financial data.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing financial data.
        
    Returns:
        dict: Dictionary containing summary statistics like mean, median, std, etc.
    """
    summary_stats = {
        'mean': data.mean(),
        'median': data.median(),
        'std': data.std(),
        'min': data.min(),
        'max': data.max()
    }
    return summary_stats

# You can add more complex analysis functions here based on your needs.
