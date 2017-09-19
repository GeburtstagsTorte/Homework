import math
import time


def fibonacci_to_max_value(n):
    lst = [1, 2]
    for i in range(int(math.sqrt(n))):
        if lst[len(lst)-1] < n:
            lst.append(lst[len(lst)-2] + lst[len(lst)-1])
        else:
            return lst[:len(lst)-1]


def main(lst):
    value = 0
    for i in lst[1::3]:
        value += i
    return value

if __name__ == '__main__':
    t1 = time.time()
    lst = fibonacci_to_max_value(4000000)
    print(main(lst))
    print((time.time()-t1)*1000)
