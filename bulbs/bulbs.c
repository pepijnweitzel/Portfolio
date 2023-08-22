#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;


void print_bulb(int bit);

int main(void)
{
    char message = get_char("Char: ");
    int binary[BITS_IN_BYTE];
    int x = message;

    for (int i = (BITS_IN_BYTE - 1); i >= 0; i--)
    {
        if (x % 2 == 1)
        {
            binary[i] = 1;
        }
        x = x / 2;
    }

    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        printf("%i", binary[i]);
    }
    printf("\n");

}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
