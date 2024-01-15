def investment():
    monthly_amt = int(input("Enter monthly inveestment: "))
    return monthly_amt
def yearly_rate():
    rate = float(input("Enter yearly interest rate: "))
    return rate
def years():
    yrs = int(input("Enter number of years: "))
    return yrs
def future_value(monthly_amt, rate, yrs):
    f_value = 0
    for i in range(yrs * 12):
        f_value += monthly_amt
        m_int = f_value * rate / (12 * 100)
        f_value += m_int
    return f_value

def main():
    loop = True
    while True:
        monthly_amt = investment()
        rate = yearly_rate()
        yrs = years()
        future_value(monthly_amt, rate, yrs)
        cont = input("Continue? (y/n): ")
        if cont.lower() != "y":
            break
        else:
            loop = True

main()
