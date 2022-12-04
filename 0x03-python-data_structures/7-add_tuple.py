#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if 0 <= len(tuple_a) < 2:
        for i in range(2 - len(tuple_a)):
            tuple_a += (0,)
    elif 0 <= len(tuple_b) < 2:
        for i in range(2 - len(tuple_b)):
            tuple_b += (0,)
    tuple_c = (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])
    return tuple_c


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
