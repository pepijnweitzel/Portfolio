#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

int binary_array(int value);
void print_bulb(int bit);

int main(void)
{
    char message = get_char("Char: ");

    int z = binary_array(message);

    for (int i = 0; i < BITS_IN_BYTE; i++)
    {
        printf("%i", z[i]);
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

int binary_array(int value)
{
    int binary[BITS_IN_BINARY];

    for (int i = (BITS_IN_BYTE - 1); i >= 0; i--)
    {
        if (value % 2 == 1)
        {
            binary[i] = 1;
        }
        value = value / 2;
    }

    return binary
}