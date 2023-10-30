# Code created by Pepijn Weitzel
import pygame
import random

# Set globals
running = True
lost = False
score = 0


def main():
    # initialize pygame
    pygame.init()
    # Set screen
    SCREEN_WIDTH = 550
    SCREEN_HEIGHT = 950
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set player
    CAR_IMAGE = pygame.image.load("car.png")
    SCALED_CAR_IMAGE = pygame.transform.scale(CAR_IMAGE, (CAR_IMAGE.get_width() / 6, CAR_IMAGE.get_height() / 6))
    car_x = 250
    car_y = 250

    # Background image
    BACKGROUND_IMAGE = pygame.image.load("background.png")
    SCALED_BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (BACKGROUND_IMAGE.get_width() / 3, BACKGROUND_IMAGE.get_height() / 3))

    # Obstacle starting setup
    obstacle = pygame.Rect(random.randint(150, 300), -80, 80, 80)
    obstacle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    while running:
        global lost
        global score
        # Show background
        SCREEN.blit(SCALED_BACKGROUND, (-50, -10))
        # Show car
        SCREEN.blit(SCALED_CAR_IMAGE, (car_x, car_y))
        # Show obstacle
        pygame.draw.rect(SCREEN, obstacle_color, obstacle)
        # Obstacle automatic movements
        obstacle_speed = calculate_speed(score)
        obstacle.move_ip(0, obstacle_speed)

        # Check for new obstacle
        if obstacle.y >= 883:
            obstacle = pygame.Rect(random.randint(150, 300), -80, 80, 80)
            obstacle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            score += 1

        # Check for car adjustments
        key = pygame.key.get_pressed()
        adjustments = check_movement(key, car_x)
        car_x += adjustments[0]
        car_y += adjustments[1]

        # Check for collisions
        car_x, car_y = check_border_collision(car_x, car_y)
        lost = check_collision(car_x, car_y, obstacle.x, obstacle.y)

        # Check if lost
        if lost == True:
            break
        # Check whether they pressed the cross
        exit_game(key)
        # Update screen with new settings
        pygame.display.update()

    if lost == True:
        for _ in range(3):
            print()
        print("                                                           You Lost!")
        print("                                                          Score = ", score, end="\n\n\n\n")

    pygame.quit()




def exit_game(key):

    # Check whether they clicked the cross or pressed escape to quit the game
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif key[pygame.K_ESCAPE] == True:
            running = False

def check_movement(key, x_coords):

    # If car is in grass lower speed
    if 50 <= x_coords <= 400:
        speed = 3
    else:
        speed = 1
    # Get car movements
    adjustments = [0, 0]
    if key[pygame.K_UP] == True:
        adjustments[1] = -speed
    if key[pygame.K_DOWN] == True:
        adjustments[1] += speed
    if key[pygame.K_RIGHT] == True:
        adjustments[0] = speed
    if key[pygame.K_LEFT] == True:
        adjustments[0] += -speed
    return adjustments

def check_border_collision(x, y):

    # Check whether they are at the border of the screen
    if x <= 0:
        return [0, y]
    elif x >= 450:
        return [450, y]
    if y <= 50:
        return [x, 50]
    elif y >= 750:
        return [x, 750]
    return [x, y]

def check_collision(car_x, car_y, obstacle_x, obstacle_y):
    if obstacle_x - 88 <= car_x <= obstacle_x + 70:
        if obstacle_y - 180 <= car_y <= obstacle_y + 70:
            return True
    return False

def calculate_speed(score):
    if score < 5:
        return 2
    elif score < 10:
        return 3
    else:
        return 4

if __name__ == "__main__":
    main()
