# Принимаем словари, на выходе получаем сортированный список по ключу state


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    return list(filter(lambda x: x.get("state") == state, data))


# Принимаем словари, на выходе получаем отсортированный по дате список


def sort_by_date(transactions: list) -> list:
    return sorted(transactions, key=lambda x: x["date"], reverse=True)
