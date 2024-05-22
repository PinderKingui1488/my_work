from typing import Dict, List


def filter_by_state(list_: List[Dict], state_status: str = "executed") -> List[Dict]:
    """
    Функция фильтрует список по указанному значению state
    """
    filtered_list = []
    for dict_ in list_:
        if dict_["state"].upper() == state_status.upper():
            filtered_list.append(dict_)
    return filtered_list


def sort_by_date(list_: List[Dict], time: str = "increasing") -> List[Dict]:
    """Сортировка списка по дате"""
    sorted_list = []
    if time == "increasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"])
    elif time == "decreasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"], reverse=True)
    return sorted_list
