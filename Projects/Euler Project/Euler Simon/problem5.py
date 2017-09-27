

def semi_brute():
    for j in range(2520, 20**7, 20):
        # wtf are those magnitudes
        count = 0
        for i in range(11, 21):
            if j % i == 0:
                count += 1
        if count == 10:
            return j


def opt_semi_brute():
    for n in range(2520, 20**7, 2520):
        # all(); basically what i was searching for
        if all((n % j == 0) for j in range(11, 21)):
            return n


def main():
    # hiring smart solutions
    pass


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = opt_semi_brute()
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
