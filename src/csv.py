import csv
import logging

import pandas as pd
from typing import List, Dict




def load_excel_data(file_path: str) -> pd.DataFrame:
    try:
        """Инициализируем logger"""
        logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

        """Читаем файл"""
        logging.info(f"Чтение файла: {file_path}")
        df = pd.read_excel(file_path, engine="openpyxl")

        """Проверяем данные"""
        logging.info(f"Размер данных: {df.shape}")
        logging.info("Первые 5 строк:")
        logging.info(df.head())

        return df

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
        df = load_excel_data("../data/transactions_exel.xlsx")
        print(df.shape)
        print(df.head())
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

logger = logging.getLogger("csv")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/csv.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


"""Создаем функцию для чтения файла csv"""


def read_transactions()-> List[dict]:
    try:
        """Считываем в файл"""
        transaction_list = []
        logger.info("Читаем файл транзакций: ../data/transactions.csv")

        with open("../data/transactions.csv") as file_transactions:
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
