import pygame
import random
import time



# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CapMan Game")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Font
font = pygame.font.Font(None, 36)

# Pac-Man settings
pacman_size = 20
pacman_speed = 5

# Ghost settings
ghost_size = 20

# Food settings
food_size = 10

# Score variable
score = 0

# Clock for FPS
clock = pygame.time.Clock()

# Timer for each level (10 seconds per level)
level_duration = 10

# Number of levels
total_levels = 5

def draw_text(text, position, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def play_level(level):
    global score
    # Adjust difficulty for each level (speed, number of ghosts, layout)
    pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
    ghost_x, ghost_y = random.randint(0, WIDTH - ghost_size), random.randint(0, HEIGHT - ghost_size)
    food_x, food_y = random.randint(0, WIDTH - food_size), random.randint(0, HEIGHT - food_size)

    level_start_time = time.time()

    # Adjust ghost speed based on level
    if level == 1:
        ghost_speed = 1  # Slow for level 1
    elif level == 2:
        ghost_speed = 2  # Slightly faster
    elif level == 3:
        ghost_speed = 3  # Moderate speed
    elif level == 4:
        ghost_speed = 4  # Fast
    elif level == 5:
        ghost_speed = 5  # Fastest speed, challenge level

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Check if 10 seconds have passed for the level
        if time.time() - level_start_time > level_duration:
            break

        # Get keys for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pacman_x > 0:
            pacman_x -= pacman_speed
        if keys[pygame.K_RIGHT] and pacman_x < WIDTH - pacman_size:
            pacman_x += pacman_speed
        if keys[pygame.K_UP] and pacman_y > 0:
            pacman_y -= pacman_speed
        if keys[pygame.K_DOWN] and pacman_y < HEIGHT - pacman_size:
            pacman_y += pacman_speed

        # Ghost movement (simple AI)
        if pacman_x < ghost_x:
            ghost_x -= ghost_speed
        elif pacman_x > ghost_x:
            ghost_x += ghost_speed

        if pacman_y < ghost_y:
            ghost_y -= ghost_speed
        elif pacman_y > ghost_y:
            ghost_y += ghost_speed

        # Check for collision with ghost (Game over)
        if (abs(pacman_x - ghost_x) < pacman_size and abs(pacman_y - ghost_y) < pacman_size):
            return False  # Player loses

        # Check for collision with food (Eat food)
        if (abs(pacman_x - food_x) < pacman_size and abs(pacman_y - food_y) < pacman_size):
            food_x = random.randint(0, WIDTH - food_size)
            food_y = random.randint(0, HEIGHT - food_size)
            score += 10  # Increment score

        # Drawing everything on the screen
        screen.fill(BLACK)

        # Draw Pac-Man
        pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_size // 2)

        # Draw Ghost
        pygame.draw.rect(screen, BLUE, (ghost_x, ghost_y, ghost_size, ghost_size))

        # Draw Food
        pygame.draw.rect(screen, WHITE, (food_x, food_y, food_size, food_size))

        # Render the score
        draw_text(f"Score: {score}", (10, 10))

        # Render the level
        draw_text(f"Level: {level}", (WIDTH - 150, 10))

        # Update the screen
        pygame.display.flip()

        # Frame rate control
        clock.tick(30)

    return True  # Player completes level

# Function to display "CapMan" title before game starts
def show_title():
    screen.fill(BLACK)
    draw_text("CapMan", (WIDTH // 2 - 80, HEIGHT // 2 - 40), YELLOW)
    pygame.display.flip()
    time.sleep(2)

# Show title
show_title()

# Game loop for levels
for level in range(1, total_levels + 1):
    print(f"Starting Level {level}")
    level_complete = play_level(level)
    
    if not level_complete:
        print(f"Game Over at Level {level}!")
        break  # Game over

# Quit Pygame
pygame.quit()


