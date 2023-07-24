#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int age = get_int("enter your age: ");
    string name = get_string("enter your name: ");
    string number = get_string("enter your phone number: ");

    printf("%s is %i years old and is reachable on: %s\n", name, age, number);
}