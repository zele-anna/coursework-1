import json
import logging

logging.basicConfig(
    filename="../logs/services.log",
    filemode="w",
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)

services_logger = logging.getLogger("services")


def simple_search(transactions: list, string_to_find: str) -> str:
    """Принимает на вход список транзакций и строку для поиска
    и возвращает список транзакций с искомой строкой в описании."""
    services_logger.info("Поиск транзакций по заданному описанию.")
    new_list = [x for x in transactions if string_to_find.lower() in x["Описание"].lower()]
    return json.dumps(new_list, indent=4, ensure_ascii=False)