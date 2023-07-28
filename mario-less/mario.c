#include <cs50.h>
#include <stdio.h>

int main(void)
{
    do
    {
        int height = get_int("Height: \n");
    }
    while (height >= 1 && height <= 8);

    printf("%i\n", height);
}