from datetime import datetime, timedelta
from functools import wraps
from typing import Any, Callable, Optional

import pandas as pd


def save_to_file(filename: Optional[str] = "category_report.csv") -> Callable:
    """Декоратор принимает список транзакций и искомую категорию и создает отчет о тратах в данной категории в файл.
    Имя файла опционально задается в параметрах декоратора.
    Если имя файла не задано, данные сохраняются в файл 'category_report'"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            func_result = func(*args, **kwargs)
            func_result.to_csv("../reports/" + filename)
        return wrapper
    return decorator


@save_to_file()
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str | None] = None) -> pd.DataFrame:
    """Функция собирает данные о тратах в заданной категории за 3 последних месяца от переданной даты
    или от текущего дня, если дата не передана."""
    if date is None:
        end_day = datetime.today().replace(hour=23, minute=59, second=59)
    else:
        end_day = datetime.strptime(date, "%d.%m.%Y").replace(hour=23, minute=59, second=59)
    start_day = end_day - timedelta(days=90)
    start_day.replace(hour=00, minute=00, second=00)
    spent_by_category = transactions.loc[transactions["Категория"] == category]
    spent_by_category_list = spent_by_category.to_dict(orient="records")
    result_func = list()
    for item in spent_by_category_list:
        item_date = datetime.strptime(item["Дата операции"], "%d.%m.%Y %H:%M:%S")
        if start_day <= item_date <= end_day:
            result_func.append(item)
    return pd.DataFrame(result_func)
