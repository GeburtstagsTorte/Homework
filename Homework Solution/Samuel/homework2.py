# homework 2_2; task: homework2 text.txt D:\


def take_input_v1():

    with open("homework2_2 text", "r") as f:
        s = f.read()
        lst = [int(x) for x in s.split(", ") if x.isdigit()]

        # It does pretty much the same as your version but I'm not happy with both of them because they can only
        # handle series of numbers in certain circumstances. It will already break by series like
        # 17, 16, 14, 8, 5; 23

    return lst


def take_input_v2():
    with open("homework2_2 text", "r") as f:
        nums = []
        cani = ""
        # cani is the abbreviation for candidate, pyCharm. God damn it!
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

        try:
            cani = int(cani)
            nums.append(sign * int(cani))
        except ValueError:
            pass
        # uncool, but otherwise the last value wouldn't be considered.

    # I'm not happy with this version either since you can argue about what a number is in a bunch of text.
    # This function also consider the algebraic sign. I don't know if you wanted it like this..

    return nums


def pairs(lst):
    p = []

    for i in range(len(lst)-1):
        if lst[i] % sum(int(x) for x in str(lst[i+1])) == 0 or \
                lst[i+1] % sum(int(x) for x in str(lst[i])) == 0:

            # It is quite a lot for an if statement, i know, but this is just too simple to put it in an extra function
            # sorry, master! m(_ _)m

            p.append((lst[i], lst[i+1]))

    return p


def main():
    u = take_input_v1()
    print(pairs(u))

    v = take_input_v2()
    print(pairs(v))


if __name__ == "__main__":
    main()
# Could you explain this a bit more? I don't really understand what this does..

