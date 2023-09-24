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
}
node;

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
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // Create a value based on the first 2 letters of the word ('aa' being 0, 'ba' being 26, 'bc' being 28)
    int value = 0;
    value = toupper(word[0]) - 'A';
    value = value * 26 + toupper(word[1]) - 'A';
    if (value >= 675)
    {
        return value % 676;
    }
    return value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open the file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not find file\n");
        return false;
    }
    char bufferword[N+1];
    while(fscanf(file, "%s", bufferword) != EOF)
    {
        // Create space for the new node and check whether there is enough space
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            printf("Not enough memory to use malloc\n");
            return false;
        }

        // Copy the word into the node
        strcpy(n->word, bufferword);

        // Get the hash value to insert the node and insert the node at the location
        int hash_value = hash(bufferword);
        n->next = table[hash_value];
        table[hash_value] = n;
        number_words++;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
