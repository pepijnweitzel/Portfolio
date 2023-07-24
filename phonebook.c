#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int age = get_int("enter your age: ");
    string name = get_string("enter your name: ");

    printf("Your name is %s \n", name);
    printf("You are %i years old\n", age);
}