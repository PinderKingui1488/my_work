from fromskypro.src.widget import convert_date, number_or_account


def test_convert_date():
    input_date = "2022T06-30T15:30:00"
    assert convert_date(input_date) == "30.06.2022"


def test_number_or_account():
    user_input_account = "Счет 1234567890"
    assert number_or_account(user_input_account) == "Счет **********"

    user_input_card = "John Doe 1234 5678 9012 3456"
    assert number_or_account(user_input_card) == "John Doe ************3456"
    