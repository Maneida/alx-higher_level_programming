#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for index in range(len(my_list)):
        if type(my_list[index]) == int:
            print("{:d}".format(my_list[index]))


if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
