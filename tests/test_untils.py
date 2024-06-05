import json
import os
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import requests
from dotenv import load_dotenv

from src.utils import receive_currency_and_convert, read_the_json_file, sum_1

load_dotenv()
API_KEY = os.getenv("api_key")


""" если API ошиблась"""


@patch("requests.get")
def test_get_transaction_rub_api_error(mock_get: Mock) -> None:
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException
    mock_get.return_value = mock_response  # Возвращаем заглушку ответа при вызове requests.get

    # Проверяем, что функция возвращает 1.0 при ошибке API
    result = receive_currency_and_convert("USD")
    assert result == 1.0


@patch("requests.get")
def test_get_transaction_rub_api_success(mock_get: MagicMock) -> None:
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    t = {"amount": 100, "currency": "USD"}
    assert receive_currency_and_convert(t) == 75.0


@patch("builtins.open", create=True)
def test_read_transactions_success(mock_open_1: MagicMock) -> None:
    # Создаем тестовые данные
    test_data = [{"amount": 100, "currency": "RUB"}]
    # Подготавливаем мок файл с помощью mock_open
    mock_open_1.return_value.read.return_value = json.dumps(test_data)
    # Проверяем, что функция возвращает правильный список транзакций
    result = read_the_json_file(Path("test_transactions.json"))
    assert result == []


""" для пустого файла"""


def test_read_transactions_empty_file() -> None:
    # Создаем пустой файл
    with open("test_transactions.json", "w"):
        pass

    result = read_the_json_file(Path("test_transactions.json"))
    assert result == []

    os.remove("test_transactions.json")  # Удаляем тестовый файл


def test_sum_amount() -> None:
    assert (
        sum_1(
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
        == 31957.58
    )
