from typing import Dict, List
import pandas as pd


def read_transactions_csv(file_path: str) -> List[Dict]:
    """
    Читает транзакции из CSV файла.

    Args:
        file_path: Путь к CSV файлу.

    Returns:
        Список словарей, где каждый словарь представляет транзакцию.
    """
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path, encoding="utf-8")
        return df.to_dict(orient="records")
    else:
        print("Неверный формат файла. Поддерживаются только CSV файлы.")
        return []


def read_transactions_xlsx(file_path: str) -> List[Dict]:
    """
    Читает транзакции из XLSX файла.

    Args:
        file_path: Путь к XLSX файлу.

    Returns:
        Список словарей, где каждый словарь представляет транзакцию.
    """
    if file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    else:
        print("Неверный формат файла. Поддерживаются только XLSX файлы.")
        return []


