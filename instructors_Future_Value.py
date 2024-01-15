import locale as lc

def future_value(monthly_investment, y_interest, years):
    monthly_interest = y_interest / (12 * 100)
    months = years * 12
    future_value_calc = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_investment = future_value * monthly_interest
        future_value += monthly_interest
    return future_value_calc

def main():
    choice = "y"
    while choice == "y":
        monthly_investment = int(input("Enter monthly investment:\t\t"))
        yearly_interest = float(input("Enter yearly interest:\t\t"))
        years = int(input("Enter number of years:\t\t"))

        future_value = future_value(monthly_investment, yearly_interest, years)
        lc.setlocale(lc.LC_ALL, "en_US")
        monthly_investment = lc.currency(monthly_investment, grouping = True)
        future_value_calc = lc.currency(future_value, grouping = True)

        print(f"{'Monthly investment:':{20}} {'monthly_investment':>10}")
        print(f"{'Interest Rate:':20} {yearly_interest:>10.2f}")
        print(f"{'Years':20} {years:>10}")
        print(f"{'Future Value:':20} {future_value_calc:>10.2f}")

        choice = input("Continue? (y/n): ").lower()
        print()

if __name__ == "__main__":
    main()