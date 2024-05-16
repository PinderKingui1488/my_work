import pytest


from fromskypro.src.generators import filter_currency, transaction, number_generator


@pytest.fixture
def transactions() -> list:
    """Список для теста функций"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize("currency, expected", [("USD", 939719570), ("RUB", 873106923)])
def test_filter_currency(transactions: list, currency: str, expected: int) -> None:
    assert next(filter_currency(transactions, currency))["id"] == expected


def test_transaction(transactions: list) -> None:
    assert next(transaction(transactions)) == "Перевод организации"


@pytest.mark.parametrize("first, last, expected", [(1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002",
                                                           "0000 0000 0000 0003", "0000 0000 0000 0004",
                                                           "0000 0000 0000 0005"]),
                                                   (4129313413480001, 4129313413480002,
                                                    ["4129 3134 1348 0001", "4129 3134 1348 0002"])])
def test_number_generator(first: int, last: int, expected: list) -> None:
    assert list(number_generator(first, last)) == expected
