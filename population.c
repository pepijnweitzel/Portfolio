#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int start;
    do
    {
        start = get_int("What is the starting population of lama's? \n");

    }
    while (start < 9);

    int goal
    do
    {
        goal = get_int("What is the goal population of lama's? \n");
    }
    while (goal < start);



    //every year n/3 get born and n/4 die

    int y = 0;
    while (start < goal)
    {
        int n = start;
        int b = n/3;
        int p = n/4;
        start = start + b - p;
        y += 1;
    }

    printf("It took %i years to reach a population of %i lama's \n", y, goal);



}