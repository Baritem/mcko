from utils import read_data
from task1 import find_allopurinol, print_allopurinol, find_duplicates

if __name__ == "__main__":
    headers, data_list, data_dict = read_data("scientist.txt")
    allopurinol = find_allopurinol(data_list)
    print_allopurinol(allopurinol)
    find_duplicates(data_list, headers)
