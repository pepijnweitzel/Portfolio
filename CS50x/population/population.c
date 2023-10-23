// Code created by Pepijn Weitzel on 26/7/2023
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    // Prompt for end size
    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    // Calculate number of years until we reach threshold
    int years = 0;

    while (start < end)
    {
        int i = start;
        int gain = i / 3;
        int lose = i / 4;
        start += gain - lose;
        years++;
    }
    // Print number of years
    printf("Years: %i\n", years);
}