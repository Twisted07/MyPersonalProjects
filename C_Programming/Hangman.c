#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main (void)
{
	srand(time(NULL));

	char guessWords[][16] = {
		"twisted",
		"laptop",
		"windows",
		"linux",
		"machine",
		"lamp",
		"hangman"
	};

	int randomIndex = rand() % 7;
	int loopIndex = 0;
	int numLives = 7;
	int numCorrect = 0;
	int oldCorrect = 0;

	int lengthOfWord = strlen(guessWords[randomIndex]);
	int letterGuessed[8] = {0, 0, 0, 0, 0, 0, 0, 0};

	int quit = 0;
	char guess[16];
	char letterEntered;

	while (numCorrect < lengthOfWord)
	{
		printf("Number of correct guess letters: %d\n", numCorrect);
		printf("\nEnter a guess letter: ");
		fgets(guess, 16, stdin);

		if (strncmp(guess, "quit", 4) == 0)
		{
			quit = 1;
			break;
		}

		letterEntered = guess[0];

		printf("Letter guessed is %c\n", letterEntered);

		for (loopIndex = 0; loopIndex < lengthOfWord; loopIndex++)
		{
			if (letterGuessed[loopIndex] == 1)
			{
				continue;
			}

			if (letterEntered == guessWords[randomIndex][loopIndex])
			{
				letterGuessed[loopIndex] = 1;
				numCorrect++;
			}
		}

	}

	if (numCorrect == lengthOfWord)
	{
		printf("\n\nBravo! Great job. The guess word is %s\n\n", guessWords[randomIndex]);
	}

	if (quit == 1)
	{
		printf("\nYou quit :(\n");
	}
	return 0;
}
