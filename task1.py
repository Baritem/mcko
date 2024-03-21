from utils import dump, read_data


def find_allopurinol(data):
    """
    Ищет всех подельников препарата Аллопуринол.
    :param data: Данные для поиска.
    :return: Список строк с препаратом Аллопуринол.
    """
    res = []
    for line in data:
        if line[1] == "Аллопуринол":
            res.append((line[0], line[2]))
    return res


def print_allopurinol(allopurinol):
    """
    Выводит на печать всех подельников препарата Аллопуринол.
    :param allopurinol: Список строк с препаратом Аллопуринол.
    :return: None
    """
    allopurinol.sort(key=lambda x: x[1])
    print("Разработчиками Аллопуринола были такие люди")
    for item in allopurinol:
        print(item[0], item[1])


def find_duplicates(data, headers):
    """
    Ищет дубликаты среди лекарств, удаляет их и сохраняет в файл.
    :param data: Данные для поиска.
    :param headers: Названия столбцов
    :return: None
    """
    found = dict()
    for line in data:
        if line[1] in found:
            found[line[1]].append(line)
        else:
            found[line[1]] = [line]
    duplicates_removed = []
    for k, v in found.items():
        v = sorted(v)
        duplicates_removed.append(v[0])
    duplicates_removed = sorted(duplicates_removed, key=lambda x: x[2])
    dump([headers] + duplicates_removed, "scientist_origin.txt")

if __name__ == "__main__":
    headers, data_list, data_dict = read_data("scientist.txt")
    allopurinol = find_allopurinol(data_list)
    print_allopurinol(allopurinol)
    find_duplicates(data_list, headers)