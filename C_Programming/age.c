#include <stdio.h>

int main()
{
	int age;

	printf("What is your age?: ");
	scanf("%d", &age);

	if (age < 50) {
		printf("You are young!\n");
	}
	else if (age ==50) {
		printf("You are golden!\n");
	}
	else {
		printf("Prepare for death!\n");
	}
	return (0);
}
