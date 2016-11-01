m = open("matrix3").read().splitlines()
m = [[int(i) for i in j.split()] for j in m]
m = [[m[i][j] for j in range(len(m[0]))] for i in range(len(m))]
print(''.join([str(m[i]) + "{0}" for i in range(len(m))]).format("\n"))
