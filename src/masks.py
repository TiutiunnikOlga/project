import logging
import sys  # noqa

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# маскируем номер карты введенной клиентом, передавая на вывод первые 6 цифр и последние 4 цифр


def get_mask_card_number(number_card: str) -> str:
    logger.info(f'Проверяем {number_card} количество символов и являются ли они цифрами')
    if len(number_card) != 16 or not number_card.isdigit():
        logger.error(f'Введено неверное значение карты {number_card}')
        return "Неверно введен номер"

    logger.info(f'Скрываем номер карты {number_card}')
    masked_number = number_card[:6] + "*" * 6 + number_card[12:]

    return " ".join([masked_number[i : i + 4] for i in range(0, len(masked_number), 4)])  # noqa


# маскируем номер карты, передавая на вывод последние 4 цифры


def get_mask_account(number_card: str) -> str:
    logger.info(f'Проверяем {number_card} количество символов и являются ли они цифрами')
    if len(number_card) != 20 or not number_card.isdigit():
        logger.error(f'Неверно введен номер счета {number_card}')
        return "Неверно введен номер {number_card}"

    logger.info(f'Скрываем номер счета {number_card}')
    masked_account = "*" * 2 + number_card[-4:]

    return masked_account
