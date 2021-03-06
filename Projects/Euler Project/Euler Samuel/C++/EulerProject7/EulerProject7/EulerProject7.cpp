// EulerProject7.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>


int nthPrime() {
	const int n = 10001;
	int primes[n]; 
	primes[0] = 2; 
	int j = 1; 
	int next = 3;
	bool isPrime = true;

	while (j < n) {
		for (int i = 0; i < j; i++) {
			if (next % primes[i] == 0) {
				next += 2; 
				isPrime = false; 
				break;
			}
		}
		if (isPrime) {
			primes[j] = next; 
			j++;
			next += 2;
		}
		isPrime = true;
	}
	return primes[n - 1];
}


int main()
{
	std::cout << nthPrime() << std::endl;
	system("pause");
    return 0;
}

