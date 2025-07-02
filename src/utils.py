import json
import logging
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    r"C:\\Users\\Olga\\PycharmProjects\\project\\logs\\utils.log", mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

operations_file = "../data/operations.json"


def fin_operations(operations_file: str) -> list[Any]:
    """
    Считывает JSON-файл и возвращает список словарей с транзакциями.
    Если файл отсутствует, пуст, или не содержит список — возвращает пустой список.
    """
    try:
        logger.info(f"выполняем запрос в JSON файл{operations_file}")
        with open(operations_file, encoding="utf-8") as json_file:
            operations_list = json.load(json_file)
            logger.info(f"Проверяем получение списка из JSON файла{operations_file}")
            print(operations_list)
            if isinstance(operations_list, list):
                return operations_list
            return []
    except (OSError, IOError) as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []


if __name__ == "__main__":
    result = fin_operations(operations_file)
    print(result)
