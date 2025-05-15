from src.masks import get_mask_account, get_mask_card_number

# импортируем функции


# создаем функцию, принимающую название и номер карты или счета и маскирующую цифры
def mask_account_card(number_card: str) -> str:
    # узнаем счет или карта и показываем только последние 4 цифры счета или первые 6 и последние 4 цифры карты
    if "Счет" in number_card:
        number_score = "Счет" + " " + get_mask_account(number_card.split()[-1])
    else:
        split_string = number_card.split()
        for name in split_string:
            if name.isalpha():
                name_card = " ".join(split_string[:2])
                card_number = split_string[-1]
            else:
                name_card = " ".join(split_string[:-1])
                card_number = split_string[-1]
        masked_number = get_mask_card_number(card_number)
        number_score = name_card + " " + masked_number

    return number_score


# получаем дату и преобразуем в читаемый формат

def get_date(date_input: str) -> str:
    year = date_input[:4]
    month = date_input[5:7]
    day = date_input[8:10]
    return f"{day}.{month}.{year}"
