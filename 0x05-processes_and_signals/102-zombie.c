#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - infinite loop
 * Return: returns 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point of C program
 * Return: returns 1 for failurr or 0 for success
 */
int main(void)
{
	pid_t child;
	int i = 0;

	while (i < 5)
	{
		child = fork();
		if (!child)
			return (1);

		printf("Zombie process created, PID: %d\n", child);
		i++;
	}

	infinite_while();

	return (0);
}
