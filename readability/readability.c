#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    printf("%i Letters\n", letters);
    int words = count_words(text);
    printf("%i Words\n", words);
}



int count_letters(string text)
{
    int number_of_letters = 0;

    for (int i = 0, length = strlen(text); i < length; i++)
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

int count_words(string text)
{
    int length = strlen(text);
    int number_of_words = 1;

    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (isspace(text[i]))
        {
            number_of_words++;
        }
    }
    return number_of_words;
}

int count_sentences(string text)
{
    int sentences = 0;

    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if
    }
}