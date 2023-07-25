#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int start = get_int("What is the starting population of lama's? \n");
    int goal = get_int("What is the goal population of lama's? \n");

    //every year n/3 get born and n/4 die
    
    printf("%i %i\n", start, goal);
}