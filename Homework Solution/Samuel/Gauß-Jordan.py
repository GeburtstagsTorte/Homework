from sys import exit


class Fraction:

    def __init__(self, div1, div2):
        self.div1, self.div2 = Fraction.convert_to_list(div1), Fraction.convert_to_list(div2)

    def multiply(self):
        return Fraction.cancel([self.div1[0] * self.div2[0], self.div1[1] * self.div2[1]])

    def divide(self):
        return Fraction.cancel([self.div1[0] * self.div2[1], self.div1[1] * self.div2[0]])

    def subtract(self):
        solution = [self.div1[0] - self.div2[0], self.div1[1]] if self.div1[1] == self.div2[1] else \
            [(self.div1[0] * self.div2[1]) - (self.div2[0] * self.div1[1]), self.div1[1] * self.div2[1]]
        return Fraction.cancel(solution)
        # defuq?!

    def add(self):
        solution = [self.div1[0] + self.div2[0], self.div1[1]] if self.div1[1] == self.div2[1] else \
            [(self.div1[0] * self.div2[1]) + (self.div2[0] * self.div1[1]), self.div1[1] * self.div2[1]]
        return Fraction.cancel(solution)

    @staticmethod
    def cancel(solution):
        x, y = solution[0], solution[1]
        while y != 0:
            x, y = y, x % y
        return solution[0] // x if solution[1]//x == 1 else str(solution[0] // x) + "/" + str(solution[1] // x)

    @staticmethod
    def convert_to_list(n):
        if type(n) == str:
            div_list, num = [], ""
            for i in n:
                if i != "/":
                    num += i
                else:
                    div_list.append(int(num))
                    num = ""
            div_list.append(int(num))
            return div_list
        return [n, 1] if type(n) == int else exit("failed by trying to convert {}.".format(n))


def file_input():
    f = open("matrix Gauß-Jordan").read().splitlines()
    m = [[i for i in j.split()] for j in f]
    # dumb fuck shit, gonna change it but im tired
    for i in range(len(m)):
        for j in range(len(m[0])):
            try:
                m[i][j] = int(m[i][j])
            except ValueError:
                pass
    return m


def organize_rows(m):
    # replaces first row if the first variable is zero
    if m[0][0] == 0:
        for i in range(len(m)):
            if m[i][0] != 0:
                m[0], m[i] = m[i], m[0]
                break


def rearrange_lower_triangle(m, n):
    div = m[n][n]
    for i in range(len(m[0])):
        if check_last_row(m):
            m[n][i] = Fraction(m[n][i], div).divide()


def finish_column_lower_triangle(m, n):
    # transforms matrix to matrix with gauss triangle in the lower left corner
        for i in range(1+n, len(m)):
            multiple = m[i][n]
            for j in range(len(m[i])):
                m[i][j] = Fraction(m[i][j], Fraction(multiple, m[n][j]).multiply()).subtract()

        if n < len(m) - 1:
            rearrange_lower_triangle(m, n + 1)
            finish_column_lower_triangle(m, n + 1)


def finish_column_upper_triangle(m, n):
    # transforms matrix to matrix with gauss triangle in the upper left corner
    for i in range(len(m)-1-n)[::-1]:
        multiple = m[i][len(m)-1-n]
        for j in range(len(m[0])):
            m[i][j] = Fraction(m[i][j], Fraction(multiple, m[len(m)-1-n][j]).multiply()).subtract()

    if n < len(m):
        finish_column_upper_triangle(m, n + 1)


def check_last_row(m):
    # controls last row
    if m[len(m)-1][len(m[0])-1] == 0 and m[len(m)-1][len(m[0])-2] == 0:
        print_matrix(m)
        print("\nSystem has infinite solutions.")
        exit(0)
    elif m[len(m)-1][len(m[0])-1] != 0 and m[len(m)-1][len(m[0])-2] == 0:
        print("System is unsolvable.")
        exit(0)
    return True


def overdetermination_trail(u, m):
    for i in range(len(u)):
        count = 0
        for j in range(len(u[i])-1):
            count = Fraction(Fraction(u[i][j], m[j][len(m[0])-1]).multiply(), count).add()
        if count != Fraction.cancel(Fraction.convert_to_list(u[i][len(u[0])-1])):
            return False
    return True


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(str(m[i][j]), end=" ")
        print()


def main():
    from string import ascii_lowercase
    l = list(ascii_lowercase)
    m = file_input()
    u = m[len(m[0]) - 1:]
    m = m[:len(m[0]) - 1]
    organize_rows(m)
    rearrange_lower_triangle(m, 0)
    finish_column_lower_triangle(m, 0)
    # print_matrix(m)
    finish_column_upper_triangle(m, 0)

    if len(u) > 0:
        if overdetermination_trail(u, m):
            print("\nTrail returned true. => Solution:\n")
            for i in (range(len(m))):
                print("{} = {}".format(l[i], m[i][len(m[0])-1]))
        else:
            print("System has no solutions.")
        exit(0)
    else:
        print("\nSolution:\n")
        for i in (range(len(m))):
            print("{} = {}".format(l[i], m[i][len(m[0]) - 1]))

if __name__ == '__main__':
    main()
