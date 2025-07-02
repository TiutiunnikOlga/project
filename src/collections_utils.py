import re
from collections import Counter

from src.csv_utils import read_transactions


def process_bank_search(transactions: list[dict], search_term: str) -> list[dict]:
    # Создаем регулярное выражение с учетом нечувствительности к регистру
    pattern = re.compile(rf".*{search_term}.*", re.IGNORECASE)

    # Фильтруем список операций, используя search
    result = [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]

    return result


def count_bank_search(transactions: list[dict], descriptions: list[str]) -> dict:
    # Создаем словарь с начальными значениями 0 для каждой категории
    result = Counter({desc: 0 for desc in descriptions})

    # Проходим по всем операциям
    for transaction in transactions:
        # Проверяем, есть ли описание операции в списке категорий
        if transaction.get("description") in descriptions:
            # Увеличиваем счетчик для соответствующей категории
            result[transaction["description"]] += 1
        else:
            # Добавляем новое описание в список и увеличиваем счетчик
            result[transaction["description"]] += 1

    return result


# Пример использования
if __name__ == "__main__":
    # Читаем транзакции из CSV
    transactions = read_transactions()

    # Пример поиска
    search_term = input("Введите строку для поиска: ")
    found_transactions = process_bank_search(transactions, search_term)

    # Выводим результаты
    for transaction in found_transactions:
        print(transaction)
    print(f"Найдено {len(found_transactions)} операций:")


if __name__ == "__main__":
    transactions = read_transactions()

    # Список возможных описаний транзакций
    descriptions = []

    result = count_bank_search(transactions, descriptions)

    for description, count in result.items():
        print(f"Описание: {description}, найдено: {count} транзакций")
