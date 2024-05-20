from typing import List, Dict


def filter_by_state(data: List[Dict], state_status: str) -> List[Dict]:
    """
    Фильтрация списка словарей по значению ключа "state"

    Args:
        data: список словарей на фильтрацию
        state_status: Значение ключа "state", по которому нужно фильтровать

    Returns:
        Отфильтрованный список словарей.
    """
    return [item for item in data if item["state"].upper() == state_status.upper()]


def sort_by_date(data: List[Dict], sort_order: str) -> List[Dict]:
    """
    Сортировка списка словарей по значению ключа "date"

    Args:
        data: Список словарей, которые нужно отсортировать
        sort_order: Порядок сортировки "increasing" (по возрастанию) или "decreasing" (по убыванию)

    Returns:
        Отсортированный список словарей.
    """
    if sort_order == "increasing":
        return sorted(data, key=lambda item: item["date"], reverse=True)
    elif sort_order == "decreasing":
        return sorted(data, key=lambda item: item["date"])
    else:
        raise ValueError("Invalid sort order. Choose 'increasing' or 'decreasing'")


def test_filter_by_state() -> None:
    test_list = [
        {"id": 1, "state": "executed"},
        {"id": 2, "state": "pending"},
        {"id": 3, "state": "executed"},
    ]

    # Test cases for state_status="executed"
    filtered_list_executed = filter_by_state(test_list, "executed")
    assert len(filtered_list_executed) == 2
    assert all(item["state"] == "EXECUTED" for item in filtered_list_executed)

    # Test cases for state_status="pending"
    filtered_list_pending = filter_by_state(test_list, "pending")
    assert len(filtered_list_pending) == 1
    assert all(item["state"] == "PENDING" for item in filtered_list_pending)


def test_sort_by_date() -> None:
    test_list = [
        {"id": 1, "date": "2022-01-01"},
        {"id": 2, "date": "2022-02-15"},
        {"id": 3, "date": "2022-03-10"},
    ]

    # Test cases for sort_order="increasing"
    sorted_list_increasing = sort_by_date(test_list, "increasing")
    assert sorted_list_increasing == [
        {"id": 3, "date": "2022-03-10"},
        {"id": 2, "date": "2022-02-15"},
        {"id": 1, "date": "2022-01-01"},
    ]

    # Test cases for sort_order="decreasing"
    sorted_list_decreasing = sort_by_date(test_list, "decreasing")
    assert sorted_list_decreasing == [
        {"id": 1, "date": "2022-01-01"},
        {"id": 2, "date": "2022-02-15"},
        {"id": 3, "date": "2022-03-10"},
    ]
