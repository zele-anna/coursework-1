import pandas as pd

from src.views import main_page
from src.services import simple_search
from src.utils import read_excel
from src.reports import spending_by_category

date = "2024-11-08 18:45:00"

main_page(date)

transactions_list = read_excel("data/operations.xlsx")
string_for_simple_search = "Пополнение"

search_result_json = simple_search(transactions_list, string_for_simple_search)

df = pd.DataFrame(transactions_list)
category_to_find = "Переводы"

data_for_report = spending_by_category(df, category_to_find)
