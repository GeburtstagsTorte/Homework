class Fraction:

    def __init__(self, div1, div2):
        self.div1 = div1
        self.div2 = div2

    def multiply(self):
        solution = [self.div1[0] * self.div2[0], self.div1[1] * self.div2[1]]
        return Fraction.cancel(solution)

    def divide(self):
        solution = [self.div1[0] * self.div2[1], self.div1[1] * self.div2[0]]
        return Fraction.cancel(solution)

    def subtract(self):
        if self.div1[1] == self.div2[1]:
            solution = [self.div1[0] - self.div2[0], self.div1[1]]
        else:
            solution = [self.div1[0] * self.div2[1] - self.div2[0] * self.div1[1], self.div1[1] * self.div2[1]]
        return Fraction.cancel(solution)

    @staticmethod
    def cancel(solution):
        x = solution[0]
        y = solution[1]

        while y != 0:
            x, y = y, x % y

        if solution[1]//x == 1:
            return solution[0] // x
        else:
            return str(solution[0] // x) + "/" + str(solution[1] // x)


def file_input():
    f = open("matrix Gauß-Jordan").read().splitlines()
    m = [[int(i) for i in j.split()] for j in f]

    return m


def organize_rows(m):
    if m[0][0] == 0:
        for i in range(len(m)):
            if m[i][0] != 0:
                m[0], m[i] = m[i], m[0]
                break


def rearrange_lower_triangle(m, n):
    div = convert_to_list(m[n][n])
    for i in range(len(m[0])):
        y = convert_to_list(m[n][i])
        m[n][i] = Fraction(y, div).divide()


def finish_column_lower_triangle(m, n):
    for i in range(1+n, len(m)):
        multiple = convert_to_list(m[i][n])
        for j in range(len(m[i])):
            x = convert_to_list(Fraction(multiple, convert_to_list(m[n][j])).multiply())
            m[i][j] = Fraction(convert_to_list(m[i][j]), x).subtract()


def finish_column_upper_triangle(m, n):
    for i in range(len(m)-1-n)[::-1]:
        multiple = convert_to_list(m[i][len(m)-1-n])
        for j in range(len(m[0])):
            x = convert_to_list(Fraction(multiple, convert_to_list(m[len(m)-1-n][j])).multiply())
            m[i][j] = Fraction(convert_to_list(m[i][j]), x).subtract()


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(str(m[i][j]), end=" ")
        print()


def convert_to_list(n):
    if type(n) == int:
        lst = [n, 1]
        return lst

    elif type(n) == str:
        div_list = []
        num = ""
        for i in n:
            if i != "/":
                num += i
            else:
                div_list.append(int(num))
                num = ""
        div_list.append(int(num))
        return div_list


def main():
    from string import ascii_lowercase
    m = file_input()

    print("\nfirst triangle:\n")

    for i in range(len(m)-1):
        rearrange_lower_triangle(m, i)
        finish_column_lower_triangle(m, i)
    rearrange_lower_triangle(m, len(m)-1)
    print_matrix(m)

    print("\nsecond triangle:\n")

    for i in range(len(m)):
        finish_column_upper_triangle(m, i)
    print_matrix(m)

    print("\nSolution:\n")

    l = list(ascii_lowercase)
    for i in (range(len(m))):
        print("{} = {}".format(l[i], m[i][len(m[0])-1]))


if __name__ == '__main__':
    main()
