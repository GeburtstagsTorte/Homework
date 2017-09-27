

def main():
    largest = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            string = str(i*j)
            if len(string) < 6:
                return largest
            if string[:len(string)//2] == string[len(string):len(string)//2-1:-1]:
                competitor = int(string)
                if competitor > largest:
                    largest = competitor


if __name__ == '__main__':
    from time import time
    t1 = time()
    result = main()
    t2 = time()
    exit("Result: " + str(result) + "\nTime: " + str((t2 - t1) * 1000))
