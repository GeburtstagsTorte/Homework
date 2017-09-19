from time import time


def get_grid():
    m = open("grid_problem11").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]
    return m


def get_x(grid, i, j):
    try:
        return grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
    except IndexError:
        return 0


def get_y(grid, i, j):
    try:
        return grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
    except IndexError:
        return 0


def get_diagonal_left(grid, i, j):
    try:
        return grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
    except IndexError:
        return 0


def get_diagonal_right(grid, i, j):
    try:
        return grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
    except IndexError:
        return 0


def main(grid, i, j, temp_product, t1):
    temp = temp_product
    if i == 20:
        t2 = time()
        exit("Biggest Product: " + str(temp) + "\nTime: " + str((t2 - t1)*1000))

    for product in [get_x(grid, i, j), get_y(grid, i, j), get_diagonal_left(grid, i, j),
                    get_diagonal_right(grid, i, j)]:
        if product > temp:
            temp = product

    if j == 19:
        i += 1
        j = -1

    main(grid, i, j+1, temp, t1)


if __name__ == '__main__':
    t = time()
    main(get_grid(), 0, 0, 0, t)
