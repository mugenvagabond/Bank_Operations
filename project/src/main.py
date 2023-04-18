from project.src.utils import get_data, filter_data, sort_data, format_data


def main():
    print('Получение данных из файла...', end='')
    data = get_data('operations.json')
    print(data)
    if data:
        print('\n---Данные получены---\n')

    print('Фильтрация данных...', end='')
    filterer = filter_data(data)
    if filterer:
        print('\n---Данные отфильтрованы---\n')

    print('Сортировка данных...', end='')
    sorter = sort_data(data)
    if sorter:
        print('\n---Данные отсортированы---')

    formatter = format_data(data)

    for row in formatter:
        print(row)


if __name__ == "__main__":
    main()
