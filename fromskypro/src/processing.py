def filter_by_state(list_: list, state_status: str = "executed") -> list:
    """
    Функция фильтрует список по указанному значению state
    """
    filtered_list = []
    for dict_ in list_:
        if dict_["state"] == state_status.upper():
            filtered_list.append(dict_)
    return filtered_list


def sort_by_date(list_: list, time: str = "increasing") -> list:
    """Сортировка списка по дате"""
    sorted_list = []
    if time == "increasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"], reverse=True)
    elif time == "decreasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"])
    return sorted_list
