def read_data(path):
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
    with open("scientist_origin.txt", "w", encoding="utf-8") as f:
        for line in data:
            s = ""
            for item in line:
                s += str(item) + "#"
            s = s[:-1] + "\n"
            f.write(s)