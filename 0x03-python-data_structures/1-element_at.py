#!/usr/bin/python3
def element_at(my_list, idx):
    if int(idx) < 0:
        return None
    elif int(idx) > len(list(my_list)):
        return None
    else:
        return my_list[idx]


if __name__ == "__main__":
    element_at(my_list, idx)
