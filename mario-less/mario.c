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
    while (height > 0)
    {
        int i = height - (height -1)
    }
}