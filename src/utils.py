import pandas as pd


def read_excel(path: str) -> list | None:
    """Чтение эксель-файла с данными о транзакциях, возвращает список словарей с данными о транзакциях."""
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return print("Файл не найден.")


def get_sum_by_card(transactions: list) -> dict:
    """Принимает на вход список транзакций и возвращает информацию о каждой карте:
- последние 4 цифры карты;
- общая сумма расходов;
- кешбэк (1 рубль на каждые 100 рублей)."""
    df = pd.DataFrame(transactions)
    grouped_df = df.groupby("Номер карты").agg({"Сумма операции": "sum",
                                                "Кэшбэк": "sum"})
    return grouped_df.to_dict(orient="index")


def get_top_five(transactions: list) -> list:
    """Функция принимает на вход список словарей с данными о транзакциях
    и возвращает топ-5 операций по сумме платежа."""
    df = pd.DataFrame(transactions)
    sorted_df = df.sort_values("Сумма операции", axis=0, ascending=False, kind='quicksort', na_position='last')
    return sorted_df.head().to_dict(orient="records")
