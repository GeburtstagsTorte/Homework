def read_file():
    m = open("matrix1 file2").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]

    return m


def positive_col(m):
    col_sign = 1
    l = []

    for i in range(len(m[0])):
        for j in range(len(m)):
            col_sign *= m[j][i]

        if col_sign == 1:
            l.append(1)
        else:
            l.append(-1)

        col_sign = 1
    m.append(l)



def positive_row(m):
    row_sign = 1

    for i in range(len(m)):
        for j in range(len(m[i])):
            row_sign *= m[i][j]

        if row_sign == 1:
            m[i].append(1)
        else:
            m[i].append(-1)

        row_sign = 1

    return m


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] > 0:
                print(" " + str(m[i][j]), end="  ")
            else:
                print(str(m[i][j]), end="  ")
        print()
    # don't know how to do it better but at least it looks nice.


def main():
    m = read_file()
    positive_col(m)
    o = positive_row(m)
    print("Old matrix: \n")
    print_matrix(read_file())
    print("\nNew matrix: \n")
    print_matrix(o)


if __name__ == '__main__':
    main()
