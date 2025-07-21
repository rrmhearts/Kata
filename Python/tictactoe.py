import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (66, 135, 245)
RED = (255, 50, 50)
GREEN = (0, 200, 0)

FPS = 30
FONT = pygame.font.SysFont("Arial", 20)

circles = []

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("Chutes and Ladders")

clock = pygame.time.Clock()

# Players' positions
player_positions = [0, 0]
player_colors = [RED, BLUE]
current_player = 0
game_over = False

import pygame

def restart_game():
    # Reset all game-specific variables here
    # Example:
    global circles, game_over, current_player
    circles = []
    game_over = False
    current_player = 0

def get_coords(position):
    """Convert board position to screen coordinates."""
    if position == 0:
        return -CELL_SIZE, HEIGHT  # Off board initially
    row = (position - 1) // 10
    col = (position - 1) % 10
    if row % 2 == 1:
        col = 9 - col
    x = col * CELL_SIZE
    y = HEIGHT - (row + 1) * CELL_SIZE
    return x, y

def draw_board():
    screen.fill(WHITE)
    # Draw grid
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    for circle in circles:
        # pygame.draw.circle(screen, player_colors[i], (x + CELL_SIZE//2, y + CELL_SIZE//2), 15)
        pygame.draw.circle(screen, circle["color"], circle["pos"], circle["radius"])

            # pos = (ROWS - 1 - row) * 10 + (col + 1 if (ROWS - 1 - row) % 2 == 0 else 10 - col)
            # text = FONT.render(str(pos), True, BLACK)
            # screen.blit(text, (col * CELL_SIZE + 5, row * CELL_SIZE + 5))

def main():
    global current_player, game_over
    running = True
    rolled = False
    dice_value = 0
    winner = None
    message = ""
    message_time = 0
    display_duration = 2000  # 2 seconds

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)
        draw_board()

        # UI area
        pygame.draw.rect(screen, (200, 200, 200), (0, HEIGHT, WIDTH, 100))

        if game_over:
            # Display game over message
            # ...
            restart_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    new_circle = {"pos": (mouse_x, mouse_y), "radius": 70, "color": player_colors[current_player]}  # Red circle
                    circles.append(new_circle)
                    current_player = (current_player + 1) % 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_over = True
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
