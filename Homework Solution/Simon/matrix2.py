"""lst = []
    lst2 = []
    for i in range(len(m)):              # for i in range(len(m)): # for j in range(i, (i+1)):
        for j in range(len(m)):
            print(j)
            print(i)
            lst.append(m[j][i])
            print("lst", lst)

        if eval('*'.join(str(k) for k in lst)) > 0:
            lst2.append(1)

        if eval('*'.join(str(l) for l in lst)) < 0:
            lst2.append(-1)

    print("lst2: ", lst2)
    m.append(lst2)
    return m"""


def open_matrix():             # no return of matrix needed

    m = open("matrix2_1").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]

    return m


def append_at_lines(m):

    for i in m:

        if eval('*'.join(str(k) for k in i)) > 0:
            i.append(1)

        else:
            i.append(-1)


def append_at_columns(m):

    new_column = []

    for i in range(len(m[0])):
        p = 1
        for j in range(len(m)):
            p *= m[j][i]
        new_column.append(p)

    m.append(new_column)


def print_matrix(m):

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:                          # tried that at first within the function -.-
                print(" " + str(m[i][j]), end=" ")
            else:
                print(m[i][j], end=" ")
        print()


def main():
    m = open_matrix()
    append_at_lines(m)
    append_at_columns(m)
    print_matrix(m)

if __name__ == '__main__':
    main()
