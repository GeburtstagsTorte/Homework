# source: https://pythonandr.com/2015/07/05/the-merge-sort-python-code/
# divide and conquer
from test import SortTest


def merge(l, r):
    lst = []

    while len(l) > 0 and len(r) > 0:
        if l[0] < r[0]:
            lst.append(l[0])
            del l[0]
        else:
            lst.append(r[0])
            del r[0]

    return lst + l + r


def merge_sort(lst):
    """
        using recursion to sort the list; divide and conquer
        -> splitting the list in sub-lists sort and merge them in the end
    """
    if len(lst) < 2:
        return lst
    else:
        n = len(lst) // 2
        l = merge_sort(lst[:n])
        r = merge_sort(lst[n:])
        return merge(l, r)

if __name__ == '__main__':
    SortTest.test_all(merge_sort)
