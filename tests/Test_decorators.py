import pytest
from typing import Optional, Callable, Any
from src.decorators import log


# Создаем простую функцию, которую будем декорировать
def simple_function(a, b):
    return a + b


# Создаем фикстуру для временного файла
@pytest.fixture
def tmp_file(tmp_path):
    return tmp_path / "log.txt"


# Параметризация для тестирования декоратора с выводом в файл и в консоль
@pytest.mark.parametrize("filename, mode", [
    ("test_log1.txt", "w"),
    ("test_log2.txt", "a")
])
def test_decorator_file_and_console(tmp_file, filename, mode):
    @log(filename=filename, mode=mode)
    def test_function(a, b):
        return a - b

    result = test_function(5, 2)

    with open(filename, "r") as f:
        content = f.read()

    assert result == "test_function ok"
    assert "test_function ok" in content


# Параметризация для тестирования декоратора с выводом в консоль
def test_decorator_console(capfd):
    @log()
    def test_function(a, b):
        raise ValueError("Some error")

    result = test_function(8, 3)

    out, _ = capfd.readouterr()

    assert result == "test_function error: ValueError. Inputs: (8, 3), {}"
    assert "test_function error: ValueError. Inputs: (8, 3), {}" in out
