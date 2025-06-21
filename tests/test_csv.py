import pytest
from unittest.mock import patch, mock_open

# Функция для тестирования (предполагается, что она находится в модуле transactions)
from src.csv import read_transactions

# Создаем тестовые данные
TEST_CSV_DATA = """id;state;date;amount;currency_name;currency_code;from;to;description
1;SUCCESS;2023-01-01;1000;RUB;643;user1;user2;Оплата товара
2;PENDING;2023-01-02;500;USD;840;user3;user4;Перевод другу"""


# Тест на успешное чтение файла
def test_read_transactions_success():
    # Создаем mock файла
    with patch("builtins.open", mock_open(read_data=TEST_CSV_DATA)) as mock_file:
        transactions = read_transactions()

    # Проверяем, что файл открыт правильно
    mock_file.assert_called_once_with("../data/transactions.csv")

    # Проверяем структуру данных
    assert len(transactions) == 2


# Тест на отсутствие файла
def test_read_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_transactions()


# Тест на некорректный формат CSV
def test_read_transactions_invalid_csv():
    with patch("builtins.open", mock_open(read_data="id;state\n1;SUCCESS\n2;PENDING")):
        with pytest.raises(Exception):
            read_transactions()


# Тест на пустые данные
def test_read_transactions_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        transactions = read_transactions()
        assert transactions == []


# Тест на проверку разделителя
def test_read_transactions_wrong_delimiter():
    wrong_delimiter_data = TEST_CSV_DATA.replace(";", ",")
    with patch("builtins.open", mock_open(read_data=wrong_delimiter_data)):
        with pytest.raises(Exception):
            read_transactions()
