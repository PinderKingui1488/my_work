def mask_card_number(user_card_number: str) -> str:
    masked_number = user_card_number[:4] + " " + user_card_number[4:6] + "** **** " + user_card_number[12:]
    return masked_number


def mask_account_number(user_account_number: str) -> str:
    masked_number = "**" + user_account_number[-4:]
    return masked_number
