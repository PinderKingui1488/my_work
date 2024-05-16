from fromskypro.src.masks import mask_card_number, mask_account_number

def test_mask_card_number():
    assert mask_card_number("1234567812345678") == "1234 56 **** 5678"
    assert mask_card_number("9876543210987654") == "9876 54 **** 7654"

def test_mask_account_number():
    assert mask_account_number("1234567890") == "7890"
    assert mask_account_number("9876543210") == "3210"
