def euler4():

    # I created a local function, that can be accessed after I finish declaring it
    def palindrome(x):
        # I convert x to a string so I can reverse it easier
        # (To reverse stuff easier I need a list and strings act like lists)
        x = str(x)
        # x[::-1] is the reverse of the string
        # Now I compare the string to its reverse. If it's the same, then it's a palindrome
        if x == x[::-1]:
            return True
        else:
            return False

    # Here is a list to hold the biggest palindrome and its members
    # max_pal[0] is the holder for the largest palindrome and max_pal[1] and max_pal[2] are its members
    max_pal = [0, 0, 0]
    # By range(999, 900, -1), it goes from 999 to 901, because the step is -1
    # And by for in for I combine every 2 3-digit number from 999 to 901
    # It will go like this:
    """
        i  | j
        999|999
        999|998 ->||
        999|997   ||
        .......   ||
        999|901   \/
        998|999 -> here the same patter repeats, which is not optimised
        998|998         -to fix this, replace the seconde for with: for j in range(i, 901, -1)
        .......
        901|901
    """
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            # I check if the product is a palindrome
            if palindrome(i*j):
                # If the product is a palindrome I will compare it to the previous biggest palindrome
                # That's why I initialised max_pal with [0, 0, 0]
                # So the fast palindrome found will get recognised, because it will be bigger than 0
                if i*j > max_pal[0]:
                    max_pal = [i*j, i, j]
                    # Saving in max_pal the NEW largest palindrome
                    # By doing this, we'll not save palindromes who are smaller than the biggest found at that time
                    # We'll do this saving so we'll always have the biggest palindrome up to that point

    # Also, started from 999 and 999, because fewer stuff will have to compute
    # Bigger numbers result in bigger palindromes and we are searching for that
    print("The biggest palindrome is: ", max_pal[0], " composed of ", max_pal[1], " and ", max_pal[2])
    # I did this long print so it can be easily converted to 3.5.2
    # Otherwise, there are formatting options

euler4()
