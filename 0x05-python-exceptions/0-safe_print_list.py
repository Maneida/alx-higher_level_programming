#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        list_len = 0
        for i in my_list:
            list_len += 1

        if x <= list_len:
            pass
        elif x > list_len:
            x = list_len

        for j in range(x):
            print("{:d}".format(my_list[j]), end='')
        print("")

        return (x)
    
    except Exception as e:
        print(e)
