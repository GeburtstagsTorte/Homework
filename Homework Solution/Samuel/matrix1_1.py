def open_matrix():

    matrix = []
    file = open("matrix file1").read().splitlines()
    for i in file:
        matrix.append([])
        numbers = i.split()

        for j in numbers:
            try:
                matrix[len(matrix)-1].append(int(j))
            except ValueError:
                pass
    return matrix


def open_matrix_v2():
    file = open("matrix file1").read().splitlines()
    m = [[int(i) for i in j.split()] for j in file]

    return m


def upper_left(m):
    for i in range(len(m) // 2):
        for j in range(len(m) // 2):
            print(m[i][j], end=" ")
        print()


def upper_right(m):
    for i in range(len(m) // 2):
        for j in range(len(m) // 2, len(m)):
            print(m[i][j], end=" ")
        print()


def lower_left(m):
    for i in range(len(m) // 2, len(m)):
        for j in range(len(m) // 2):
            print(m[i][j], end=" ")
        print()


def lower_right(m):
    for i in range(len(m) // 2, len(m)):
        for j in range(len(m) // 2, len(m)):
            print(m[i][j], end=" ")
        print()


def cookie_function(m):
    for i in range(len(m)):
        m[i] = m[i][len(m) // 2:] + m[i][:len(m) // 2]

    m = m[len(m) // 2:] + m[:len(m) // 2]

    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end=" ")
        print()


def main():
    m = open_matrix_v2()
    print()
    upper_left(m)
    print()
    upper_right(m)
    print()
    lower_left(m)
    print()
    lower_right(m)
    print("\nI want my cookies!\n")
    cookie_function(m)

if __name__ == '__main__':
    main()

