# TEST 1
import re


def take_input():
    lst = []
    seen = set()
    with open("test1 file", "r") as f:
        s = re.findall('[-\d]+', f.read())
        for x in s:
            if x not in seen:
                lst.append(x)
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
        count += int(x)

    if count == sum_lst:
        return True
    else:
        return False


def main():
    u = take_input()
    print(is_permutation(u))


if __name__ == "__main__":
    main()
