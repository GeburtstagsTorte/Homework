def open_matrix():

    m = open("matrix4").read().splitlines()
    m = [[int(i) for i in j.split()] for j in m]

    return m


def first(m):

    lst = []
    for k in range(0, len(m[0]), 2):
        lst3 = []
        for i in range(len(m)):
            for j in range(k, 2+k):
                try:
                    lst3.append(int(m[i][j]))
                except IndexError:
                    pass
        lst.append(lst3)
    print("lst", lst, "\n")

    for p in range(len(lst)):
        lst2 = []
        if p % 2 == 0:
            for ö in lst[p]:
                lst2.append(lst[p][0:1])
                for ü in range(3, len(lst[p]), 4):
                    lst2.append(lst[p][ü:ü+2])
            print(list(lst2[:len(lst[p])//3]))
        else:
            for ä in lst[p]:
                for n in range(1, len(lst[p]), 4):
                    lst2.append(lst[p][n:n+2])
            print(list(lst2[:len(lst[p])//3]))

# solved but ugly af ... i am ashamed


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


def main():
    m = open_matrix()
    first(m)
    print()
    print_matrix(m)

if __name__ == '__main__':
    main()
