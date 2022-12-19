#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        if int(value) == value:
            return (True)
        else:
            return (False)

    except Exception as e:
        pass
