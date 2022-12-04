#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        my_list.sort()

        return my_list[:-1]


if __name__ == "__main__":
    max_integer(my_list=[])
