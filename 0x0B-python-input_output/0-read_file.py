#!/usr/bin/python3
"""contains module that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
