import json
import os
from pathlib import Path
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def read_the_json_file(file_path: Path) -> List[Dict[str, Any]]:
    """Считывает транзакции из JSON-файла."""
    try:
        with file_path.open(encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def receive_currency_and_convert(currency: Any) -> Any:
    """Получает курс валюты от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/fixer/latest?symbols={currency}"
    try:
        response = requests.get(url, headers={"apikey": API_KEY}, timeout=5)
        response.raise_for_status()
        """Поднимает исключение, если код ответа не 2xx"""
        response_data = response.json()
        rate = response_data["rates"]["RUB"]
        return rate
    except requests.exceptions.RequestException as e:
        print(f"Ошибка API: {e}")
        """# Возвращаем 1.0 как значение по умолчанию"""
        return 1.0


def sum_1(transaction: dict) -> float:

    total = 0.0
    if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":
        total += float(transaction["operationAmount"]["amount"])
    elif transaction.get("operationAmount", {}).get("currency", {}).get("code") == "EUR":
        total += float(transaction["operationAmount"]["amount"]) * receive_currency_and_convert("EUR")
    elif transaction.get("operationAmount", {}).get("currency", {}).get("code") == "USD":
        total += float(transaction["operationAmount"]["amount"]) * receive_currency_and_convert("USD")
    return total


if __name__ == "__main__":
    operations_path = Path("../data/operations.json")  # Путь к файлу с операциями
    transactions = read_the_json_file(operations_path)
    total_rub = sum_1(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )

    print(f"Общая сумма в рублях: {total_rub:.2f}")
