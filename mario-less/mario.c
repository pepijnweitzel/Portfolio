#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for height
    int height;
    do
    {
        height = get_int("Height: ");
    }

    while (height < 1 || height > 8);

    // Make the pyramid

    int space = height - 1;
    int hash = height - space;
    int a;
    int b;

    while (hash <= height)
    {
        a = space;
        b = hash;
        //print 3 times space and 1 time hash
        while (a > 0)
        {
            printf(" ");
            a--;
        }
        while (b > 0)
        {
            printf("#");
            b--;
        }
        printf("\n");
        space--;
        hash++;
    }

}