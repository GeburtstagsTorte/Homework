def take_input():
    lst = []
    lines = open("file4").read().splitlines()
    for i in lines:
        i = i.split(" ")
        for j in i:
            try:
                j = int(j)
                lst.append(j)
            except ValueError:
                pass

    return lst


def sum_digits(x):
    x = str(x)
    s = 0
    for i in x:
        s += int(i)

    return s


def print_pair(x, y):
    print("(", x, ",", y, ")", end=" ")   # no new line for py


def check_pairs(lst):

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] % sum_digits(lst[j]) == 0 or lst[j] % sum_digits(lst[i]) == 0:
                print_pair(lst[i], lst[j])


def main():
    lst = take_input()
    check_pairs(lst)

if __name__ == "__main__":
    main()
