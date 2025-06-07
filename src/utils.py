import json
from typing import Any

operations_file = "../data/operations.json"


def fin_operations(operations_file: str) -> list[Any]:
    """
    Считывает JSON-файл и возвращает список словарей с транзакциями.
    Если файл отсутствует, пуст, или не содержит список — возвращает пустой список.
    """
    try:
        with open(operations_file, encoding="utf-8") as json_file:
            operations_list = json.load(json_file)
            if isinstance(operations_list, list):
                return operations_list
            return []
    except (OSError, IOError):
        return []
