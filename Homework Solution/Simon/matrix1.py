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
# have to revise print_matrix but it isn't needed, is it?


def print_upper_left(m):

    for i in range(len(m[0])//2): # since it is a "square" it doesnt matter if m[n] or just m
        for j in range(len(m)//2):
            print(m[i][j], end=" ")


def print_upper_right(m):

    for i in range(0, len(m) // 2):
        for j in range(len(m)//2, len(m)):
            print(m[i][j], end=" ")


def print_lower_right(m):         # revisit !

    for i in range(len(m) // 2, len(m)):
        for j in range(len(m)//2, len(m)):
            print(m[i][j], end=" ")


def print_lower_left(m):

    for i in range(len(m[0])//2, len(m[0])):
        for j in range(len(m)//2):
            print(m[i][j], end=" ")


def main():
    m = open_matrix()
    print("\nPrinting upper left: ")
    print_upper_left(m)
    print("\nPrinting upper right: ")
    print_upper_right(m)
    print("\nPrinting lower left: ")
    print_lower_left(m)
    print("\nPrinting lower right: ")
    print_lower_right(m)

if __name__ == "__main__":              # sorry i couldn't figure out a proper way to print them im little squares
    main()