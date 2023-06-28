#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    l_i = list_of_integers
    beg = 0
    end = len(l_i)-1

    if (l_i)[beg] > (l_i)[beg+1]:
        return (l_i)[beg]
    if (l_i)[end] > (l_i)[end-1]:
        return (l_i)[end]

    mid = (beg+end)//2
    if (l_i)[mid-1] < (l_i)[mid] and (l_i)[mid+1] < (l_i)[mid]:
        return (l_i)[mid]
    if (l_i)[mid] < (l_i)[mid-1]:
        return find_peak((l_i)[beg:mid+1])
    elif (l_i)[mid] < (l_i)[mid+1]:
        return find_peak((l_i)[mid:end+1])
    else:
        return (l_i)[beg]
