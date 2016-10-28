def is_prime(x):
    return False if 0 in [(x % i) for i in range(2, x//2+1)] else True
n = int(input("n="))
print([i for i in range(10**(n-1), 10**n) if is_prime(i) and is_prime(i//10)])
