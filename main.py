from src.csv_utils import load_excel_data, read_transactions
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import fin_operations

# Программа здоровается и предлагает на выбор формат файла откуда брать информацию
print('''
Программа: Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
''')
input_name_of_transaction = int(input())


if input_name_of_transaction == 1:
    print("Для обработки выбран JSON-файл")
    # Выбираем статус операции из предложенных
    print("""
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    """)
    while True:
        # Когда статус введен из предложенных, приступаем к фильтрации
        status = str(input().upper())
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status}"')
            # Считываем файл
            data_list = fin_operations(r"C:\Users\Olga\PycharmProjects\project\data\operations.json")
            result = filter_by_state(data_list, status)
            # Если отбор не выдает ни одной транзакции, сообщаем
            if not result:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            else:
                # Если список транзакций не пустой, предлагаем фильтрацию по дате
                print("Отсортировать операции по дате? Да / Нет")
                sort_ask = str(input().lower())
                if sort_ask == "да":
                    print("Отсортировать по возрастанию или по убыванию?")
                    # Предлагаем фильтрацию по возрастанию или убыванию даты
                    ascending_ask = str(input().lower())
                    if ascending_ask == "по возрастанию":
                        sorted_result = sort_by_date(result, reverse=False)
                    else:
                        sorted_result = sort_by_date(result)
                    # Предлагаем сортировку по транзакциям в РУБ
                    print("Выводить только рублевые транзакции? Да/Нет")
                    ask_rub = str(input().lower())
                    if ask_rub == "да":
                        result = list(filter_by_currency(result, "RUB"))
                        if not result:
                            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

                    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                    # Предлагаем отсорировать транзакции включающие определенное слово из описания
                    ans_filtered = input().lower()
                    if ans_filtered == "да":
                        word_filtered = str(input("Введите слово:").lower())
                        filtered_descriptions = transaction_descriptions(result, word_filtered)
                        print(filtered_descriptions)
                        # Проверяем есть ли транзакции в списке, если да, выдаем список, если нет, ошибку
                        if not filtered_descriptions:
                            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        for description in filtered_descriptions:
                            print(description)
                    else:
                        sorted_of_word = sorted_result
                        if not sorted_of_word:
                            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        else:
                            print(sorted_of_word)
                else:
                    sorted_result = result
                    if not sorted_result:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                    else:
                        print(sorted_result)
            break
        else:
            print("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")


elif input_name_of_transaction == 2:
    print("Для обработки выбран CSV-файл")
    print("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
    while True:
        status = str(input().upper())
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            # Когда статус введен из предложенных, приступаем к фильтрации
            print(f'Операции отфильтрованы по статусу "{status}"')
            # Считываем файл
            data_list = read_transactions()
            result = filter_by_state(data_list, status)
            # Предлагаем фильтрацию по дате
            print("Отсортировать операции по дате? Да / Нет")
            sort_ask = str(input().lower())
            if sort_ask == "да":
                # Предлагаем фильтрацию по возрастанию или убыванию даты
                print("Отсортировать по возрастанию или по убыванию?")
                ascending_ask = str(input().lower())
                if ascending_ask == "по возрастанию":
                    sorted_result = sort_by_date(result, reverse=False)
                else:
                    sorted_result = sort_by_date(result)
                # Предлагаем сортировку по транзакциям в РУБ
                print("Выводить только рублевые транзакции? Да/Нет")
                ask_rub = str(input().lower())
                if ask_rub == "да":
                    result = list(filter_by_currency(result, "RUB"))
                    if not result:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                # Предлагаем отсорировать транзакции включающие определенное слово из описания
                print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                ans_filtered = input().lower()
                if ans_filtered == "да":
                    word_filtered = str(input("Введите слово:").lower())
                    filtered_descriptions = list(transaction_descriptions(result, word_filtered))
                    # Проверяем есть ли транзакции в списке, если да, выдаем список, если нет, ошибку
                    if not filtered_descriptions:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                    for description in filtered_descriptions:
                        print(description)
                else:
                    sorted_of_word = sorted_result
                    if not sorted_of_word:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                    else:
                        print(sorted_of_word)
            else:
                sorted_result = result
                if not sorted_result:
                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                else:
                    print(sorted_result)
            break
        else:
            print("""
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    """)

else:
    print("Для обработки выбран XLSX-файл")
    print("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
    while True:
        status = str(input().upper())
        # Выбираем статус операции из предложенных
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status}"')
            # Когда статус введен из предложенных, приступаем к фильтрации
            data_list = load_excel_data("C:\\Users\\Olga\\PycharmProjects\\project\\data\\transactions_excel.xlsx")
            # Считываем файл
            result = filter_by_state(data_list, status)
            print("Отсортировать операции по дате? Да / Нет")
            sort_ask = str(input().lower())
            if sort_ask == "да":
                # Предлагаем фильтрацию по возрастанию или убыванию даты
                print("Отсортировать по возрастанию или по убыванию?")
                ascending_ask = str(input().lower())
                if ascending_ask == "по возрастанию":
                    sorted_result = sort_by_date(result, reverse=False)
                else:
                    sorted_result = sort_by_date(result)
                # Предлагаем сортировку по транзакциям в РУБ
                print("Выводить только рублевые транзакции? Да/Нет")
                ask_rub = str(input().lower())
                if ask_rub == "да":
                    result = list(filter_by_currency(result, "RUB"))
                    if not result:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                # Предлагаем отсорировать транзакции включающие определенное слово из описания
                print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                ans_filtered = input().lower()
                if ans_filtered == "да":
                    word_filtered = str(input("Введите слово:").lower())
                    filtered_descriptions = list(transaction_descriptions(result, word_filtered))
                    # Проверяем есть ли транзакции в списке, если да, выдаем список, если нет, ошибку
                    if not filtered_descriptions:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                    for description in filtered_descriptions:
                        print(description)
                else:
                    sorted_of_word = sorted_result
                    if not sorted_of_word:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                    else:
                        print(sorted_of_word)
            else:
                sorted_result = result
                if not sorted_result:
                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                else:
                    print(sorted_result)
            break
        else:
            print("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
""")
if __name__ == "__main__":
    print()
