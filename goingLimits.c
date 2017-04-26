#include <math.h>
#include <stdio.h>
/*
	Calculate (1 / n!) * (1! + 2! + 3! + ... + n!) for a given n. Call this function "going(n)" where n is an integer greater or equal to 1.

To avoid discussions about rounding, if the result of the calculation is designed by "result", going(n) will return "result" truncated to 6 decimal places.

*/

long double factorial(int n) {
	long double fac = 1;
	for (int i = 1; i <= n; i++)
		fac *= i;
	printf("fact: %Lf\n", fac);
	return fac;
}

long double factorial(int n, int low) {
	long double fac = 1;
	for (int i = low; i <= n; i++)
		fac *= i;
	return fac;
}

double going(int n) {
	//printf("N: %d\n", n);
	long double sum = 0;
	for (int i = 1; i <= n; i++)
		sum += factorial(i);
	printf("%Lf\n", sum);
	return (double)(sum / factorial(n) * 1000000)/1000000;
}

int main()
{
	printf("%f\n", going(1000));
	return 0;
}
