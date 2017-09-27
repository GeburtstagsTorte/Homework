

def main():
    sum_of_the_squares = 0
    square_of_the_sum = 0
    for i in range(1, 101):
        sum_of_the_squares += i**2
        square_of_the_sum += i

    return square_of_the_sum**2 - sum_of_the_squares


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = main()
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
