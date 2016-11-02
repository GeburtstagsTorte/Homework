
def file_input():
    m = open("matrix1 file4").read().splitlines()
    m = [[int(i) for i in j.split()]for j in m]
    return m


def zig_zag(m):
    # doesn't work with row length 4
    d = 1
    for i in range(len(m)):
        for j in range(d, len(m[0]), 4):
            print(j)
            m[i][j] = "x"
            if j < (len(m[0])-1) and d == 1:
                m[i][j+1] = "x"
            elif j > 0 and d == 0:
                m[i][j-1] = "x"

        d = 1 if d == 0 else 0

    return m


def zig_zagv2(m):
    # doesn't work with row length 4
    l = [m[i][j] for i in range(len(m)) for j in range(len(m[i]))]
    d = 1
    for i in range(d, len(l), 4):
        l[i] = 'x'
        if (i + 1) < len(l):
            l[i + 1] = 'x'

    m = [l[i - len(m[0]):i] for i in range(len(m[0]), len(l) + 1, len(m[0]))]

    return m


def zig_zagv3(m):
    d = 1
    l = [0]*len(m[0])
    for i in range(d, len(l), 4):
        l[i] = 1
        if (i+1) < len(l):
            l[i+1] = 1

    a = True
    for i in range(len(m)):
        for j, k in zip(range(len(m[0])), l):
            if k == int(a):
                m[i][j] = 'x'

        a = False if a else True

    return m
    # otherwise i can't print it.


def print_output(m):
    l = [[i for i in j if i != "x"] for j in m]
    for i in range(len(l[0])):
        for j in range(len(l)):
            print(l[j][i], end=" ")
    print()
    print()


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(str(m[i][j]), end=" ")
        print()


def main():
    m = zig_zagv3(file_input())
    print_output(m)
    print_matrix(m)

if __name__ == '__main__':
    main()
