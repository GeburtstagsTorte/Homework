a = open("file2_2").read().splitlines()[0].split(" ")
for i in range(len(a)-1):
    if int(a[i+1]) % sum([int(x) for x in a[i]]) == 0 or int(a[i]) % sum([int(x) for x in a[i+1]]) == 0:
        print('(' + a[i] + ',' + a[i+1] + ')', end=" ")