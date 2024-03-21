from utils import read_data


def qsort(data, left, right, comp_index=2):
    """
    Быстрая сортировка для таблицы.
    :param data: Данные
    :param left: Левая граница отрезка, который нужно отсортировать.
    :param right: Правая граница отрезка, который нужно отсортировать.
    :param comp_index: Индекс колонки для сравнения.
    :return: None
    """
    if right <= left:
        return
    pivot = right
    l0, r0 = left, right
    right -= 1
    while left < right:
        while left < right and data[left][comp_index] <= data[pivot][comp_index]:
            left += 1
        while right > left and data[right][comp_index] > data[pivot][comp_index]:
            right -= 1
        if left != right:
            data[left], data[right] = data[right], data[left]

    if data[pivot][comp_index] < data[left][comp_index]:
        data[left], data[pivot] = data[pivot], data[left]
    if right < left:
        qsort(data, l0, left, comp_index)
        qsort(data, left, pivot, comp_index)
    else:
        if left - 1 >= l0:
            qsort(data, l0, left, comp_index)
        if left + 1 <= pivot:
            qsort(data, left + 1, pivot, comp_index)
    return None


if __name__ == "__main__":
    headers, data_list, data_dict = read_data("scientist.txt")
    qsort(data_list, 0, len(data_list) - 1, 2)
    for line in data_list[:5]:
        print(f"{line[0]}: {line[1]}")
