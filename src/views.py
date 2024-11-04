import json

from src.utils import get_exchange_rate, get_stocks_rate, get_sum_by_card, get_top_five, greeting, read_excel


def main(date: str) -> str:
    """Главная функция страницы Главная."""
    result = json.loads(greeting(date))
    transaction_list = read_excel("../data/my_operations.xlsx")
    result["cards"] = json.loads(get_sum_by_card(transaction_list))
    result["top_transactions"] = json.loads(get_top_five(transaction_list))
    currencies_to_get_rates = ["USD", "EUR"]
    result["currency_rates"] = json.loads(get_exchange_rate(currencies_to_get_rates))
    ticker = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    result["stock_prices"] = json.loads(get_stocks_rate(ticker))
    return json.dumps(result, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    print(main("2024-11-04 19:03:01"))
