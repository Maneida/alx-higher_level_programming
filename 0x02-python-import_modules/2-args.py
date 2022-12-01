#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if int(len(sys.argv)) == 1:
        str_end = '.'
    else:
        str_end = ':'

    if int(len(sys.argv)) != 2:
        arg_string = 'arguments'
    else:
        arg_string = 'argument'

    print("{:d} {:s}{:s}".format(int(len(sys.argv)) - 1, arg_string, str_end))

    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
