#include <stdio.h>

//lets display fibonacci series

	int fib(int i) {
	if (i == 0) {
		return (0);
		}
	if (i == 1) {
		return (1);
		}
	return (fib (i-1) + fib (i-2));
	}

	int main()
{
	int i;
	for (i = 0; i < 20; i++) {
		printf ("%d\t\n", fib (i));
	}
	return (0);
}
