n = int(input("n = "))
print([i for i in range(1, n) for j in range(i) if (i-1)*i/2 + j < n])
