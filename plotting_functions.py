import matplotlib.pyplot as plt

def plot_price_movement(data):
    """
    Plot price movement over time.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing price data and timestamps.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['timestamp'], data['price'], label='Price Movement')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Price Movement Over Time')
    plt.legend()
    plt.show()

# You can add additional plotting functions for different visualizations here.
