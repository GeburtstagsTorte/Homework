#include "stdafx.h"
#include <iostream>

bool *primeSieve() {
	const int limit = 775147;
	
	bool sieve[limit] = {};
	sieve[0] = 1;
	sieve[1] = 1;

	for (int i = 2; i < (int)pow(limit, 0.5) + 1; i++) {
		for (int j = i + 1; j < limit; j++) {
			if (j % i == 0) {
				sieve[j] = 1;
			}
		}
	}
	return sieve;
}


int main(){
	/*
	the whole approach is ineffective as fuck but who cares, i don't know yet how to use dynamic arrays. 
	a better algorithm can be found in the python eulerProject folder.
	*/
	
	bool *primes = primeSieve();
	// how to return arrays in a function (returning the pointer of the array)
	// https://www.tutorialspoint.com/cplusplus/cpp_return_arrays_from_functions.htm
	int largestPrimefactor = 0;
	long long int num = 600851475143;

	for (int i = 0; i < 775147; i++) {
		if (primes[i] == 0) {
			//std::cout << i << std::endl;
			if (num == 1) {
				break;
			}
			if (num % i == 0) {
				//std::cout << i << std::endl;
				num = num / i;
				largestPrimefactor = i;
			}

		}
	}
	std::cout << largestPrimefactor << std::endl;
	system("pause");
    return 0;
}

