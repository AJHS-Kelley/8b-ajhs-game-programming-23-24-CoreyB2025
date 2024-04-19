# Final Project, Corey Battle, v0.0

import pygame
import sys
import random


# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PLATFORM_WIDTH, PLATFORM_HEIGHT = 100, 10
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)  # Light blue color for the level indicator
# Initialize Pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")
font = pygame.font.Font(None, 36)


# Clock to control the frame rate
clock = pygame.time.Clock()

# Initialize variables for the game
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]  # Faster starting speed
platform_pos = [WIDTH // 2 - PLATFORM_WIDTH // 2, HEIGHT - PLATFORM_HEIGHT - 10]
platform_speed = 10
score = 0
lives = 3
current_level = 1
platform_color = ORANGE  # Initialize platform color
# Functions for screens
def start_screen():
    screen.fill(BLACK)
    show_text_on_screen("Bouncing Ball Game", 50, HEIGHT // 4)
    show_text_on_screen("Press any key to start...", 30, HEIGHT // 3)
    show_text_on_screen("Move the platform with arrow keys...", 30, HEIGHT // 2)
    pygame.display.flip()
    wait_for_key()


def game_over_screen():
    screen.fill(BLACK)
    show_text_on_screen("Game Over", 50, HEIGHT // 3)
    show_text_on_screen(f"Your final score: {score}", 30, HEIGHT // 2)
    show_text_on_screen("Press any key to restart...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()


def victory_screen():
    screen.fill(BLACK)
    show_text_on_screen("Congratulations!", 50, HEIGHT // 3)
    show_text_on_screen(f"You've won with a score of {score}", 30, HEIGHT // 2)
    show_text_on_screen("Press any key to exit...", 20, HEIGHT * 2 // 3)
    pygame.display.flip()
    wait_for_key()


def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


def show_text_on_screen(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, WHITE)
    text_rect = text_render.get_rect(center=(WIDTH // 2, y_position))
    screen.blit(text_render, text_rect)


def change_platform_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# Main game loop
start_screen()
game_running = True


while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False


    keys = pygame.key.get_pressed()


# Move the platform
    platform_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * platform_speed
    platform_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * platform_speed


    # Ensure the platform stays within the screen boundaries
    platform_pos[0] = max(0, min(platform_pos[0], WIDTH - PLATFORM_WIDTH))
    platform_pos[1] = max(0, min(platform_pos[1], HEIGHT - PLATFORM_HEIGHT))


    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]


    # Bounce off the walls
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_speed[0] = -ball_speed[0]


    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]


 # Check if the ball hits the platform
    if (
        platform_pos[0] <= ball_pos[0] <= platform_pos[0] + PLATFORM_WIDTH
        and platform_pos[1] <= ball_pos[1] <= platform_pos[1] + PLATFORM_HEIGHT
    ):
        ball_speed[1] = -ball_speed[1]
        score += 1


    # Check if the player advances to the next level
    if score >= current_level * 5:
        current_level += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]  # Randomize the ball speed
        platform_color = change_platform_color()


