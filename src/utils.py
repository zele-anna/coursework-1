import pandas as pd
import requests
import json

from mypy.util import json_loads


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


def get_exchange_rate():
    url_moex = 'https://iss.moex.com/iss/statistics/engines/currency/markets/selt/rates.json?iss.meta=off'
    url_moex_2 = "http://iss.moex.com/iss/statistics/engines/futures/markets/indicativerates/securities/USD/RUB.json?from=2021-01-01&till=2021-02-25&iss.meta=off"
    response = requests.get(url_moex)
    if response.status_code == 200:
        result = response.json()
    else:
        raise Exception(f"Ошибка получения данных, код {response.status_code}")
    return json.dumps(result, indent=4)


def get_stocks_rate():
    API_KEY = "325ebeba71fc68618bd241a7bd9e2ed5"
    base_url = "http://api.marketstack.com/v1/"
    ticker = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    url_moex = f'https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticker}.json?iss.meta=off'
    # url_moex_2 = f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.xml?iss.meta=off&iss.only=securities&securities.columns={ticker},PREVLEGALCLOSEPRICE"
    mktstack_url = f"{base_url}tickers?access_key={API_KEY}"
    response = requests.get(mktstack_url)
    if response.status_code == 200:
        result = response.json()
        json_str = json.dumps(result, indent=4)
        data = json.loads(json_str)
        new_data = []
        for item in data["data"]:
            if item["symbol"] in ticker:
                new_data.append(item)
                print(item["symbol"])
    else:
        raise Exception(f"Ошибка получения данных, код {response.status_code}")

    return json.dumps(new_data, indent=4)

print(get_exchange_rate())