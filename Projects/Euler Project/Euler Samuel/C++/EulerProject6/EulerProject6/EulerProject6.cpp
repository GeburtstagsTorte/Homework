// EulerProject6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>


int sumOfSquares(int n) {
	unsigned long long int sum = (int)(n*(n + 1)*(2 * n + 1)) / 6;
	return sum;
}

int sumSquared(int n) {
	unsigned long long int sum = (int)pow(0.5*n*(n + 1), 2.0);
	return sum;
}

int main()
{

	std::cout << std::abs(sumOfSquares(100) - sumSquared(100)) << std::endl;
	system("pause");
    return 0;
}

