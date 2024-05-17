from typing import Generator


def filter_currency(data: list, currency_code: str) -> Generator[dict, None, None]:
    """Принимает список, возвращает генератор словарей, фильтрованных по валюте"""
    for item in data:
        if item["operationAmount"]["currency"]["code"] == currency_code.upper():
            yield item


def transaction(data: list) -> Generator[str, None, None]:
    """Принимает список словарей, возвращает генератор описаний"""
    for item in data:
        yield item["description"]


def number_generator(start_range: int, end_range: int) -> Generator[str, None, None]:
    """Генератор номеров нужных нам карт"""
    for number in range(start_range, end_range + 1):
        card_number = f"{number:0>16}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
