import datetime
import functools
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """
    Записывает в файл и выводит в консоль результат выполнения декорируемой функции
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(args: Any, kwargs: Any) -> Any:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(args, kwargs)
                logmessage = f"{timestamp} {func.__name__} ok"
            except Exception as e:
                result = None
                logmessage = f"{timestamp} {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, "a") as f:
                    f.write(logmessage + "\n")
            else:
                print(logmessage)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def homework_function(x: int, y: int) -> int:
    return x + y


homework_function(1, 2)
