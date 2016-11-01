def open_matrix():

    m = open("matrix3").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]

    return m


def check_coordinates(m):

    for i in range(len(m[0])):
        for j in range(len(m)):
            if int(i+j) % 2 != 0:
                try:
                    st = str(m[j][i-1]) + str(m[j][i]) + str(m[j][i+1])
                    if st[0] == "0":
                        m[j][i] = int(st[1:])
                    else:
                        m[j][i] = int(st)
                except IndexError:
                    pass


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


def main():
    m = open_matrix()
    check_coordinates(m)
    print_matrix(m)

if __name__ == '__main__':
    main()
