import pytest
from src.processing import filter_by_state, sort_by_date


# fixture для предоставления тестовых данных
@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2022-01-15"},
        {"state": "PENDING", "date": "2022-02-10"},
        {"state": "EXECUTED", "date": "2022-02-01"},
        {"state": "FAILED", "date": "2022-03-05"}
    ]


# Параметризованный тест для функции filter_by_state
@pytest.mark.parametrize("state_status, expected_output",
                         [("EXECUTED", [{"state": "EXECUTED", "date": "2022-01-15"},
                                        {"state": "EXECUTED", "date": "2022-02-01"}]),
                          ("FAILED", [{"state": "FAILED", "date": "2022-03-05"}])])
def test_filter_by_state(sample_data, state_status, expected_output):
    assert filter_by_state(sample_data, state_status) == expected_output


# Параметризованный тест для функции sort_by_date
@pytest.mark.parametrize("time, expected_output",
                         [("increasing", [{"state": "EXECUTED", "date": "2022-01-15"},
                                          {"state": "EXECUTED", "date": "2022-02-01"},
                                          {"state": "PENDING", "date": "2022-02-10"},
                                          {"state": "FAILED", "date": "2022-03-05"}]),
                          ("decreasing", [{"state": "FAILED", "date": "2022-03-05"},
                                          {"state": "PENDING", "date": "2022-02-10"},
                                          {"state": "EXECUTED", "date": "2022-02-01"},
                                          {"state": "EXECUTED", "date": "2022-01-15"}])])
def test_sort_by_date(sample_data, time, expected_output):
    assert sort_by_date(sample_data, time) == expected_output
