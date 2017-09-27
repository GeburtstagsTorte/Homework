

def main():
    smallest_number = 20

    for j in range(smallest_number**6, smallest_number**7, 20):
        # wtf are those magnitudes
        count = 0
        for i in range(1, 21):
            if j % i == 0:
                count += 1
        if count == 20:
            return j


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = main()
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
