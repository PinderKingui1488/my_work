import pytest

from src.widget import convert_date, number_or_account


@pytest.mark.parametrize(
    "input_date, expected_result",
    [
        ("2022-04-13T15:30:00", "13.04.2022"),
        ("2023-12-25T08:00:00", "25.12.2023"),
    ],
)
def test_convert_date(input_date: str, expected_result: str) -> None:
    assert convert_date(input_date) == expected_result


@pytest.fixture
def account_number_fixture() -> str:
    return "Visa 1111222233334444"


@pytest.fixture
def card_number_fixture() -> str:
    return "Счет 1234567890123456"


def test_number_or_account(card_number_fixture: str) -> None:
    data = number_or_account(card_number_fixture)
    assert data == "Счет **3456"
