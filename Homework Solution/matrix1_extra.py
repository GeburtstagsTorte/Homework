def open_matrix():

    matrix = []
    file = open("matrix1").read().splitlines()
    for i in file:
        matrix.append([])
        numbers = i.split()

        for j in numbers:
            try:
                matrix[len(matrix)-1].append(int(j))
            except ValueError:
                pass
    return matrix


def user_input():
    try:
        i = int(input("length of your squares: "))

    except ValueError:
        print("not an int!")
        return user_input()

    if i < 0:
        print("fuck you!")
        i = abs(i)

    return i


def squares(m, i):

    for j in range(len(m)-i+1):
        for n in range(len(m)-i+1):
            for x in range(j, i+j):
                for y in range(n, i+n):
                    print(m[x][y], end=" ")
                print()
            print()
        print("____________")


m = open_matrix()
i = user_input()
squares(m, i)
