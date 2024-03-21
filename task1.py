from utils import dump


def find_allopurinol(data):
    res = []
    for line in data:
        if line[1] == "Аллопуринол":
            res.append((line[0], line[2]))
    return res


def print_allopurinol(allopurinol):
    allopurinol.sort(key=lambda x: x[1])
    print("Разработчиками Аллопуринола были такие люди")
    for item in allopurinol:
        print(item[0], item[1])


def find_duplicates(data, headers):
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
