import pandas as pd


def read_excel(path: str) -> list | None:
    """Чтение эксель-файла с данными о транзакциях, возвращает список словарей с данными о транзакциях."""
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return print("Файл не найден.")


# def get_sum_by_card(transactions: list) -> dict:
#     """Принимает на вход список транзакций и возвращает информацию о каждой карте:
# - последние 4 цифры карты;
# - общая сумма расходов;
# - кешбэк (1 рубль на каждые 100 рублей)."""
#     df = pd.DataFrame(transactions)
#     grouped_df = df.groupby("Номер карты").agg({"Сумма операции": "sum"})
#
#     dict_data = grouped_df.to_dict(orient="index")
#     print(dict_data)
#     result = dict()
#     sum_dict = dict()
#     cashback_dict = dict()

    # for key, value in dict_data.items():
    #     print(key, value)
    #     for keyword, val in value.items():
    #         if key == "Сумма операции":
    #             sum_dict[keyword] = {"Сумма операций": val}
    #         elif key == "Кэшбэк":
    #             cashback_dict[keyword] = {"Кэшбэк": val}


def get_sum_by_card(transactions: list) -> dict:
    """Принимает на вход список транзакций и возвращает информацию о каждой карте:
- последние 4 цифры карты;
- общая сумма расходов;
- кешбэк (1 рубль на каждые 100 рублей)."""
    df = pd.DataFrame(transactions)
    grouped_df = df.groupby("Номер карты").agg({"Сумма операции": "sum",
                                                "Кэшбэк": "sum"})

    return grouped_df.to_dict(orient="index")


transaction_list = read_excel("../data/my_operations.xlsx")
print(get_sum_by_card(transaction_list))