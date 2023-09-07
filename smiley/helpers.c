#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            RGBTRIPLE pixel = image[i][j];

            if (image[i][j].rgbtBlue == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtRed == 0x00)
            {
                image[i][j].rgbtRed = 0x03;
                image[i][j].rgbtGreen = 0xF9;
                image[i][j].rgbtBlue = 0xF1;
            }
        }
    }
}
