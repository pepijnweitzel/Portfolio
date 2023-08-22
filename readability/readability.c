#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

//    index = 0.0588 * L - 0.296 * S - 15.8
//   L: Number of letters per 100 words >> L = letters / words * 100
//   S: Number of sentences per 100 words >> S = sentences / words * 100
int main(void)
{
    // Prompt for the text
    string text = get_string("Text: ");

    // Declare and calculate all variables
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Calculate last 2 variables for Coleman-Liau index
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    // Calculate the index via the Coleman-Liau index
    float index = 0.0588 * L - 0.296 * S - 15.8;


    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before grade 1\n");
    }
    else
    {
        index = round(index);
        printf("Grade %i\n", (int)index);
    }
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