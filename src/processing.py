# Принимаем словари, на выходе получаем сортированный список по ключу state


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    return list(filter(lambda x: x.get("state") == state, data))


# Принимаем словари, на выходе получаем отсортированный по дате список


def sort_by_date(data: list, date_key: str = "date") -> list:
    return sorted(data, key=lambda x: x.get(date_key))
