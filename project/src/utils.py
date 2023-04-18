import json
from datetime import datetime
import time


def get_data():
    """
    Функция открывает json файл и преобразует данные из него в формате списка
    в переменную
    :return: data
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    time.sleep(0.8)
    return data


def filter_data(data):
    """
    Функция принимает на вход список словарей из json файла и
    отбирает только те операции, у которых в поле state указаны
    только успешные операции - EXECUTED
    :param data:
    :return: data
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    time.sleep(0.8)
    return data


def sorted_key(x):
    """
    Функция принимает на вход элементы списка и сортирует их по дате
    :param x:
    :return: x['date']
    """
    return x['date']


def sort_data(data):
    """
    Функция принимает на вход отсортированные по дате успешные операции
    и выводит последние 5 операций
    :param data:
    :return: data[:5]
    """
    data = sorted(data, key=sorted_key, reverse=True)
    time.sleep(0.8)
    return data[:5]


def format_data(data):
    """
    Функция принимает последние 5 успешных операций (по дате) и выводит
    данные по этим операциям в отформатированном виде
    :param data:
    :return: formatted_data
    """
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description = row['description']
        if "from" in row:
            from_arrow = "->"
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
        else:
            sender_info = "Новый счёт ->"
            sender_bill = ""
            from_arrow = ""
        amount = row['operationAmount']['amount']
        currency = row['operationAmount']['currency']['name']
        recipient = row['to'].split()
        recipient_bill = "".join(recipient)
        recipient_info = f"{recipient_bill[:4]} {recipient_bill[4:6]}** **** {recipient_bill[-4:]}"

        formatted_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow} {recipient_info}
{amount} {currency} """)
    return formatted_data

