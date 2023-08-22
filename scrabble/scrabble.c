// Code created by Pepijn Weitzel on 22/8/2023
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
        printf("1 = %i   2 = %i\n", score1, score2);
    }
    if (score1 == score2)
    {
        printf("Tie!\n");
        printf("1 = %i   2 = %i\n", score1, score2);
    }
    if (score1 < score2)
    {
        printf("Player 2 wins!\n");
        printf("1 = %i   2 = %i\n", score1, score2);
    }
}

int compute_score(string word)
{
    int length = strlen(word);
    int i = 0;
    int score = 0;

    // Iterate through every letter in the string given and calculate its score
    for (i = 0; i <= length; i++)
    {
        if (isupper(word[i]))
        {
            word[i] = tolower(word[i]);
            int ascii_value = word[i];
            if (ascii_value >= 97 && ascii_value <= 122)
            {
                int x = ascii_value - 97;
                score += POINTS[x];
            }
        }
    }
    return score;
}