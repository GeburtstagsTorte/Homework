# https://projecteuler.net/problem=18
# Find the maximum total from top to bottom of the triangle below
# moving to adjacent numbers on the row below
# euler18.txt, triangle
# here are only 16384 routes, still no brute force!
# Euler67: 633825300114114700748351602688 routes


def get_triangle():
    m = open("euler67").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]
    return m


"""def get_triangle_value(m, pos):
    # gets the sum of every number which is possible to reach when you choose pos
    count = m[pos[0]][pos[1]]
    a = pos[1]+1
    for i in range(pos[0]+1, len(m)):
        a += 1
        for j in m[i][pos[1]:a]:
            count += j
            print(pos, j)
    return count


def generate_path_sum(m):
    # flaw must be in this function
    total = m[0][0]
    current_pos = (0, 0)
    l = [m[0][0]]
    # l for debugging
    for i in range(1, len(m)):
        choice0 = get_triangle_value(m, (i, current_pos[1]))
        choice1 = get_triangle_value(m, (i, current_pos[1] + 1))
        if choice0 > choice1:
            if i != len(m)-1:
                l.append(m[i][current_pos[1]])
                total += m[i][current_pos[1]]
                current_pos = (i, current_pos[1])
            else:
                l.append(choice0)
                total += choice0

        else:
            if i != len(m)-1:
                l.append(m[i][current_pos[1] + 1])
                total += m[i][current_pos[1] + 1]
                current_pos = (i, current_pos[1] + 1)
            else:
                l.append(choice1)
                total += choice1
    return total, l


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()
"""


def generate_path_sum(m):
    for i in range(len(m)-1)[::-1]:
        for j in range(len(m[i])):
            # not sure if max() is the most efficient method
            m[i][j] += max(m[i+1][j], m[i+1][j+1])
    return m[0][0]


def main():
    m = get_triangle()
    print(generate_path_sum(m))

if __name__ == '__main__':
    main()
