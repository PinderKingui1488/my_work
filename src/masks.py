from src.logger import setup_logging

# Создаем loger для модуля masks
logger = setup_logging()


def mask_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    if len(card_number) == 16:  # Проверяем длину номера карты
        masked_card = card_number[:4] + " " + card_number[4:6] + " ** " + card_number[-4:]
        logger.info("Функция mask_card выполнена успешно")  # Используем masks_logger
        return masked_card
    else:
        logger.error("С функцией mask_card что-то пошло не так")  # Используем masks_logger
        return "Некорректный номер карты"


def mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    if len(account_number) >= 4:  # Проверяем, что номер счета хотя бы 4 символа
        masked_account = account_number[-4:]
        logger.info("Функция mask_account выполнена успешно")  # Используем masks_logger
        return masked_account
    else:
        logger.error("С функцией mask_account что-то пошло не так")  # Используем masks_logger
        return "Некорректный номер счета"

# Пример использования функций
# mask_card("1234567890123456")
# mask_account("12345678901234567890123456789012")
