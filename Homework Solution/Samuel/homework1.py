# vlad homework 1; task: homework1 text.txt :D\


def intro():
    # input func exercise 1
    # returns all input numbers as int in list

    i = input("Your numbers: ")
    num = ""
    numbers = []
    for char in i:
        try:
            num += str(int(char))

        except ValueError:
            if len(num) > 0:
                numbers.append(int(num))
                num = ""
            pass
    numbers.append(int(num))
    return numbers


def common_divisors(numbers):
    # func exercise 1
    # prints as the name says all common divisors of given numbers (from intro())

    divisors = []

    for i in range(1, min(numbers) + 1):
        for j in numbers:
            if j % i != 0:
                break
        else:
            if i not in divisors:
                divisors.append(i)

    print(divisors)


def intro_exercise2():
    # input func exercise 2
    # returns k as int

    k = input("Your number: ")
    try:
        k = int(k)

    except ValueError:
        pass

    return k


def exercise2(k):
    # func exercise 2
    # prints x, y integers, where x^2 + y^2 = k

    for x in range(1, k//2):
        for y in range(x, k//2):
            if x**2 + y**2 == k:
                print("%d^2 + %d^2 = %d" % x, y, k)


def intro_exercise3():
    # input func exercise 3
    # returns list with numbers from file with algebraic sign

    with open("homework1 ex3.txt", "r") as f:
        nums = []
        cani = ""
        sign = 1
        s = f.read()
        for char in s:
            try:
                cani += str(int(char))

            except ValueError:
                if len(cani) > 0:
                    nums.append(sign * int(cani))
                if char != "-":
                    sign = 1
                    cani = ""
                else:
                    sign = -1
                pass
        # uncool
        try:
            cani = int(cani)
            nums.append(sign * int(cani))
        except ValueError:
            pass

    return nums


def exercise3(nums):
    # func exercise 3

    count = 0
    for i in nums:
        if i < 0:
            count += 1
    if count > len(nums)//2:
        return -1
    elif count == len(nums)//2:
        return 0
    else:
        return 1
    # print("count: ", count)


def main():

    x = intro_exercise3()
    print(exercise3(x))

if __name__ == "__main__":
    main()
