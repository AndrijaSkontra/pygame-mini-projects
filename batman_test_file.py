import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Simple Jump")

# Set the background color
bg_color = (255, 255, 255)

# Set the player's starting position
player_x = 270
player_y = 380

player_velocity = 0

gravity = 1
jump_strength = -15

player_image = pygame.image.load("R.png").convert_alpha()
LIK = pygame.transform.scale(player_image,(100,100))

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for a key press
        if event.type == pygame.KEYDOWN:
            # If the space bar is pressed, jump
            if event.key == pygame.K_SPACE:
                player_velocity = jump_strength

    player_velocity += gravity

    player_y += player_velocity

    if player_y > 380:
        player_velocity = 0
        player_y = 380

    screen.fill(bg_color)

    screen.blit(LIK, (player_x, player_y))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
