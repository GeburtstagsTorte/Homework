// EulerProject4.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <string>

int findPalindrome() {
	
	int candidate = -1; // -1 for debug purposes 
	
	for (int i = 999; i > 900; i--) {
		for (int j = i; j > 900; j--) {
			
			int p = i * j;
			
			std::string num = std::to_string(p);
			std::string copy = num;
			std::reverse(copy.begin(), copy.end());

			if (num == copy) {
				if (p > candidate) {
					candidate = p;
				}

			}
		}
	}
	return candidate;
}

int main()
{
	std::cout << findPalindrome() << std::endl;
	system("pause");
    return 0;
}

