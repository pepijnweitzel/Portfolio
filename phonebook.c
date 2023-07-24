#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("enter your name: ");

    printf("The name you entered is : %s\n", name);
}