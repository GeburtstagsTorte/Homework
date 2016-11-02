m = open("matrix4").read().splitlines()
m = [[int(i) for i in j.split()] + [-1] for j in m]
print([m[i % len(m)][2*(i//len(m)) + i % 2] for i in range(len(m) * len(m[0]) // 2 - 2)])
