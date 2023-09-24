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
    // Create the hash value of the word
    int value = hash(word);
    // Iterate through the linked list at the given index to compare the word with each node
    for (node *ptr = table[value]; ptr != NULL; ptr = ptr->next)
    {
        if(strcasecmp(word, ptr->word) == 0)
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
        if(n == NULL)
        {
            printf("Not enough memory to malloc\n");
            fclose(file);
            return false;
        }

        // Put the word in the newly made node
        strcpy(n->word, bufferword);

        // Get the index for the node
        int index = hash(bufferword);

        // Add node to the linked list in the table
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
        number_words++;
    }
    fclose(file);
    return true;















    // Open the file
    //FILE *file = fopen(dictionary, "r");
    //if (file == NULL)
    //{
    //    printf("Could not find file\n");
    //    fclose(file);
    //    return false;
    //}
    //char *bufferword = malloc(LENGTH + 1);
    //if (bufferword == NULL)
    //{
    //    free(bufferword);
    //    return false;
    //}
    //while(fscanf(file, "%s", bufferword) != EOF)
    //{
        // Create space for the new node and check whether there is enough space
    //    node *n = malloc(sizeof(node));
    //    if (n == NULL)
    //    {
    //        printf("Not enough memory to use malloc\n");
    //        fclose(file);
    //        return false;
    //    }

        // Copy the word into the node
    //    strcpy(n->word, bufferword);

        // Get the hash value to insert the node and insert the node at the location
    //    int hash_value = hash(bufferword);

    //    if (table[hash_value] == NULL)
    //    {
    //        n->next = NULL;
    //        table[hash_value] = n;
    //    }
    //    else
    //    {
    //        n->next = table[hash_value];
    //        table[hash_value] = n;
    //    }
    //    number_words++;
    //}
    //fclose(file);
    //free(bufferword);
    //return true;
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
    for (int i = 0; i <= N; i++)
    {
        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *temp = ptr->next;
            free(ptr);
            ptr = temp;
        }
    }
    return false;
}
