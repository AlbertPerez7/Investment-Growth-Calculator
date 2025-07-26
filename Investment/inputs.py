def get_float_input(prompt):
    """
    Repeatedly prompts the user for a float until a valid input is provided.

    Args:
        prompt (str): Text to display when asking for input.

    Returns:
        float: Validated float input from the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt):
    """
    Repeatedly prompts the user for an integer until a valid input is provided.

    Args:
        prompt (str): Text to display when asking for input.

    Returns:
        int: Validated integer input from the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_user_inputs():
    """
    Interactively collects all user inputs related to the investment simulation,
    including parameters that depend on the selected investment type.

    Returns:
        dict: Dictionary containing all simulation parameters.
    """
    print("\nSelect investment type:")
    print("1. Fund/ETF")
    print("2. Individual Stock")
    print("3. Derivative")

    # Ensure a valid investment type is selected
    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice in ('1', '2', '3'):
            break
        else:
            print("Invalid option. Choose 1, 2 or 3.")

    # Base input for all types
    initial_capital = get_float_input("Enter initial capital: ")
    annual_contribution = get_float_input("Enter annual contribution: ")
    years = get_int_input("Enter number of years: ")
    expected_return = get_float_input(
        "Enter expected average compound annual growth rate (CAGR) (in %): "
    ) / 100

    # Default values
    dividend_yield = 0
    expense_ratio = 0
    spread_cost = 0
    reinvest_dividends = True
    broker_fee_percent = 0
    broker_fee_fixed = 0

    # Additional inputs based on investment type
    if choice == '1':  # Fund/ETF
        dividend_yield = get_float_input("Enter average annual dividend yield (in %): ") / 100
        expense_ratio = get_float_input("Enter fund manager's expense ratio (in %): ") / 100

    elif choice == '2':  # Individual Stock
        dividend_yield = get_float_input("Enter average annual dividend yield (in %): ") / 100
        print("\nSelect broker fee type:")
        print("1. Percentage of portfolio per year")
        print("2. Fixed annual fee")
        fee_choice = input("Enter fee type (1/2): ")
        if fee_choice == '1':
            broker_fee_percent = get_float_input("Enter annual broker fee (in %): ") / 100
        elif fee_choice == '2':
            broker_fee_fixed = get_float_input("Enter fixed annual broker fee (in EUR): ")

    elif choice == '3':  # Derivative
        spread_cost = get_float_input("Enter estimated annual spread cost (in %): ") / 100

    # Ask about dividend reinvestment if applicable
    if choice in ('1', '2'):
        while True:
            reinvest = input("Reinvest dividends? (yes/no): ").lower()
            if reinvest in ('yes', 'y', 'ye'):
                reinvest_dividends = True
                break
            elif reinvest in ('no', 'n'):
                reinvest_dividends = False
                break
            else:
                print("Please enter 'yes' or 'no'.")

    # Return all gathered inputs in a structured dictionary
    return {
        "initial_capital": initial_capital,
        "annual_contribution": annual_contribution,
        "years": years,
        "expected_return": expected_return,
        "dividend_yield": dividend_yield,
        "expense_ratio": expense_ratio,
        "spread_cost": spread_cost,
        "reinvest_dividends": reinvest_dividends,
        "broker_fee_percent": broker_fee_percent,
        "broker_fee_fixed": broker_fee_fixed,
        "investment_type": choice
    }
