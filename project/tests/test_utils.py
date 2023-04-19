import os.path

from project.src.utils import *


def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-07-03T18:35:29.512364',
                                                '2017-08-26T10:50:58.294041']


def test_filter_data(test_data):
    assert [x for x in test_data if 'state' in x and x['state'] == 'EXECUTED'] != [{
            "id": 41428829,
            "to": "Счет 35383033474447895560"
    }, ]
    assert [x for x in test_data if 'state' in x and x['state'] == 'EXECUTED'] != [
        {
            "id": 41428829,
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }, ]
    assert [x for x in test_data if 'state' in x and x['state'] == 'EXECUTED'] == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }, ]


def test_get_data():
    assert get_data(os.path.abspath('test_file.json')) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"}
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]


def test_format_data(test_data):
    assert type(format_data(test_data)) == list
