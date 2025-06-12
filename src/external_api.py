import os
from typing import Dict, List, Optional

import requests
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')

"""Создаем запрос по внешнему API на сайт для получения актуальной информации по курсу валют"""


def get_exchange_rate(from_currency: str, to_currency: str, amount: float) -> Optional[float]:
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"api_key": "API_KEY"}
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        try:
            return float(response.json()["result"])
        except (KeyError, ValueError):
            return None
    return None


"""Создаем функцию, которая принимает на вход транзакцию и возвращает сумму"""


def amount_sum(transactions: List[Dict]) -> float:
    total = 0.0
    for transaction in transactions:
        '''Получаем сумму и валюту'''
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            total += float(amount)
        else:
            '''Получаем курс валюты'''
            response = requests.get(
                f"https://api.apilayer.com/currency_data/convert?"
                f"to=RUB&from={currency}&amount={amount}"
            )
            data = response.json()
            total += data["result"]

    return total
