#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

//    index = 0.0588 * L - 0.296 * S - 15.8
//   L: Number of letters per 100 words
//   S: Number of sentences per 100 words
int main(void)
{
    string text = get_string("Text: ");
    
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
    int number_of_sentences = 0;

    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            number_of_sentences++;
        }
    }
    return number_of_sentences;
}