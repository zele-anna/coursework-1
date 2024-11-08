from unittest.mock import patch

from src.utils import get_exchange_rate, get_stocks_rate, get_sum_by_card, get_top_five, greeting, read_excel


def test_greeting():
    assert greeting("2024-11-03 04:10:00") == "Доброй ночи"
    assert greeting("2024-11-03 11:10:00") == "Доброе утро"
    assert greeting("2024-11-03 12:10:00") == "Добрый день"
    assert greeting("2024-11-03 18:10:00") == "Добрый вечер"


@patch("src.utils.pd.read_excel")
def test_read_excel(mock_reader, sample_df, transaction_list) -> None:
    """Тест на чтение файла csv."""
    mock_reader.return_value = sample_df
    assert read_excel("test.scv") == transaction_list


def test_get_sum_by_card(transaction_list):
    assert get_sum_by_card(transaction_list) == [{'cashback': '', 'last_digits': '', 'total_spent': -50000.0},
                                                 {'cashback': '', 'last_digits': '4529', 'total_spent': -2450.0},
                                                 {'cashback': '', 'last_digits': '9916', 'total_spent': 16968.0}]


def test_get_top_five(transaction_list):
    assert get_top_five(transaction_list) == [{'amount': 16968.0,
                                               'category': 'Пополнения',
                                               'date': '28.10.2024',
                                               'description': 'Пополнение. Премия'},
                                              {'amount': -2450.0,
                                               'category': 'Супермаркеты',
                                               'date': '28.10.2024',
                                               'description': 'Людмила П.'},
                                              {'amount': -50000.0,
                                               'category': 'Переводы',
                                               'date': '28.10.2024',
                                               'description': 'Перевод между счетами'}]


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
    assert get_exchange_rate(["USD", "EUR"]) == [{'currency': 'USD', 'rate': 97.55},
                                                 {'currency': 'EUR', 'rate': 106.14}]


@patch("requests.get")
def test_get_stocks_rate(mock_get) -> None:
    """Проверка вывода суммы в рублях по долларовой транзакции"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'pagination':
            {'limit': 100,
             'offset': 0,
             'count': 100,
             'total': 250},
        'data':
            [{'open': 220.97,
              'high': 225.35,
              'low': 220.27,
              'close': 222.91,
              'volume': 65242200.0,
              'symbol': 'AAPL',
              'exchange': 'XNAS',
              'date': '2024-11-01T00:00:00+0000'}]}
    assert get_stocks_rate(["AAPL"]) == [{'price': 222.91, 'stock': 'AAPL'}]
