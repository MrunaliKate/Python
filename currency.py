import requests

def get_exchange_rates():
    api_key = "90f49c598674adc995f311407c7497a7"
    url = "https://openexhangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount
    if from_currency != "USD":
        amount /= exchange_rates[from_currency]

    amount *= exchange_rates[to_currency]
    return amount

def main():
    get_exchange_rates = get_exchange_rates()

    amount = float(input("Enter the amount: ")) 
    from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want to convert from (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()    
