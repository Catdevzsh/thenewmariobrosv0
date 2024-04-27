import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The New Mario Bros.")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
blue = (0, 0, 255)
brown = (139, 69, 19)

# Define fonts
font_title = pygame.font.SysFont(None, 48)
font_text = pygame.font.SysFont(None, 24)

# Render text surfaces
title_surface = font_title.render("The New Mario Bros.", True, white)
ready_p1_surface = font_text.render("Ready! P1", True, white)
ready_p2_surface = font_text.render("P2", True, green)
select_surface = font_text.render("Select Your Plumber!", True, white)
mario_surface = font_text.render("Mario", True, red)
luigi_surface = font_text.render("Luigi", True, green)

# Initial selection
selected = "Mario"

# Function to draw a character (simplified representation)
def draw_character(x, y, color):
    pygame.draw.circle(screen, color, (x, y), 20)  # Head
    pygame.draw.rect(screen, color, (x - 10, y + 20, 20, 40))  # Body
    pygame.draw.line(screen, color, (x - 20, y + 40), (x - 40, y + 60), 5)  # Left arm
    pygame.draw.line(screen, color, (x + 20, y + 40), (x + 40, y + 60), 5)  # Right arm
    pygame.draw.line(screen, color, (x - 10, y + 60), (x - 20, y + 80), 5)  # Left leg
    pygame.draw.line(screen, color, (x + 10, y + 60), (x + 20, y + 80), 5)  # Right leg

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                selected = "Luigi" if selected == "Mario" else "Mario"

    # Fill background
    screen.fill(black)

    # Draw title and text
    screen.blit(title_surface, (width // 2 - title_surface.get_width() // 2, 20))
    screen.blit(ready_p1_surface, (50, 100))
    screen.blit(ready_p2_surface, (550, 100))
    screen.blit(select_surface, (width // 2 - select_surface.get_width() // 2, 150))
    screen.blit(mario_surface, (100, 400) if selected == "Mario" else (100, 450))
    screen.blit(luigi_surface, (450, 400) if selected == "Luigi" else (450, 450))

    # Draw characters
    draw_character(120, 250 if selected == "Mario" else 300, red)  # Mario
    draw_character(470, 250 if selected == "Luigi" else 300, green)  # Luigi

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
