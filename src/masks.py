# маскируем номер карты введенной клиентом, передавая на вывод первые 6 цифр и последние 4 цифры

number_card = str(input("Введите номер карты"))


def get_mask_card_number(number_card):
    masced_number = number_card[:6] + "*" * 6 + number_card[12:]

    return " ".join([masced_number[i : i + 4] for i in range(0, len(masced_number), 4)])


print(get_mask_card_number(number_card))


# маскируем номер карты, передавая на вывод последние 4 цифры

number_card = str(input("Введите номер карты"))


def get_mask_account(number_card):
    masced_account = "*" * 2 + number_card[-4:]

    return masced_account


print(get_mask_account(number_card))
