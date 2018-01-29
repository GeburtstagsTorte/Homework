# source: http://www.codeadventurer.de/?p=2605
# all sorting algorithms: https://www.toptal.com/developers/sorting-algorithms/
from test import SortTest


def insertion_sort(l):
    for i in range(len(l)):
        while i > 0 and l[i-1] > l[i]:
            l[i], l[i-1] = l[i-1], l[i]
            i -= 1
    return l

if __name__ == '__main__':
    SortTest.minimum_test(insertion_sort)
