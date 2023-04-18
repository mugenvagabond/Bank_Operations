from utils import *


def main():
    print('Получение данных из файла...', end='')
    data = get_data()
    if data:
        print('\n---Данные получены---\n')

    print('Фильтрация данных...', end='')
    data = filter_data(data)
    if data:
        print('\n---Данные отфильтрованы---\n')

    print('Сортировка данных...', end='')
    data = sort_data(data)
    if data:
        print('\n---Данные отсортированы---')

    data = format_data(data)

    for row in data:
        print(row)


if __name__ == "__main__":
    main()
