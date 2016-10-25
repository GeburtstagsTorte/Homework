a = list(map(int, input("nrs = ").split(" ")))
b = [[i for i in range(1, a[j]+1) if a[j] % i == 0] for j in range(len(a))]
for i in range(len(b)):
    fin = fin & set(b[i]) if i > 0 else set(b[0])
print(fin)