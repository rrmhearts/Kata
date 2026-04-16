import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (66, 135, 245)
RED = (255, 50, 50)
GREEN = (0, 200, 0)

FPS = 30
FONT = pygame.font.SysFont("Arial", 20)

# Define ladders and chutes as a dictionary {start: end}
ladders = {3: 22, 5: 8, 11: 26, 20: 29, 28: 84, 36: 44, 51: 67, 71: 91}
chutes = {17: 4, 19: 7, 21: 9, 27: 1, 54: 34, 62: 18, 64: 60, 87: 24, 93: 73, 95: 75, 98: 79}

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("Chutes and Ladders")

clock = pygame.time.Clock()

# Players' positions
player_positions = [0, 0]
player_colors = [RED, BLUE]
current_player = 0
climb_or_fall = 0

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

            pos = (ROWS - 1 - row) * 10 + (col + 1 if (ROWS - 1 - row) % 2 == 0 else 10 - col)
            text = FONT.render(str(pos), True, BLACK)
            screen.blit(text, (col * CELL_SIZE + 5, row * CELL_SIZE + 5))

    # Draw ladders
    for start, end in ladders.items():
        sx, sy = get_coords(start)
        ex, ey = get_coords(end)
        pygame.draw.line(screen, GREEN, (sx + CELL_SIZE//2, sy + CELL_SIZE//2), (ex + CELL_SIZE//2, ey + CELL_SIZE//2), 4)

    # Draw chutes
    for start, end in chutes.items():
        sx, sy = get_coords(start)
        ex, ey = get_coords(end)
        pygame.draw.line(screen, BLACK, (sx + CELL_SIZE//2, sy + CELL_SIZE//2), (ex + CELL_SIZE//2, ey + CELL_SIZE//2), 4)

    # Draw players
    for i, pos in enumerate(player_positions):
        x, y = get_coords(pos)
        pygame.draw.circle(screen, player_colors[i], (x + CELL_SIZE//2, y + CELL_SIZE//2), 15)

def roll_dice():
    return random.randint(1, 6)

def show_message(message, climb=0, y_offset=0):
    if climb != 0:
        climber = "Player hit a chute!" if climb==-1 else "Player hit a ladder!\n"
        message = climber + message
    text = FONT.render(message, True, BLACK)
    screen.blit(text, (10, HEIGHT + 10 + y_offset))

def main():
    global current_player, climb_or_fall
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and not rolled and winner is None:
                if event.key == pygame.K_SPACE:
                    dice_value = roll_dice()
                    rolled = True
                    message = f"Player {current_player + 1} rolled a {dice_value}"
                    message_time = pygame.time.get_ticks()

        # Handle post-roll logic with delay
        if rolled:
            now = pygame.time.get_ticks()
            show_message(message, climb_or_fall)
            if now - message_time >= display_duration:
                player = player_positions[current_player]
                new_pos = player + dice_value

                if new_pos <= 100:
                    player_positions[current_player] = new_pos

                # Check ladders or chutes
                pos = player_positions[current_player]
                if pos in ladders:
                    player_positions[current_player] = ladders[pos]
                    climb_or_fall = 1
                elif pos in chutes:
                    player_positions[current_player] = chutes[pos]
                    climb_or_fall = -1
                else:
                    climb_or_fall = 0

                if player_positions[current_player] == 100:
                    winner = current_player
                else:
                    current_player = (current_player + 1) % 2

                rolled = False

        else:
            if winner is not None:
                show_message(f"Player {winner + 1} wins!")
            else:
                show_message(f"Player {current_player + 1}'s turn. Press SPACE to roll.")

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
