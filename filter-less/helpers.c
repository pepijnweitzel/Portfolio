// Code created by Pepijn Weitzel on 7/9/2023
#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            int new_value = round(average / 3.0);
            image[i][j].rgbtBlue = new_value;
            image[i][j].rgbtGreen = new_value;
            image[i][j].rgbtRed = new_value;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int w = width - 1;
        int h = width / 2;
        for (int j = 0; j < h; j++)
        {
            RGBTRIPLE *a = &image[i][j];
            RGBTRIPLE *b = &image[i][w];
            RGBTRIPLE tmp = *a;
            *a = *b;
            *b = tmp;
            w--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int total_red = 0;
            int total_green = 0;
            int total_blue = 0;
            float x = 0.0;

            for (int i_line = -1; i_line < 2; i_line++)
            {
                for (int j_line = -1; j_line < 2; j_line++)
                {
                    if (i + i_line < 0 || i + i_line > height - 1)
                    {
                        continue;
                    }
                    if (j + j_line < 0 || j + j_line > width - 1)
                    {
                        continue;
                    }

                    x++;
                    total_red += copy[i + i_line][j + j_line].rgbtRed;
                    total_green += copy[i + i_line][j + j_line].rgbtGreen;
                    total_blue += copy[i + i_line][j + j_line].rgbtBlue;
                }
            }

            image[i][j].rgbtRed = round(total_red / x);
            image[i][j].rgbtGreen = round(total_green / x);
            image[i][j].rgbtBlue = round(total_blue / x);
        }
    }
    return;
}
