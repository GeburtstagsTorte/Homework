def read_matrix():
    matrix = []
    lines = open("m_file").read().splitlines()
    for line in lines:
        matrix.append([])
        numbers = line.split(" ")

        for n in numbers:
            try:
                matrix[len(matrix)-1].append(int(n))
            except ValueError:
                pass

    return matrix


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


def print_main_diagonal(m):
    for i in range(len(m)):
        print(m[i][i], end=" ")


def print_secondary_diagonal(m):
    for i in range(len(m)):
        print(m[i][len(m)-i-1], end=" ")


def print_numbers_above_the_main_diagonal(m):
    for i in range(len(m)):
        for j in range(i+1, len(m)): # in Python range(i+1, len(m)) goes from i+1 up to len(m)-1
            print(m[i][j], end=" ")


def print_numbers_below_the_main_diagonal(m):
    for i in range(1, len(m)):
        for j in range(i): # so j goes from 0 to i-1
            print(m[i][j], end=" ")


def print_numbers_above_the_second_diagonal(m):
    for i in range(len(m)-1):
        for j in range(len(m)-i-1):
            print(m[i][j], end=" ")


def print_numbers_below_the_second_diagonal(m):
    for i in range(1, len(m)):
        for j in range(len(m)-i, len(m)):
            print(m[i][j], end=" ")


def add_line(m, line):
    m.append(line)


def add_column(m, column):
    for i in range(len(column)):
        m[i].append(column[i])


def main():
    m = read_matrix()
    print_matrix(m)
    print("Main diagonal:")
    print_main_diagonal(m)
    print("\nNumbers above the first diagonal:")
    print_numbers_above_the_main_diagonal(m)
    print("\nNumbers below the main diagonal:")
    print_numbers_below_the_main_diagonal(m)
    print("\nSecondary diagonal:")
    print_secondary_diagonal(m)
    print("\nNumbers above the secondary diagonal:")
    print_numbers_above_the_second_diagonal(m)
    print("\nNumbers below the secondary diagonal:")
    print_numbers_below_the_second_diagonal(m)
    print("\nAdding Line (to the end): [1, 2, 0, -9]")
    add_line(m, [1, 2, 0, -9])
    print_matrix(m)
    print("\nAdding column: [0, 0, 0, 0, 0]")
    add_column(m, [0, 0, 0, 0, 0])
    print_matrix(m)

    # Accessing a number
    # m[row][column]
    # Accessing a line:
    # m[row]

if __name__ == "__main__":
    main()