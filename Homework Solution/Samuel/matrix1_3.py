def file_input():
    m = open("matrix1 file3").read().splitlines()
    m = [[int(i) for i in j.split() if int(i) >= 0] for j in m]

    return m


def is_divisible(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i+j) % 2 != 0:
                if (j-1) < 0:
                    m[i][j] = int(str(m[i][j]) + str(m[i][j + 1]))
                elif (j+1) == len(m[i]):
                    m[i][j] = int(str(m[i][j - 1]) + str(m[i][j]))
                else:
                    m[i][j] = int(str(m[i][j - 1]) + str(m[i][j]) + str(m[i][j + 1]))



def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(str(m[i][j]), end=" ")
        print()


def main():
    m = file_input()
    print("\nOld matrix: \n")
    print_matrix(m)
    print("\nNew matrix: \n")
    is_divisible(m)
    print_matrix(m)


if __name__ == '__main__':
    main()


