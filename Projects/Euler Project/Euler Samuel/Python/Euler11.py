# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

# optimization options: searching pattern, exclude areas with lower numbers etc. // not necessary


def get_input():
    m = open("euler11.txt").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]
    return m


def get_x_value(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])-3):
            c = 1
            for k in m[0][j:j+4]:
                c *= k
            count = c if c > count else count
    return count


def get_y_value(m):
    count = 0
    for i in range(len(m[0])):
        for j in range(len(m)-3):
            c = 1
            for k in range(4):
                c *= m[j+k][i]
            count = c if c > count else count
    return count


def get_diagonal_value(m):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            try:
                c = 1
                for k in range(4):
                    c *= m[j+k][i+k]
                count = c if c > count else count
            except IndexError:
                pass
    return count


def get_diagonal_value_reversed(m):
    count = 0
    for i in range(3, len(m[0]))[::-1]:
        for j in range(len(m)):
            try:
                c = 1
                for k in range(4):
                    c *= m[j+k][i-k]
                count = c if c > count else count
            except IndexError:
                pass
    return count


def main():
    from time import time
    m = get_input()
    t1 = time()
    l = sorted([get_x_value(m), get_y_value(m), get_diagonal_value(m), get_diagonal_value_reversed(m)])
    t2 = time()
    print(l[len(l)-1])
    print((t2-t1)*1000)

if __name__ == '__main__':
    main()
