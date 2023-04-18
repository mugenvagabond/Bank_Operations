import json
from datetime import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sorted_key(x):
    return x['date']


def sort_data(data):
    data = sorted(data, key=sorted_key, reverse=True)
    return data[:5]


def format_data(data):
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
        {amount} {currency}
        """)
    return formatted_data

