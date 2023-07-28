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
        // Print a times " ":
        while (a > 0)
        {
            printf(" ");
            a--;
        }
        // Print b times #:
        while (b > 0)
        {
            printf("#");
            b--;
        }
        // Go to next line and update value for a and b:
        printf("\n");
        space--;
        hash++;
    }

}