import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def plot_investment(contribution, value):
    """
    Plots the evolution of investment value and cumulative contributions.

    Args:
        contribution (list): List of total contributions per year.
        value (list): List of portfolio values per year.
    """
    years = list(range(len(contribution)))  # X-axis values: 0 to number of years

    plt.figure(figsize=(10, 6))
    plt.plot(years, value, label="Investment Value")
    plt.plot(years, contribution, label="Total Contribution", linestyle='--')

    plt.xlabel("Year")
    plt.ylabel("Amount (Thousands of EUR)")
    plt.title("Investment Growth vs Contributions")
    plt.legend()
    plt.grid(True)

    # Format Y-axis ticks as 'k' for thousands (e.g. 20,000 → 20k)
    formatter = FuncFormatter(lambda x, _: f'{x/1000:.0f}k')
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.tight_layout()
    plt.show()
