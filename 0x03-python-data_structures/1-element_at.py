#!/usr/bin/python3
'''def element_at(my_list, idx):
    if int(idx) < 0 or int(idx) >= len(my_list):
        return None
    else:
        return my_list[idx]'''


def element_at(my_list, idx):
    return None if int(idx) < 0 or int(idx) >= len(my_list) else my_list[idx]


if __name__ == "__main__":
    element_at(my_list, idx)
