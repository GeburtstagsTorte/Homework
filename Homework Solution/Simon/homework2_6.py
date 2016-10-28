import re


def get_input():

        lst = []

        with open("homework2_6") as f:
            s = re.findall('[-\d]+', f.read())
            try:
                for i in s:
                    i = int(i)
                    lst.append(str(i))
            except ValueError:
                pass
        print(lst)
        return lst


def find_numbers(lst):

    final_lst = []

    for i in lst:
        if i[0] == i[int(len(i))-1]:
            final_lst.append(int(i))

    return final_lst


def main():
    lst = get_input()
    print(find_numbers(lst))

if __name__ == "__main__":
    main()
