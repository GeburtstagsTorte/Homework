# What is the sum of the digits of the number 2**1000?
num = str(2**1000)
c = 0
for i in num:
    c += int(i)
print(c)
