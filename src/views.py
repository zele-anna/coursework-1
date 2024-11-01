from datetime import datetime

def greeting(date):
    """"Функция возвращает приветствие в зависимости от текущего времени суток."""
    date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    if date_obj.hour <= 4:
        print("Доброй ночи")
    elif date_obj.hour <= 11:
        print("Доброе утро")
    elif date_obj.hour <= 17:
        print("Добрый день")
    else:
        print("Добрый вечер")


transaction_list = read_excel("../data/my_operations.xlsx")

cards_info = get_sum_by_card(transaction_list)


if __name__ == "__main__":
    greeting("2024-12-03 04:03:01")
    for key, value in cards_info.items():
        print(f'По карте: {key} общая сумма операций {round(value["Сумма операции"], 2)}, кэшбэк: {value["Кэшбэк"]}')