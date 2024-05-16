from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None, mode: str = "a") -> Callable:
    """Записывает в файл/ выводит в консоль результат выполнения декорируемой функции"""

    def dec(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            try:
                func(*args, **kwargs)
                result = f"{func.__name__} ok"
            except Exception as e:
                result = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
            if filename:
                with open(filename, mode) as f:
                    f.write(result + "\n")
            else:
                print(result)
            return result

        return wrapper

    return dec
