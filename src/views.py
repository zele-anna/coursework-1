import json
import os

from src.utils import get_exchange_rate, get_stocks_rate, get_sum_by_card, get_top_five, greeting, read_excel

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "../data", "my_operations.xlsx")


def main_page(date: str) -> str:
    """Главная функция страницы Главная."""
    result = dict()
    result["greeting"] = greeting(date)
    transaction_list = read_excel(PATH_TO_FILE)
    result["cards"] = get_sum_by_card(transaction_list)
    result["top_transactions"] = get_top_five(transaction_list)
    currencies_to_get_rates = ["USD", "EUR"]
    result["currency_rates"] = get_exchange_rate(currencies_to_get_rates)
    ticker = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    result["stock_prices"] = get_stocks_rate(ticker)
    return json.dumps(result, indent=4, ensure_ascii=False)
