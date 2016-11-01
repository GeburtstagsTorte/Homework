
def file_input():
    m = open("matrix1 file4").read().splitlines()
    m = [[int(i) for i in j.split()]for j in m]

    return m


def zig_zag(m):
    d = 1

    for i in range(len(m)):
        for j in range(d, len(m[0]), 4):
            m[i][j] = "x"
            if j < (len(m[0])-1) and d == 1:
                m[i][j+1] = "x"
            elif j > 0 and d == 0:
                m[i][j-1] = "x"

        d = 1 if d == 0 else 0
    return m

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
    m = zig_zag(file_input())
    print_output(m)
    print_matrix(m)

if __name__ == '__main__':
    main()
