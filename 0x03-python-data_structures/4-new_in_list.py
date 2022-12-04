#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        list_copy = my_list.copy
        list_copy[idx] = element
        return list_copy


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
