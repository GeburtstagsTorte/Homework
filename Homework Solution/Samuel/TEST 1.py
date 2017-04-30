# TEST 1
import re
from time import clock


def take_input():
    lst = []
    seen = set()
    with open("test1 file", "r") as f:
        s = re.findall('[-\d]+', f.read())
        for x in s:
            if x not in seen:
                lst.append(int(x))
                seen.add(x)
            else:
                return False
    return lst


def is_permutation(lst):
    if not lst:
        return False

    count = 0
    sum_lst = ((len(lst) * (len(lst) + 1)) / 2)

    for x in lst:
        count += abs(x)
    print(count)
    print(sum_lst)

    if abs(count) == sum_lst:
        return True
    else:
        return False


def is_permutation_v2(lst):
    if not lst:
        return False

    s = [x for x in range(min(lst), max(lst) + 1)]

    if sorted(lst) == s:
        return True
    else:
        return False


def is_permutation_v3(lst):
    if not lst:
        return False

    sum_lst = ((len(lst) * (len(lst) + 1)) // 2)
    count = 0

    for x in set(lst):
        count += x

    if count == sum_lst:
        return True


def main():
    u = take_input()
    t1 = clock()
    print(is_permutation(u))
    t2 = clock()
    print(t2-t1)

    t1 = clock()
    print(is_permutation_v2(u))
    t2 = clock()
    print(t2 - t1)

    t1 = clock()
    print(is_permutation_v3(u))
    t2 = clock()
    print(t2 - t1)

if __name__ == "__main__":
    main()
