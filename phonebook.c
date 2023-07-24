#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int age = get_int("enter your age: ");

    printf("You are %i years old\n", age);
}