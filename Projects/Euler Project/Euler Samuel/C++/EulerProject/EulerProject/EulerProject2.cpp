#include "stdafx.h"
#include <iostream>

int getFibonacci(int n) {
	if (n == 0 || n == 1) {
		return n;
	}
	else {
		return getFibonacci(n - 1) + getFibonacci(n - 2);
	}
}


int main() {
	int count = 0;
	int n = 0;
	int val = getFibonacci(n);

	while (val < 4000000) {
		if (val % 2 == 0) {
			count += val;
		}
		n++;
		val = getFibonacci(n);
	};
	std::cout << count << std::endl;

	system("pause");
}