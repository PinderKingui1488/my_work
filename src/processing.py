from typing import Dict, List


def filter_by_state(list_of_dicts: List[dict], state: str = "EXECUTED") -> List[dict]:

    return [item for item in list_of_dicts if item.get("state") == state]


def sort_by_date(list_: List[Dict], time: str = "increasing") -> List[Dict]:
    """Сортировка списка по дате"""
    sorted_list = []
    if time == "increasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"])
    elif time == "decreasing":
        sorted_list = sorted(list_, key=lambda dict_: dict_["date"], reverse=True)
    return sorted_list
