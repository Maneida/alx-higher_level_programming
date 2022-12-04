#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for i in matrix:
            for j in i:
                print("{:d}".format(j), end='')
                if j != i[-1]:
                    print(" ", end='')
            print("\n", end='')


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
