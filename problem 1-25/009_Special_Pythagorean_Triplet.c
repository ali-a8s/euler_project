/*
There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc
a < b < c ==> a**2 + b**2 = c**2
*/

#include <stdio.h>

int main()
{
    int a, b, c;

    for (a = 1; a <= 1000; a++){
        for (b = 1; b <= 1000; b++){
            for (c = 1; c <= 1000; c++){
                if ((a < b && b < c) && (a + b + c == 1000) && (a*a + b*b == c*c)) {
                    int result = a * b * c;
                    printf("%d * %d * %d = %d\n", a, b, c, result);
                    break;
                }
            }
        }
    }
    return 0;
}
