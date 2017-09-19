def test():
    num = 2520
    divisible = True
    for x in range(1, 11):
        if num % x != 0:
            divisible = False
            print("%d is not fully divisible" % num)
            break
    if divisible:
        print("%d is fully divisible" % num)


def euler5():
    from time import clock

    time1 = clock()
    divisible = False
    x = 200
    while not divisible:
        for div in range(1, 21):
            if x % div != 0:
                # optimize selection process
                x += 10
                break
        else:
            divisible = True
            print("Your number is ", x)
            time2 = clock()
    print(time2-time1, "s")


def euler5_solution():
    from time import clock
    time1 = clock()
    x = 1
    for i in range(1, 21):
        if x % i != 0:
            for j in range(1, 21):
                if x*j % i == 0:
                    x *= j
                    time2 = clock()
                    break
    print(x)
    print(time2-time1, "s")

euler5_solution()