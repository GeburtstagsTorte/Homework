#TEST 1


def take_input():
    with open("test1 file", "r") as f:
        s = f.read()
        lst = [int(x) for x in s.split(", ") if x.isdigit()]

        return lst


def is_permutation(lst):
    count = 0
    sum_lst = ((len(lst)*(len(lst)+1))/2)
    
    for x in lst:
        count += x

    if count == sum_lst:
        return True
    else:
        return False


def main():
    u = take_input()
    print(u)
    print(is_permutation(u))


if __name__ == "__main__":
    main()
