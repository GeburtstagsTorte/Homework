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

# > making small triplets and building the sum then searching the path with the greatest sum


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


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


def main():
    m = get_triangle()
    print(search_path_trivial(m))

if __name__ == '__main__':
    main()
