from unittest.mock import patch

from src.views import main_page


@patch("src.views.get_stocks_rate")
@patch("src.views.get_exchange_rate")
@patch("src.views.read_excel")
def test_main_page(mocked_read, mocked_exchange, mocked_stocks, transaction_list_for_main) -> None:
    """Тест на чтение файла csv."""
    mocked_read.return_value = transaction_list_for_main
    mocked_exchange.return_value = [{"currency": "USD", "rate": 97.83}, {"currency": "EUR", "rate": 105.45}]
    mocked_stocks.return_value = [{"stock": "AAPL",
                                  "price": 227.48},
                                  {"stock": "AMZN",
                                   "price": 210.05}]
    assert main_page("2024-11-04 20:03:11") == '''{
    "greeting": "Добрый вечер",
    "cards": [
        {
            "last_digits": "",
            "total_spent": -50000.0,
            "cashback": ""
        }
    ],
    "top_transactions": [
        {
            "date": "28.10.2024",
            "amount": -50000.0,
            "category": "Переводы",
            "description": "Перевод между счетами"
        }
    ],
    "currency_rates": [
        {
            "currency": "USD",
            "rate": 97.83
        },
        {
            "currency": "EUR",
            "rate": 105.45
        }
    ],
    "stock_prices": [
        {
            "stock": "AAPL",
            "price": 227.48
        },
        {
            "stock": "AMZN",
            "price": 210.05
        }
    ]
}'''
