from unittest.mock import patch

import pytest

from src.utils import get_exchange_rate, get_stocks_rate, get_sum_by_card, get_top_five, greeting, read_excel


def test_greeting():
    assert greeting("2024-11-03 04:10:00") == '{\n    "greeting": "Доброй ночи"\n}'
    assert greeting("2024-11-03 11:10:00") == '{\n    "greeting": "Доброе утро"\n}'
    assert greeting("2024-11-03 12:10:00") == '{\n    "greeting": "Добрый день"\n}'
    assert greeting("2024-11-03 18:10:00") == '{\n    "greeting": "Добрый вечер"\n}'


@patch("src.utils.pd.read_excel")
def test_read_excel(mock_reader, sample_df, transaction_list) -> None:
    """Тест на чтение файла csv."""
    mock_reader.return_value = sample_df
    assert read_excel("test.scv") == transaction_list


def test_get_sum_by_card(transaction_list):
    assert get_sum_by_card(transaction_list) == ('[\n'
 '    {\n'
 '        "last_digits": "",\n'
 '        "total_spent": -50000.0,\n'
 '        "cashback": ""\n'
 '    },\n'
 '    {\n'
 '        "last_digits": "4529",\n'
 '        "total_spent": -2450.0,\n'
 '        "cashback": ""\n'
 '    },\n'
 '    {\n'
 '        "last_digits": "9916",\n'
 '        "total_spent": 16968.0,\n'
 '        "cashback": ""\n'
 '    }\n'
 ']')


def test_get_top_five(transaction_list):
    assert get_top_five(transaction_list) == ('[\n'
 '    {\n'
 '        "date": "28.10.2024",\n'
 '        "amount": 16968.0,\n'
 '        "category": "Пополнения",\n'
 '        "description": "Пополнение. Премия"\n'
 '    },\n'
 '    {\n'
 '        "date": "28.10.2024",\n'
 '        "amount": -2450.0,\n'
 '        "category": "Супермаркеты",\n'
 '        "description": "Людмила П."\n'
 '    },\n'
 '    {\n'
 '        "date": "28.10.2024",\n'
 '        "amount": -50000.0,\n'
 '        "category": "Переводы",\n'
 '        "description": "Перевод между счетами"\n'
 '    }\n'
 ']')


@patch("requests.get")
def test_get_exchange_rate(mock_get) -> None:
    """Проверка вывода суммы в рублях по долларовой транзакции"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'disclaimer': 'https://www.cbr-xml-daily.ru/#terms',
                                               'date': '2024-11-03', 'timestamp': 1730581200,
                                               'base': 'RUB',
                                               'rates':
                                                   {'USD': 0.01025116,
                                                    'EUR': 0.00942128797}}
    assert get_exchange_rate(["USD", "EUR"]) == ('[\n'
 '    {\n'
 '        "currency": "USD",\n'
 '        "rate": 97.55\n'
 '    },\n'
 '    {\n'
 '        "currency": "EUR",\n'
 '        "rate": 106.14\n'
 '    }\n'
 ']')


@patch("requests.get")
def test_get_stocks_rate(mock_get) -> None:
    """Проверка вывода суммы в рублях по долларовой транзакции"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'pagination':
                                                   {'limit': 100, 'offset': 0, 'count': 100, 'total': 250},
                                               'data':
                                                   [{'open': 220.97,
                                                     'high': 225.35,
                                                     'low': 220.27,
                                                     'close': 222.91,
                                                     'volume': 65242200.0,
                                                     'symbol': 'AAPL',
                                                     'exchange': 'XNAS',
                                                     'date': '2024-11-01T00:00:00+0000'}]}
    assert get_stocks_rate(["AAPL"]) == ('[\n'
 '    {\n'
 '        "stock": "AAPL",\n'
 '        "price": 222.91\n'
 '    }\n'
 ']')
