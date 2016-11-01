def open_matrix():

    m = open("matrix3").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]

    return m


def check_coordinates(m):

    for i in range(len(m[0])):
        for j in range(len(m)):
            lst = []
            lst.append(i+j)
            for k in lst:
                st = ""
                if int(k) % 2 != 0:
                    try:
                        st = str(m[i][j-1]) + str(m[i][j]) + str(m[i][j+1])
                        if st[0] == "0":
                            m[i][j] = int(st[1:])
                        else:
                            m[i][j] = int(st)
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
