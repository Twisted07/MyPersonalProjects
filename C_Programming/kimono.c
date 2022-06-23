#include <stdio.h>
int main()
{
int i;
char Yes;
char No;
char answer;

	do {
	printf("Should I print all the 2 letter words in my memory? ");
	scanf("%c", &answer);
	}
	while (answer == Yes);{
		for (i=0; i < 100000000; i++)
			printf("%d", i);
	}
 	if (answer == No){
			printf("Okay\n");

	}


	return (0);
}
