from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
import pytest
from typing import List, Dict, Any, Iterator

# Исходный список транзакций для тестов
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"}
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"}
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
]


# Тестовый набор для filter_by_currency
@pytest.mark.parametrize(
    "transactions, currency, expected",
    [
        (transactions, "USD", [transactions[0], transactions[1], transactions[3]]),
        ([], "USD", []),  # Тест на пустой список
        (transactions, "", [])  # Тест на пустую строку валюты
    ]
)
def test_filter_by_currency(transactions: List[any], currency: str, expected: List[any]):
    # Получаем результат работы функции
    result = list(filter_by_currency(transactions, currency))

    # Проверяем, что результат совпадает с ожидаемым
    assert result == expected

@pytest.fixture
def transactions():
    # Создаем фиктивные данные для транзакций
    return [
        {'description': 'Перевод организации'},
        {'description': 'Перевод со счета на счет'},
        {'description': 'Перевод со счета на счет'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Перевод организации'}]
@pytest.fixture
def descriptions():
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]


def test_transaction_descriptions(transactions, descriptions):
    # Получаем генератор описаний
    result = transaction_descriptions(transactions, 'description')

    # Проверяем каждое описание
    for i, expected in enumerate(descriptions):
        try:
            assert next(result) == expected, f"Ошибка в описании для транзакции {i}"
        except StopIteration:
            pytest.fail(f"Недостаточно элементов в генераторе для транзакции {i}")

    # Проверяем, что генератор исчерпан
    try:
        next(result)
        pytest.fail("Генератор должен быть исчерпан")
    except StopIteration:
        pass  # Это ожидаемое поведение

# Тестовый набор для card_number_generator
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1234567890123456, 1234567890123459,
         ["1234 5678 9012 3456", "1234 5678 9012 3457", "1234 5678 9012 3458", "1234 5678 9012 3459"]
         ),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        (1, 1, ["0000 0000 0000 0001"])
    ]
)
def test_card_number_generator(start: int, end: int, expected: List[str]):
    # Получаем результат
    result = list(card_number_generator(start, end))

    # Проверяем результат
    assert result == expected
