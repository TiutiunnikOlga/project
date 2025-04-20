from masks import get_mask_account, get_mask_card_number
from masks import number_card

# импортируем функции


# создаем функцию, принимающую название и номер карты или счета и маскирующую цифры
def mask_account_card(number_card: str):
    # узнаем счет или карта и показываем только последние 4 цифры счета или первые 6 и последние 4 цифры карты
    if "Счет" in number_card:
        number_score = "Счет" + "  " + "*" * 2 + number_card[-4:]
    else:
        split_string = number_card.split()
        for name in split_string:
            if name.isalpha():
                name_card = " ".join(split_string[:2])
            else:
                name_card = " ".join(split_string[:1])
        masced_number = split_string[-1][:6] + "*" * 6 + split_string[-1][12:]
        number_score = name_card + " " + masced_number

    return number_score


print(mask_account_card(number_card))
