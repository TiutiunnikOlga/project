import unittest

from src.collections_utils import count_bank_search, process_bank_search


class TestBankSearch(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.transactions = [
            {"id": 1, "description": "Оплата в магазине Пятерочка"},
            {"id": 2, "description": "Перевод другу"},
            {"id": 3, "description": "Оплата в магазине Перекресток"},
            {"id": 4, "description": "Оплата ЖКХ"},
            {"id": 5, "description": "Перевод коллеге"},
        ]

    def test_process_bank_search(self):
        # Тестирование поиска по части описания
        result = process_bank_search(self.transactions, "оплата")
        self.assertEqual(len(result), 3)
        self.assertIn("Оплата в магазине Пятерочка", [t["description"] for t in result])
        self.assertIn("Оплата в магазине Перекресток", [t["description"] for t in result])
        self.assertIn("Оплата ЖКХ", [t["description"] for t in result])

        # Тестирование поиска с учетом регистра
        result = process_bank_search(self.transactions, "перевод")
        self.assertEqual(len(result), 2)
        self.assertIn("Перевод другу", [t["description"] for t in result])
        self.assertIn("Перевод коллеге", [t["description"] for t in result])

    def test_empty_search_term(self):
        # Тестирование с пустым поисковым запросом
        result = process_bank_search(self.transactions, "")
        self.assertEqual(len(result), len(self.transactions))

    def test_non_existing_term(self):
        # Тестирование с несуществующим запросом
        result = process_bank_search(self.transactions, "не_существует")
        self.assertEqual(len(result), 0)

    def test_count_with_non_existing_descriptions(self):
        # Тестирование подсчета с несуществующими категориями
        descriptions = ["Оплата", "Перевод", "Не_существует"]
        result = count_bank_search(self.transactions, descriptions)
        self.assertEqual(result["Не_существует"], 0)


if __name__ == "__main__":
    unittest.main()
