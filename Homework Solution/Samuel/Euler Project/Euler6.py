def euler6():
    from time import clock
    sum_squares = 0
    n = 100
    time1 = clock()

    # optimize sum_squares
    for i in range(1, 101):
        sum_squares += i**2

    print((n*(n+1)/2)**2-sum_squares)
    time2 = clock()
    print(time2-time1, "s")

euler6()




