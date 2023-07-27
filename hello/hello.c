//Code created by Pepijn Weitzel at 27/7/2023
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Prompt for users name:
    string name = get_string("What is your name? \n");
    //Greet user by their name:
    printf("Hello, %s\n", name);
}