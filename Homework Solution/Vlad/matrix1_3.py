m = open("matrix3").read().splitlines()
m = [[int(i) for i in j.split()] + [-1] for j in m]
m = [[[m[i][j], int(['', str(m[i][j-1])][j-1 >= 0] + str(m[i][j]) + ['', str(m[i][j+1])][j+1 < len(m[0])-1])][(i+j)%2 != 0] for j in range(len(m[0])-1)] for i in range(len(m))]
print(''.join([str([m[i][j] for j in range(len(m[0]))]) + "{0}" for i in range(len(m))]).format("\n"))
