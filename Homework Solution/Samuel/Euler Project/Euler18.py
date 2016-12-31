# Find the maximum total from top to bottom of the triangle below
# moving to adjacent numbers on the row below
# euler18.txt, triangle
# here are only 16384 routes, still no brute force!

# characteristics:
# numbers between 1 - 99

# ideas:
# > eliminating small numbers and search a path through the numbers left
# -> eliminate numbers until only one path is left ..

# > going backwards

# > figure out, where the biggest numbers are, then try to find a connection between them with other big numbers

# > making triplets and building the sum then searching the path with the greatest sum <


def get_triangle():
    m = open("euler18").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]
    return m


def search_path_trivial(m):
    # trivial attempt to solve this. It doesn't work, obviously, since it is not even brute force
    # but just to understand it a bit further

    l = [m[0][0]]
    count = m[0][0]
    current_position = (0, 0)
    for i in range(1, len(m)):
        if m[i][current_position[1]] > m[i][current_position[1] + 1]:
            count += m[i][current_position[1]]
            l.append(m[i][current_position[1]])
            print("choose: {}, pos = {}".format(m[i][current_position[1]], current_position))
            current_position = (i, current_position[1])
        else:
            count += m[i][current_position[1] + 1]
            l.append(m[i][current_position[1] + 1])
            print("choose: {}, pos = {}".format(m[i][current_position[1] + 1], current_position))
            current_position = (i, current_position[1] + 1)
    return count, l


def get_triangle_value(m, pos):
    # gets the sum of every number which is possible to reach when you choose pos
    count = m[pos[0]][pos[1]]
    a = pos[1]+1
    for i in range(pos[0]+1, len(m)):
        a += 1
        for j in m[i][pos[1]:a]:
            count += j
    return count


def generate_path_sum(m):
    total = m[0][0]
    current_pos = [0, 0]
    l = [m[0][0]]
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


def main():
    m = get_triangle()
    print(generate_path_sum(m))
if __name__ == '__main__':
    main()
