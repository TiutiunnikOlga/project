import csv
import logging
from typing import List

import pandas as pd


def load_excel_data(file_path: str) -> list:
    try:
        logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", encoding="utf-8", level=logging.INFO)

        logging.info("Чтение файла")
        df = pd.read_excel(file_path, engine="openpyxl")

        # Преобразуем DataFrame в список словарей
        data_list = df.to_dict(orient="records")

        logging.info(f"Размер данных: {len(data_list)}")
        logging.info("Первые 5 записей:")
        logging.info(data_list[:5])

        return data_list

    except FileNotFoundError:
        logging.error("Файл не найден")
        raise

    except pd.errors.EmptyDataError:
        logging.error("Файл пуст")
        raise

    except Exception as e:
        logging.error(f"Ошибка при чтении файла: {str(e)}")
        raise


"""Пример использования"""
if __name__ == "__main__":
    try:
        df = load_excel_data(r"C:\Users\Olga\PycharmProjects\project\data\transactions_excel.xlsx")
        print(df)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

logger = logging.getLogger("csv")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r"C:\Users\Olga\PycharmProjects\project\logs\csv.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


"""Создаем функцию для чтения файла csv"""


def read_transactions() -> List[dict]:
    try:
        """Считываем в файл"""
        transaction_list = []
        logger.info("Читаем файл транзакций: ../data/transactions.csv")

        with open(
            r"C:\Users\Olga\PycharmProjects\project\data\transactions.csv", encoding="utf-8"
        ) as file_transactions:
            reader = csv.DictReader(file_transactions, delimiter=";")

            """Задаем ключевые параметры"""
            for row in reader:
                my_dict = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "amount": row["amount"],
                    "currency_name": row["currency_name"],
                    "currency_code": row["currency_code"],
                    "from": row["from"],
                    "to": row["to"],
                    "description": row["description"],
                }
                transaction_list.append(my_dict)

            logger.info(f"Успешно прочитано {len(transaction_list)} транзакций")

        return transaction_list
    # Проверяем на ошибки
    except Exception as e:
        logger.error(f"Ошибка при чтении файла транзакций: {str(e)}")
        raise


if __name__ == "__main__":
    print(read_transactions)
