import time


def fibonacci_to_max_value(n):
    lst = [1, 2]
    for i in range(n//2):
        if lst[len(lst)-1] < n:
            lst.append(lst[len(lst)-2] + lst[len(lst)-1])
        else:
            return lst[:len(lst)-1]


def main(input_list):
    value = 0
    for i in input_list[1::3]:
        value += i
    return value


if __name__ == '__main__':
    t1 = time.time()
    result = main(fibonacci_to_max_value(4000000))
    t2 = time.time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
