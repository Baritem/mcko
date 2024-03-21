from utils import read_data


def task3(data=None):
    """
    Функция для поиска препаратов, созданных в определённую дату.
    :param data: Данные для поиска, если None, то будут загружены из scientist.txt
    :return:
    """
    if data is None:
        headers, data, data_dict = read_data("scientist.txt")
    data = sorted(data, key=lambda x: x[2])

    s = input()
    while s != "эксперимент":
        l, r = 0, len(data) - 1
        m = (l + r) // 2
        while l <= r:
            if data[m][2] <= s:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2
        i = m
        flag = True
        while i < len(data) and data[i][2] == s:
            flag = False
            print(f"Ученый {data[i][0]} создал препарат: {data[i][1]} - {data[i][2]}”")
            i += 1
        if flag:
            print("В этот день ученые отдыхали")
        s = input()

if __name__ == "__main__":
    task3()
