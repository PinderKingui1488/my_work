from src.masks import mask_account_number, mask_card_number


def test_mask_card_number() -> None:
    assert mask_card_number("1234567812345678") == "1234 56 **** 5678"
    assert mask_card_number("9876543210987654") == "9876 54 **** 7654"


def test_mask_account_number() -> None:
    assert mask_account_number("1234567890") == "7890"
    assert mask_account_number("9876543210") == "3210"
