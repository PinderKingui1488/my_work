from fromskypro.src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    test_list = [
        {"id": 1, "state": "executed"},
        {"id": 2, "state": "pending"},
        {"id": 3, "state": "executed"},
    ]

    # Тестирование для state_status="executed"
    filtered_list_executed = filter_by_state(test_list, "executed")
    assert len(filtered_list_executed) == 2
    assert all(item["state"] == "EXECUTED" for item in filtered_list_executed)

    # Тестирование для state_status="pending"
    filtered_list_pending = filter_by_state(test_list, "pending")
    assert len(filtered_list_pending) == 1
    assert all(item["state"] == "PENDING" for item in filtered_list_pending)

def test_sort_by_date():
    test_list = [
        {"id": 1, "date": "2022-01-01"},
        {"id": 2, "date": "2022-02-15"},
        {"id": 3, "date": "2022-03-10"},
    ]

    # Тестирование для времени "increasing"
    sorted_list_increasing = sort_by_date(test_list, "increasing")
    assert sorted_list_increasing == [
        {"id": 3, "date": "2022-03-10"},
        {"id": 2, "date": "2022-02-15"},
        {"id": 1, "date": "2022-01-01"},
    ]

    # Тестирование для времени "decreasing"
    sorted_list_decreasing = sort_by_date(test_list, "decreasing")
    assert sorted_list_decreasing == [
        {"id": 1, "date": "2022-01-01"},
        {"id": 2, "date": "2022-02-15"},
        {"id": 3, "date": "2022-03-10"},
    ]
