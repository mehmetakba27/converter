# currency_converter.py

import requests

# Function to fetch exchange rates from an API
def get_exchange_rate(base_currency, target_currency):
    try:
        # API endpoint for exchange rates
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        
        # Check if the response is valid
        if response.status_code == 200 and target_currency in data['rates']:
            return data['rates'][target_currency]
        else:
            print(f"Error: Unable to fetch exchange rate for {base_currency} to {target_currency}.")
            return None
    except Exception as e:
        print("Error fetching data:", e)
        return None

# Main function to convert currencies
def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed.")

# User interaction
def main():
    print("Currency Converter - Convert between different currencies")
    try:
        amount = float(input("Enter the amount: "))
        base_currency = input("Enter the base currency (e.g., USD): ").upper()
        target_currency = input("Enter the target currency (e.g., EUR): ").upper()
        convert_currency(amount, base_currency, target_currency)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    main()
