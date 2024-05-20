from unittest.mock import patch, MagicMock
from src.utils import read_transactions_from_file, convert_amount_to_rubles


def test_read_transactions_from_file_with_valid_file():
    with patch("builtins.open") as mock_open:
        mock_file = MagicMock()
        mock_file.__enter__.return_value = [{"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}]
        mock_open.return_value = mock_file

        transactions = read_transactions_from_file("data/operations.json")

        assert transactions == [{"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}]


def test_convert_amount_to_rubles():
    with patch("requests.get") as mock_get:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"USD": 1, "RUB": 80, "EUR": 0.9}}
        mock_get.return_value = mock_response

        rubles_amount = convert_amount_to_rubles(transaction)

        assert rubles_amount == 8000


if __name__ == 'main':
    test_read_transactions_from_file_with_valid_file()
    test_convert_amount_to_rubles()
    print("All tests passed.")
