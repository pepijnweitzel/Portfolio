// Code created by Pepijn Weitzel at 27/7/2023
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for users name:
    char name = get_char("What is your letter? \n");
    // Greet user by their name:
    printf("Hello, %c\n", name);
    printf("%i", name);
}