from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account():
    assert get_mask_account("736541o8430135874305") == "Неверно введен номер"


def test_get_mask_account():
    assert get_mask_account("736541084301358743") == "Неверно введен номер"


def test_get_mask_card_number():
    assert get_mask_card_number("700o7922896o6361") == "Неверно введен номер"


def test_get_mask_card_number():
    assert get_mask_card_number("700079228960636") == "Неверно введен номер"


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"