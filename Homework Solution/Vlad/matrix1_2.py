m = open("matrix2").read().splitlines()
m = [[int(i) for i in j.split()] for j in m]
m = [m[i] + [eval('*'.join(str(j) for j in m[i]))] for i in range(len(m))]
m.append([eval('*'.join(str(m[i][j]) for i in range(len(m)))) for j in range(len(m[0]))])
