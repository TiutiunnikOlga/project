# маскируем номер карты введенной клиентом, передавая на вывод первые 6 цифр и последние 4 цифр


def get_mask_card_number(number_card: str) -> str:
    masced_number = number_card[:6] + "*" * 6 + number_card[12:]

    return " ".join([masced_number[i: i + 4] for i in range(0, len(masced_number), 4)])




# маскируем номер карты, передавая на вывод последние 4 цифры


def get_mask_account(number_card: str) -> str:
    masced_account = "*" * 2 + number_card[-4:]

    return masced_account

