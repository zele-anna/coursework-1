import json
import os
from datetime import datetime

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()


def greeting(date: str) -> str:
    """"Функция возвращает приветствие в зависимости от текущего времени суток."""
    date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    result = dict()
    if date_obj.hour <= 4:
        result["greeting"] = "Доброй ночи"
    elif date_obj.hour <= 11:
        result["greeting"] = "Доброе утро"
    elif date_obj.hour <= 17:
        result["greeting"] = "Добрый день"
    else:
        result["greeting"] = "Добрый вечер"
    return json.dumps(result, indent=4, ensure_ascii=False)


def read_excel(path: str) -> list | None:
    """Чтение эксель-файла с данными о транзакциях, возвращает список словарей с данными о транзакциях."""
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return print("Файл не найден.")


def get_sum_by_card(transactions: list | None) -> str:
    """Принимает на вход список транзакций и возвращает информацию о каждой карте:
- последние 4 цифры карты;
- общая сумма расходов;
- кешбэк (1 рубль на каждые 100 рублей)."""
    df = pd.DataFrame(transactions)
    grouped_df = df.groupby("Номер карты").agg({"Сумма операции": "sum",
                                                "Кэшбэк": "sum"})
    cards_dict = grouped_df.to_dict(orient="index")
    info = list()
    for key, value in cards_dict.items():
        item_to_add = dict()
        item_to_add["last_digits"] = str(key)[-4:]
        item_to_add["total_spent"] = round(value["Сумма операции"], 2)
        item_to_add["cashback"] = value["Кэшбэк"]
        info.append(item_to_add)
    return json.dumps(info, indent=4, ensure_ascii=False)


def get_top_five(transactions: list | None) -> str:
    """Функция принимает на вход список словарей с данными о транзакциях
    и возвращает топ-5 операций по сумме платежа."""
    df = pd.DataFrame(transactions)
    sorted_df = df.sort_values("Сумма операции", axis=0, ascending=False, kind='quicksort', na_position='last')
    top_five_dict = sorted_df.head().to_dict(orient="records")
    result = list()
    for item in top_five_dict:
        item_to_add = dict()
        date = datetime.strptime(item["Дата операции"], "%d.%m.%Y %H:%M:%S")
        item_to_add["date"] = date.strftime("%d.%m.%Y")
        item_to_add["amount"] = item["Сумма операции"]
        item_to_add["category"] = item["Категория"]
        item_to_add["description"] = item["Описание"]
        result.append(item_to_add)
    return json.dumps(result, indent=4, ensure_ascii=False)


def get_exchange_rate(currency_list: list) -> str:
    """Получение курсов валют через API https://www.cbr-xml-daily.ru/."""
    url_cbr = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url_cbr)
    if response.status_code == 200:
        result = response.json()
        currency_rates = list()
        for item in currency_list:
            rates = dict()
            rates["currency"] = item
            rates["rate"] = round(1/result["rates"][item], 2)
            currency_rates.append(rates)
    else:
        raise Exception(f"Ошибка получения данных, код {response.status_code}")
    return json.dumps(currency_rates, indent=4, ensure_ascii=False)


def get_stocks_rate(ticker: list) -> str:
    """Получение котировок акций через API https://marketstack.com/documentation."""
    access_key = os.getenv("ACCESS_KEY")
    base_url = "http://api.marketstack.com/v1/"
    url_marketstack = f"{base_url}eod?access_key={access_key}"
    stock_prices = list()
    for stock in ticker:
        stock_to_add = dict()
        querystring = {"symbols": stock}
        response = requests.get(url_marketstack, params=querystring)
        if response.status_code == 200:
            result = response.json()
            stock_to_add["stock"] = stock
            stock_to_add["price"] = result["data"][0]["close"]
            stock_prices.append(stock_to_add)
        else:
            raise Exception(f"Ошибка получения данных, код {response.status_code}")
    return json.dumps(stock_prices, indent=4, ensure_ascii=False)
