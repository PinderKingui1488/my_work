import json
from pathlib import Path
from typing import Any, Dict, List

from src.external_API import get_currency_rate
from src.logger import setup_logging

logger = setup_logging()


def read_transaction_data(file_path: Path) -> List[Dict[str, Any]]:
    """Считывает транзакции из JSON-файла."""
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при чтении JSON-файла: {e}")
        return []


def calculate_total_amount(transaction: dict) -> float:
    """Суммирует суммы всех транзакций"""
    total_amount = 0.0
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    transaction_amount = float(transaction.get("operationAmount", {}).get("amount", 0.0))

    if currency_code == "RUB":
        total_amount += transaction_amount
    elif currency_code == "EUR":
        total_amount += transaction_amount * get_currency_rate("EUR")
    elif currency_code == "USD":
        total_amount += transaction_amount * get_currency_rate("USD")
    else:
        logger.warning(f"Неизвестная валюта: {currency_code}")

    logger.info(f"Сумма транзакции: {total_amount:.2f} RUB")
    return total_amount


if __name__ == "__main__":
    transactions_file_path = Path("../data/operations.json")  # Путь к файлу с операциями
    transactions_data = read_transaction_data(transactions_file_path)
    total_amount_rub = calculate_total_amount(
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
    print(f"Общая сумма в рублях: {total_amount_rub:.2f}")
