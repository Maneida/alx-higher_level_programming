#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string is not None:
        for i in my_string:
            if i == 'c' or i == 'C':
                i = ''
            new_string += i
        return new_string


if __name__ == "__main__":
    no_c(my_string)
