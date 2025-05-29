from typing import Iterator

"""Функция генерирует номер карты от заданного числа до заданного числа"""


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Проверяем корректность входных данных"""
    if not (1 <= start <= 9999999999999999):
        raise ValueError("Начальное значение должно быть от 1 до 9999999999999999")
    if not (1 <= end <= 9999999999999999):
        raise ValueError("Конечние значение должно быть от 1 до 9999999999999999")
    if start > end:
        raise ValueError("Начальное значение должно быть меньше или равно конечному")

    """Генерируем номера карт"""
    for number in range(start, end + 1):
        """Форматируем число в нужный формат"""
        formatted_number = f"{number:016d}"
        card_number = " ".join(formatted_number[i: i + 4] for i in range(0, 16, 4))
        yield card_number


"""Функция принимает на вход список транзакций и возвращает значения по наименованию описания"""


def transaction_descriptions(transactions: list[dict], descriptions: str) -> Iterator[str]:
    """Проверяем наличие ключа в каждой транзакции"""
    for i, transaction in enumerate(transactions):
        if i >= 5:
            break

        if descriptions in transaction:
            yield transaction[descriptions]
        else:
            yield "Нет описания операции"


# Функция принимает на вход словари с транзакциями и выдает список отсортированный по валюте
def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:

    for transaction in transactions:
        try:
            # Проверяем наличие всех необходимых ключей
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            raise ValueError("Транзакция не содержит ключ 'currency'")
        except TypeError:
            raise ValueError("Некорректная структура данных транзакции")
