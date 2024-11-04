import pandas as pd
import pytest


@pytest.fixture
def transaction_list():
    return [{'MCC': '',
  'Бонусы (включая кэшбэк)': 0,
  'Валюта операции': 'RUB',
  'Валюта платежа': 'RUB',
  'Дата операции': '28.10.2024 18:25:42',
  'Дата платежа': '28.10.2024',
  'Категория': 'Переводы',
  'Кэшбэк': '',
  'Номер карты': '',
  'Округление на инвесткопилку': 0,
  'Описание': 'Перевод между счетами',
  'Статус': 'OK',
  'Сумма операции': -50000.0,
  'Сумма операции с округлением': -50000.0,
  'Сумма платежа': -50000.0},
 {'MCC': '5814',
  'Бонусы (включая кэшбэк)': 0,
  'Валюта операции': 'RUB',
  'Валюта платежа': 'RUB',
  'Дата операции': '28.10.2024 18:25:41',
  'Дата платежа': '28.10.2024',
  'Категория': 'Пополнения',
  'Кэшбэк': '',
  'Номер карты': '*9916',
  'Округление на инвесткопилку': 0,
  'Описание': 'Пополнение. Премия',
  'Статус': 'OK',
  'Сумма операции': 16968.0,
  'Сумма операции с округлением': 16968.0,
  'Сумма платежа': 16968.0},
 {'MCC': '5411',
  'Бонусы (включая кэшбэк)': 0,
  'Валюта операции': 'RUB',
  'Валюта платежа': 'RUB',
  'Дата операции': '28.10.2024 18:24:55',
  'Дата платежа': '28.10.2024',
  'Категория': 'Супермаркеты',
  'Кэшбэк': '',
  'Номер карты': '*4529',
  'Округление на инвесткопилку': 0,
  'Описание': 'Людмила П.',
  'Статус': 'OK',
  'Сумма операции': -2450.0,
  'Сумма операции с округлением': -2450.0,
  'Сумма платежа': -2450.0}]


@pytest.fixture
def sample_df():
    return pd.DataFrame(
    {
        "Дата операции": ["28.10.2024 18:25:42",
                          "28.10.2024 18:25:41",
                          "28.10.2024 18:24:55"],
        "Дата платежа": ["28.10.2024",
                         "28.10.2024",
                         "28.10.2024"],
        "Номер карты": ["", "*9916", "*4529"],
        "Статус": ["OK", "OK", "OK"],
        "Сумма операции": [-50000.00, 16968.00, -2450.00],
        "Валюта операции": ["RUB", "RUB", "RUB"],
        "Сумма платежа": [-50000.00, 16968.00, -2450.00],
        "Валюта платежа": ["RUB", "RUB", "RUB"],
        "Кэшбэк": ["", "", ""],
        "Категория": ["Переводы", "Пополнения", "Супермаркеты"],
        "MCC": ["", "5814", "5411"],
        "Описание": ["Перевод между счетами", "Пополнение. Премия", "Людмила П."],
        "Бонусы (включая кэшбэк)": [0, 0, 0],
        "Округление на инвесткопилку": [0, 0, 0],
        "Сумма операции с округлением": [-50000.00, 16968.00, -2450.00]
    }
)