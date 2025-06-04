import logging
from functools import wraps
from logging.handlers import RotatingFileHandler
from typing import Any, Callable, ParamSpec, TypeVar, Union

"""Определяем типы для функций и их параметров"""
P = ParamSpec("P")
R = TypeVar("R")

"""Декоратор логирует начало и конец выполнения функции, регистрирует ошибки и результаты"""


def log(filename: str | None = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> R:
            """Создаем логи"""
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            """Форматируем логи"""
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

            """Объявляем handler как Union для обоих типов"""
            handler: Union[RotatingFileHandler, logging.StreamHandler]

            """Добавляем зависимости от filename"""
            if filename:
                handler = RotatingFileHandler(filename, maxBytes=1024 * 1024, backupCount=5)
            else:
                handler = logging.StreamHandler()

            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                logger.info(f"Начало выполнения функции {func.__name__}")
                result = func(*args, **kwargs)
                logger.info(f"Функция {func.__name__} выполнена успешно. Результат {result}")
                return result
            except Exception as e:
                logger.error(f"Ошибка в функции {func.__name__}: {type(e).__name__}: {str(e)}")
                logger.error(f"Входные параметры: {args}, {kwargs}")
                raise
            finally:
                logger.handlers.clear()

        return wrapper

    return decorator
