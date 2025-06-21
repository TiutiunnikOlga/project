from unittest.mock import patch
from src.external_api import amount_sum


"""Тестируем функцию ammount_summ"""


@patch("requests.get")
def test_amount_summ(mock_get):
    mock_get.return_value.json.return_value = {"result": 678233.551389}
    """Создаем тестовые значения для проверки"""
    transactions = [{"id": 41428829, "operationAmount": {"amount": "8221.37", "currency": {"code": "USD"}}}]

    result = amount_sum(transactions)
    assert result == 678233.551389
    """Проверяем вызов API"""
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/currency_data/convert?to=RUB&from=USD&amount=8221.37"
    )
