import unittest
import pandas as pd
from src.almost_exel_table import read_transactions_csv, read_transactions_xlsx


class TestReadTransactions(unittest.TestCase):

    def test_read_transactions_csv(self) -> None:
        # Подготовка тестовых данных
        test_data = {
            'date': ['2023-10-26', '2023-10-27'],
            'amount': [100.0, 200.0],
            'description': ['Покупка товаров', 'Оплата услуг'],
        }
        df = pd.DataFrame(test_data)
        df.to_csv('test_transactions.csv', index=False)

        # Проверка функции
        transactions = read_transactions_csv('test_transactions.csv')
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]['date'], '2023-10-26')
        self.assertEqual(transactions[1]['amount'], 200.0)

        # Очистка тестовых данных
        import os
        os.remove('test_transactions.csv')

    def test_read_transactions_xlsx(self) -> None:
        # Подготовка тестовых данных
        test_data = {
            'date': ['2023-10-26', '2023-10-27'],
            'amount': [100.0, 200.0],
            'description': ['Покупка товаров', 'Оплата услуг'],
        }
        df = pd.DataFrame(test_data)
        df.to_excel('test_transactions.xlsx', index=False)

        # Проверка функции
        transactions = read_transactions_xlsx('test_transactions.xlsx')
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]['date'], '2023-10-26')
        self.assertEqual(transactions[1]['amount'], 200.0)

        # Очистка тестовых данных
        import os
        os.remove('test_transactions.xlsx')

    def test_read_transactions_invalid_format(self) -> None:
        # Проверка для неверного формата файла
        transactions = read_transactions_csv('test_transactions.txt')  # Файл с неправильным расширением
        self.assertEqual(transactions, [])

        transactions = read_transactions_xlsx('test_transactions.txt')
        self.assertEqual(transactions, [])


if __name__ == '__main__':
    unittest.main()
