# https://de.wikipedia.org/wiki/Bubblesort#/media/File:Bubble-sort-example-300px.gif
#
from test import SortTest


def bubble_sort(l):
    for i in range(len(l), 0, -1):
        for j in range(i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


if __name__ == '__main__':
    SortTest.minimum_test(bubble_sort)
