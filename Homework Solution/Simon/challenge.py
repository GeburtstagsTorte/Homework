import re


def get_input():

        lst = []

        with open("challenge1") as f:
            s = re.findall('[-\d]+', f.read())
            try:
                for i in s:
                    i = int(i)
                    lst.append(i)
            except ValueError:
                pass

        return lst


def make_lst2(lst):

    lst2 = []

    for i in range(1, len(lst)+1):
        lst2.append(i)

    return lst2


def compare_lsts(lst2, lst):

        if lst2 == sorted(lst):
            print("True")
            return True
        else:
            print("False")
            return False


def main():
    lst = get_input()
    lst2 = make_lst2(lst)
    compare_lsts(lst2, lst)


if __name__ == "__main__":
    main() # code is a bit long but "it works man!!"