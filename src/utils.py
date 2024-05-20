import json
import requests

API_URL = "https://api.exchangeratesapi.io/latest?base=USD"


def read_transactions_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def convert_amount_to_rubles(transaction):
    amount = transaction.get("operationAmount", {}).get("amount")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency_code == "USD" or currency_code == "EUR":
        response = requests.get(API_URL)
        if response.status_code == 200:
            rates = response.json().get("rates", {})
            usd_rate = rates.get("RUB")
            if currency_code == "USD":
                return amount * usd_rate
            elif currency_code == "EUR":
                eur_rate = rates.get("EUR")
                return amount * eur_rate
    return amount

