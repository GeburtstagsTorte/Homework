#include "stdafx.h"
#include <iostream>


int calculateMultiples(int n) {
	int count = 0; 
	int num = 0; 
	
	while (num < n) {
		if (num % 3 == 0 || num % 5 == 0) {
			count += num; 
		}
		num++;
	}
	
	return count;
}


/*int main()
{
	int n = 1000;
	std::cout << calculateMultiples(n);
	system("pause");
    return 0;
}*/

