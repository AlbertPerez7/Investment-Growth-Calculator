import sys
import io
from Investment.inputs import get_user_inputs
from Investment.calculator import simulate_investment, save_detailed_results_to_txt
from Investment.plotter import plot_investment

def main():
    """
    Main entry point for the Investment Calculator app.
    Handles user input, investment simulation, result display,
    optional saving to TXT, and final plot visualization.
    """
    try:
        print("📊 Welcome to the Investment Calculator")
        params = get_user_inputs()

        # Capture printed output for optional saving
        buffer = io.StringIO()
        sys.stdout = buffer

        final_value, contributions, values, non_reinvested_dividends, per_year_data = simulate_investment(**params)

        total_contributed = params["initial_capital"] + params["annual_contribution"] * params["years"]
        profit = final_value - total_contributed

        print(f"\n💰 Total contributed: {total_contributed:.2f}")
        print(f"📈 Total value after {params['years']} years: {final_value:.2f}")
        print(f"🟢 Net profit before taxes: {profit:.2f}")
        if not params["reinvest_dividends"] and params["investment_type"] in ('1', '2'):
            print(f"💸 Total dividends received (not reinvested): {non_reinvested_dividends:.2f}")

        # Restore stdout and show results
        sys.stdout = sys.__stdout__
        print(buffer.getvalue())

        # Keep asking until the user enters a valid response
        while True:
            save = input("\n📥 Do you want to save all results as shown to a TXT file? (y/n): ").lower().strip()
            if save in ('y', 'yes'):
                filename = input("Enter filename (e.g., results.txt): ").strip()
                if not filename.lower().endswith(".txt"):
                    filename += ".txt"
                save_detailed_results_to_txt(buffer.getvalue(), filename)
                print(f"✅ Results saved to '{filename}'")
                break
            elif save in ('n', 'no'):
                print("ℹ️ Results were not saved.")
                break
            else:
                print("❌ This is not valid. Please enter 'y' (yes) or 'n' (no).")

        # Display investment growth plot
        plot_investment(contributions, values)

    except Exception as e:
        # Ensure stdout is restored in case of error
        sys.stdout = sys.__stdout__
        print("❌ An error occurred:", str(e))

if __name__ == "__main__":
    main()
