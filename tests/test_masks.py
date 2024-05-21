import pytest
from src.masks import mask_account_number, mask_card_number


@pytest.mark.parametrize("input_number, expected_output",
                         [("1234567890123456", "1234 56** **** 3456"),
                          ("9876543210987654", "9876 54** **** 7654")])
def test_mask_card_number(input_number, expected_output):
    assert mask_card_number(input_number) == expected_output


@pytest.mark.parametrize("input_number, expected_output",
                         [("1234567890", "**7890"),
                          ("9876543210", "**3210")])
def test_mask_account_number(input_number, expected_output):
    assert mask_account_number(input_number) == expected_output


if __name__ == "__main__":
    pytest.main()
