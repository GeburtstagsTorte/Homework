m = open("matrix1").read().splitlines()
m = [[int(i) for i in j.split()] for j in m]
print("First quarter: ", [m[i][j] for i in range(len(m)//2) for j in range(len(m) // 2)])
print("Second quarter: ", [m[i][j] for i in range(len(m)//2) for j in range(len(m) // 2, len(m))])
print("Third quarter: ", [m[i][j] for i in range(len(m)//2, len(m)) for j in range(len(m) // 2)])
print("Fourth quarter: ", [m[i][j] for i in range(len(m)//2, len(m)) for j in range(len(m) // 2, len(m))])
# Print matrix
print(''.join([str(m[i]) + "{0}" for i in range(len(m))]).format("\n"))
