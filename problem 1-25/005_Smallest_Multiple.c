/*
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

#include <stdio.h>

int is_multiple(long long x, int n)
{
	int i; 
	
    for (i = 1; i <= n; i++) {
        if (x % i != 0)
            return 0;
    }
    return 1;
}

int main(void)
{
    int n = 20;
    long long i = n;
    
    while (1) {
        if (is_multiple(i, n)) {
            printf("%lld\n", i);
            return 0;
        }
        i += n;  
    }
}
