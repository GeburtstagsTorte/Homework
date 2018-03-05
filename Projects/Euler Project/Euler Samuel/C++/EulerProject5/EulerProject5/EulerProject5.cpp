// EulerProject5.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>


int findNum() {
	int n = 1;

	for (int i = 1; i < 21; i++) {
		if (n % i != 0) {
			for (int j = 1; j < 21; j++) {
				if (n*j % i == 0) {
					n *= j;
					break;
				}
			}
		}
	}
	return n;
}


int main()
{
	std::cout << findNum() << std::endl;
	system("pause");
    return 0;
}

