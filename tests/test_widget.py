from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize("string, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 7365410843013587430565", "Счет Неверно введен номер"),
    ("Maestro 15968378687o5199", "Maestro Неверно введен номер"),
    ("Счет 646864736788947795", "Счет Неверно введен номер"),
    ("MasterCard 715830073472675890", "MasterCard Неверно введен номер"),
    ("Счет 3538303347444789556o", "Счет Неверно введен номер")
])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

