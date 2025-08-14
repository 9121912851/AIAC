def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts amount from one currency to another using exchange rates.

    :param amount: float, the amount of money to convert
    :param from_currency: str, the currency code to convert from
    :param to_currency: str, the currency code to convert to
    :param rates: dict, exchange rates with respect to a base currency
    :return: float, converted amount
    """
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Currency not supported.")
    # Convert amount to base currency, then to target currency
    base_amount = amount / rates[from_currency]
    converted = base_amount * rates[to_currency]
    return converted

# Example exchange rates (relative to USD)
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'INR': 83.2,
    'GBP': 0.79
}

# Few-shot prompting examples:
# Example 1: Convert 100 USD to EUR
print("Example 1: 100 USD to EUR =", convert_currency(100, 'USD', 'EUR', exchange_rates))

# Example 2: Convert 1000 INR to GBP
print("Example 2: 1000 INR to GBP =", convert_currency(1000, 'INR', 'GBP', exchange_rates))

# Take input from user
try:
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD, EUR, INR, GBP): ").upper()
    to_curr = input("To currency (e.g., USD, EUR, INR, GBP): ").upper()
    result = convert_currency(amount, from_curr, to_curr, exchange_rates)
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
except Exception as e:
    print("Error:", e)