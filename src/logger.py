import logging
from typing import Any


def setup_logging() -> Any:
    """Настраивает логирование."""
    logger = logging.getLogger(__name__)  # Используем __name__ для получения имени модуля
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(ASCtime)s - %(name)s - %(level_name)s - %(message)s")

    # Исправленное имя файла
    file_handler = logging.FileHandler("app.log", mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
