from src.decorators import log
import pytest
import os

@log("log.txt")
def complex_function(x: float, y: float) -> float:
    return x * y

@log()
def simple_function(a: int, b: int) -> int:
    return a + b


def test_simple_function(capsys):
    result = simple_function(2, 3)
    captured = capsys.readouterr()
    assert result == 5

    """Проверяем, что в логах есть нужные строки"""
    assert "Начало выполнения функции simple_function" in captured.err
    assert "Функция simple_function выполнена успешно. Результат 5" in captured.err
    assert "Результат 5" in captured.err


def test_complex_function():
    result = complex_function(2.5, 3.5)
    assert result == 8.75
    assert os.path.exists("log.txt")
    with open("log.txt", "r") as file:
        log_content = file.read()
        assert "Начало выполнения функции complex_function" in log_content
        assert "Функция complex_function выполнена успешно. Результат 8.75" in log_content
    os.remove("log.txt") # Очищаем файл после теста
