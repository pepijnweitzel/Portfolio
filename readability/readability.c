#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    printf("%i Letters\n", letters);
}



int count_letters(string text)
{
    int length = strlen(text);
    int number_of_letters = 0;

    for (int i = 0; i < length; i++)
    {
        if (isupper(text[i]))
        {
            number_of_letters++;
        }
        else if (islower(text[i]))
        {
            number_of_letters++;
        }
    }
    return number_of_letters;
}
