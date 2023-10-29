# Code created by Pepijn Weitzel
import pygame



def main():
    # initialize pygame
    pygame.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = int((0.8 * SCREEN_WIDTH))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
