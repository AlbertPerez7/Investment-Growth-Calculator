import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import csv

def simulate_investment(
    initial_capital, annual_contribution, years, expected_return,
    dividend_yield, expense_ratio, spread_cost, reinvest_dividends,
    broker_fee_percent, broker_fee_fixed, investment_type
):
    """
    Simulates investment growth over time, accounting for contributions,
    returns, dividends, and costs depending on the investment type.

    Returns:
        total (float): Final portfolio value
        total_contributed (list): Total contributed capital by year
        total_value (list): Portfolio value by year
        total_dividends_received (float): Non-reinvested dividends
        per_year_data (list): List of yearly breakdown dictionaries
    """
    total = initial_capital
    total_contributed = [initial_capital]
    total_value = [initial_capital]
    total_fees_paid = 0
    total_dividends_received = 0
    per_year_data = []

    for year in range(1, years + 1):
        year_data = {"Year": year}
        year_data["Starting Total"] = round(total, 2)

        dividends = total * dividend_yield if investment_type in ('1', '2') else 0
        year_data["Dividends"] = round(dividends, 2)

        if reinvest_dividends and investment_type in ('1', '2'):
            total += dividends
            year_data["Dividends Reinvested"] = True
        elif investment_type in ('1', '2'):
            total_dividends_received += dividends
            year_data["Dividends Reinvested"] = False

        total *= (1 + expected_return)
        year_data["After Growth"] = round(total, 2)

        fees = total * expense_ratio if investment_type == '1' else 0
        spread = total * spread_cost if investment_type == '3' else 0
        broker_fee = (
            broker_fee_fixed + (total * broker_fee_percent)
            if investment_type == '2' else 0
        )

        total_fees_paid += (fees + spread + broker_fee)
        total -= (fees + spread + broker_fee)
        year_data["Fees"] = round(fees, 2)
        year_data["Spread"] = round(spread, 2)
        year_data["Broker Fee"] = round(broker_fee, 2)
        year_data["After Fees"] = round(total, 2)

        total += annual_contribution
        year_data["After Contribution"] = round(total, 2)
        year_data["Cumulative Fees Paid"] = round(total_fees_paid, 2)

        total_contributed.append(initial_capital + annual_contribution * year)
        total_value.append(total)

        per_year_data.append(year_data)

        # Optional print for debug
        print(f"\nYear {year}:")
        for key, value in year_data.items():
            print(f"- {key}: {value}")

    return total, total_contributed, total_value, total_dividends_received, per_year_data


def plot_investment(contribution, value):
    """
    Visualizes the growth of the portfolio and total contributions.
    """
    years = list(range(len(contribution)))
    plt.figure(figsize=(10, 6))
    plt.plot(years, value, label="Investment Value")
    plt.plot(years, contribution, label="Total Contribution", linestyle='--')
    plt.xlabel("Year")
    plt.ylabel("Amount (Thousands of EUR)")
    plt.title("Investment Growth vs Contributions")
    plt.legend()
    plt.grid(True)

    formatter = FuncFormatter(lambda x, _: f'{x/1000:.0f}k')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.tight_layout()
    plt.show()


import csv

def save_detailed_results_to_txt(text, filename):
    """
    Saves the full formatted terminal output (text block) to a .txt file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)




def get_float_input(prompt):
    """Prompts the user for a float value."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt):
    """Prompts the user for an integer value."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")
