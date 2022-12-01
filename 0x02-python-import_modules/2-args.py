#!/usr/bin/python3

'''if __name__ == "__main__":
    from sys import argv
    if int(len(argv)) == 1:
        str_end = '.'
    else:
        str_end = ':'

    if int(len(argv)) != 2:
        arg_string = 'arguments'
    else:
        arg_string = 'argument'

    print("{:d} {:s}{:s}".format(int(len(argv)) - 1, arg_string, str_end))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))'''

if __name__ == "__main__":
    from sys import argv
    userin = argv[1:]
    size = len(userin)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) is not 1 else "argument",
                 "." if (size) is 0 else ":"))
    for idx, arg in enumerate(userin):
        print("{:d}: {:s}".format(idx + 1, arg))
