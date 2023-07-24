#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int start = get_int("What is the starting population of lama's? \n");
    int goal = get_int("What is the goal population of lama's? \n");

    printf("%i %i\n", start, goal);
}