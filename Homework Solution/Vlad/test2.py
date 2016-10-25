x, y, a = int(input("x = ")), int(input("y = ")), list(map(int, open("test2").read().splitlines()[0].split(" ")))
print(list(filter(lambda m: x < m < y, a))[::-1])
