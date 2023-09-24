// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 676;

// Hash table
node *table[N];

// Global variable for number of words
int number_words = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Create the hash value of the word
    int value = hash(word);
    // Iterate through the linked list at the given index to compare the word with each node
    for (node *ptr = table[value]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // Create a value based on the first 2 letters of the word ('aa' being 0, 'ba' being 26, 'bc' being 28)
    if (strlen(word) < 3)
    {
        return toupper(word[0] - 'A');
    }
    int value = 0;
    value = toupper(word[0]) - 'A';
    value = value * 26 + toupper(word[1]) - 'A';
    if (value >= 675)
    {
        return 0;
    }
    return value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open the dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char bufferword[LENGTH + 1];

    // Create new nodes and put them in the hash table
    while (fscanf(file, "%s", bufferword) != EOF)
    {
        // Create and check new node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Not enough memory to malloc\n");
            fclose(file);
            return false;
        }

        // Put the word in the newly made node
        strcpy(n->word, bufferword);

        // Get the index for the node
        int index = hash(bufferword);

        // Add node to the linked list in the table while checking whether its the first item to set pointers correctly
        if (table[index] == NULL)
        {
            table[index] = n;
            n->next = NULL;
        }
        else
        {
            n->next = table[index];
            table[index] = n;
        }
        // Increase the number_words variable by 1 for every word added to the hash table
        number_words++;
    }
    // Close the opened file for no memory errors
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return number_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Iterate through the entire array
    for (int i = 0; i < N; i++)
    {
        // Create a temporary pointer which will be used to free all the nodes while iterating through the linked list
        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *temp = ptr->next;
            free(ptr);
            ptr = temp;
        }
    }
    return true;
}
