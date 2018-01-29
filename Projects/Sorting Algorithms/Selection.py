# source: https://de.wikipedia.org/wiki/Selectionsort
#
from test import SortTest


def selection_sort(l):
    for i in range(len(l)):
        index = i
        for j in range(i, len(l)):
            if l[j] < l[index]:
                index = j

        l[i], l[index] = l[index], l[i]
    return l

if __name__ == '__main__':
    SortTest.minimum_test(selection_sort)
