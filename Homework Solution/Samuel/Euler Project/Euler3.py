from math import sqrt

primes = [2]
candidate = 3
num = 600851475143

while candidate < sqrt(num):
    for x in primes:
        if candidate % x == 0:
            candidate += 2
            break

    else:
        primes.append(candidate)
        if num % candidate == 0:
            #print(candidate)
            num = num / candidate
print(num)


    

        
