k = int(input("k = "))
print([(i, j) for i in range(1, k // 2) for j in range(i+1, k // 2) if i**2 + j**2 == k])
