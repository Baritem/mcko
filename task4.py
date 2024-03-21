import copy
import random
from utils import read_data, dump


def create_logins_and_passwords(data, headers):
    """
    Генерирует логин и пароль для всех ученых.
    :param data: Список ученых.
    :param headers: Названия колонок.
    :return: None
    """
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    small = "qwertyuiopasdfghjklzxcvbnm"
    capital = "QWERTYUIOPASDFGHJKLXCVBNM"
    digits = "1234567890"
    data_new = copy.copy(data)
    for idx, line in enumerate(data):
        s, n, p = line[0].split()
        login = s + "_" + n[0] + p[0]
        password = "".join(
            [random.choice(chars) for _ in range(7)] + [random.choice(small)] + [random.choice(capital)] + [
                random.choice(digits)])
        data_new[idx].append(login)
        data_new[idx].append(password)
    headers.append("login")
    headers.append("password")
    dump([headers] + data_new, "scientist_password.csv", sep=",")


if __name__ == "__main__":
    headers, data_list, data_dict = read_data("scientist.txt")
    create_logins_and_passwords(data_list, headers)
