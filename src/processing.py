# Принимаем словари, на выходе получаем сортированный список по ключу state


def filter_by_state(data: list, state: str) -> list:
    return list(filter(lambda x: x.get("state", "") == state or x.get("state", "executed") == state, data))


# Принимаем словари, на выходе получаем отсортированный по дате список


def sort_by_date(transactions: list, reverse=True) -> list:
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
