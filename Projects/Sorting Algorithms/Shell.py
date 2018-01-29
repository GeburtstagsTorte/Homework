# source: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html
#
from test import SortTest


def shell_sort(l):
    n = len(l) // 2
    while n > 0:
        for i in range(n):
            insertion(l, i, n)
        n //= 2
    return l


def insertion(l, i, gap):
    for j in range(i + gap, len(l), gap):
        while j >= gap and l[j-gap] > l[j]:
            l[j], l[j-gap] = l[j-gap], l[j]
            j -= gap

if __name__ == '__main__':
    SortTest.minimum_test(shell_sort)
