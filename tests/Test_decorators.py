from src.decorators import homework_function


def test_my_function() -> None:
    assert homework_function(1, 2) == 3
    assert homework_function(2, 2) == 4
    assert homework_function(3, 2) == 5
    assert homework_function(4, 2) == 6
    assert homework_function(5, 2) == 7
