import datetime

from utils import read_excel, get_sum_by_card

def greeting():
    """"Функция возвращает приветствие в зависимости от текущего времени суток."""
    now = datetime.datetime.now()
    if now.hour <= 4:
        print("Доброй ночи")
    elif now.hour <= 11:
        print("Доброе утро")
    elif now.hour <= 17:
        print("Добрый день")
    else:
        print("Добрый вечер")

transaction_list = read_excel("../data/my_operations.xlsx")

cards_info = get_sum_by_card(transaction_list)


if __name__ == "__main__":
    greeting()
    for key, value in cards_info.items():
        print(f'По карте: {key} общая сумма операций {round(value["Сумма операции"], 2)}, кэшбэк: {value["Кэшбэк"]}')