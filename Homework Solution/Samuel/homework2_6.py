import re


def file_input():
    with open("file2_6") as f:
        s = re.findall('[-\d]+', f.read())

    return s


def is_sum(s):
    count = 0

    for char in s:
        if char[0] == char[len(char)-1]:
            count += 1

    return count


def main():
    s = file_input()
    print(is_sum(s))


if __name__ == '__main__':
    main()
