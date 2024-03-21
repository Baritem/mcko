def read_data(path):
    """
    Чтение данных из файла
    :param path: Путь к файлу
    :return: Заголовки столбцов, Данные в виде списка, данные в виде словаря
    """
    try:
        lst = []
        data = dict()
        with open(path, "r", encoding="UTF-8") as f:
            headers = f.readline().replace("\n", "").replace("\r", "").split("#")
            for line in f.readlines():
                lst.append(line.replace("\n", "").replace("\r", "").split("#"))
            for i in range(len(headers)):
                data[headers[i]] = []
                for line in lst:
                    data[headers[i]].append(line[i])
        return headers, lst, data
    except Exception as e:
        print(e)
        return None

def dump(data, path):
    """
    Сохраняет данные в файл
    :param data: Данные для сохранения
    :param path: Путь к файлу для сохранения
    :return: None
    """
    with open(path, "w", encoding="utf-8") as f:
        for line in data:
            s = ""
            for item in line:
                s += str(item) + "#"
            s = s[:-1] + "\n"
            f.write(s)