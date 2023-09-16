// Code created by Pepijn Weitzel on 9/9/2023
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check for invalid usage:
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("Cannot open image for reading\n");
        return 1;
    }

    // Count the number of images found to name the images correctly:
    int images_count = 0;

    // Make the buffer which stores 512 bytes:
    typedef uint8_t BYTE;
    int BLOCK_SIZE = 512;
    BYTE buffer[BLOCK_SIZE];


    char *name_of_file = malloc(8 * sizeof(char));

    FILE *image_file = NULL;

    while (fread(buffer, sizeof(char), BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        // Check whether first 4 bytes match given signature:
        if (buffer[0] == 0xff)
        {
            if (buffer[1] == 0xd8)
            {
                if (buffer[2] == 0xff)
                {
                    if (buffer[3] >= 224 && buffer[3] <= 239)
                    {
                        // Make a sprintf() to create the name of the image file
                        sprintf(name_of_file, "%03i.jpg", images_count);

                        image_file = fopen(name_of_file, "a");

                        images_count++;
                    }
                }
            }
        }

        if (image_file != NULL)
        {
            fwrite(buffer, sizeof(char), BLOCK_SIZE, image_file);
        }
    }

    // Close and free everything for no memory errors
    fclose(file);
    fclose(image_file);
    free(name_of_file);

    return 0;
}