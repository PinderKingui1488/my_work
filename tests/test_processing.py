from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# fixture для предоставления тестовых данных
@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
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
def test_filter_by_state(sample_data: List[Dict[str, Any]], state_status: str,
                         expected_output: List[Dict[str, Any]]) -> None:
    """Тестирует функцию filter_by_state с разными состояниями."""
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
def test_sort_by_date(sample_data: List[Dict[str, Any]], time: str, expected_output: List[Dict[str, Any]]) -> None:
    """Тестирует функцию sort_by_date с разными типами сортировки."""
    assert sort_by_date(sample_data, time) == expected_output
