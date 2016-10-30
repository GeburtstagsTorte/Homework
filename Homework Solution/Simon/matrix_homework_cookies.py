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


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


def replace_squares(m):
    # shat
    """if len(m) % 2 != 0:

            for p in range(len(m)//2+1):
                for l in range(len(m)//2+1):
                    try:
                        m[p][l], m[p+len(m)//2][l+len(m)//2] = m[p+len(m)//2][l+len(m)//2], m[p][l]
                    except IndexError:
                        pass

            for ü in range(len(m)//2+1, len(m)):
                for ö in range(len(m)//2+1):
                    try:
                        m[ü+1][ö+1], m[ü-len(m)//2+1][ö+len(m)//2+1] = m[ü-len(m)//2+1][ö+len(m)//2+1], m[ü+1][ö+1]
                    except IndexError:
                        pass"""

    for i in range(len(m)//2):
        for j in range(len(m)//2):
            m[i][j], m[i+len(m)//2][j+len(m)//2] = m[i+len(m)//2][j+len(m)//2], m[i][j]

    for o in range(len(m)//2):
        for k in range(len(m)//2, len(m)):
            m[o][k], m[o+len(m)//2][k-len(m)//2] = m[o+len(m)//2][k-len(m)//2], m[o][k]


def main():
    m = open_matrix()
    print("\nthe first matrix")
    print_matrix(m)
    replace_squares(m)
    print("\nthe second matrix")
    print_matrix(m)

if __name__ == '__main__':
    main()
