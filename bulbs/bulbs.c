#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;


void print_bulb(int bit);

int main(void)
{
    string message = get_string("Message: ");

    for (int i = 0, len = strlen(message); i < len; i++)
    {
        int binary[BITS] = {0,0,0,0,0,0,0,0};
        for (int j = 7, x = message[i]; j >= 0; j--)
        {
            if (x % 2 == 1)
            {
                binary[j] = 1;
            }
            x = x / 2;
        }
        for (int j = 0; j < 7; j++)
        {
          print_bulb(binary[j]);
        }
        printf("\n");
    }


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
