def calculate_power_bill(rate_per_unit, units_consumed):
    """
    Calculate the total power bill.

    :param rate_per_unit: float, the cost per unit of electricity
    :param units_consumed: float, the number of units consumed
    :return: float, total bill amount
    """
    return rate_per_unit * units_consumed

if __name__ == "__main__":
    try:
        rate = float(input("Enter the rate per unit: "))
        units = float(input("Enter the number of units consumed: "))
        if rate < 0 or units < 0:
            print("Rate and units consumed must be non-negative.")
        else:
            total_bill = calculate_power_bill(rate, units)
            print(f"Total power bill amount: {total_bill}")
    except ValueError:
        print("Invalid input. Please enter numeric values for rate and units.")
