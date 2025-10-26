import pygame

# Initialize Pygame
pygame.init()

# Define screen parameters
screen_width = 500
screen_height = 500
screen_size = (screen_width, screen_height)
background_color = (58, 58, 58) # Grey

# Create the screen
screen = pygame.display.set_mode(screen_size)

# Set the window caption
pygame.display.set_caption("My first game screen")

# Load and scale the image
# You need to replace 'your_image.png' with the actual path to your image file
image = pygame.image.load('Hello.png') 
image_size = (300, 300)
scaled_image = pygame.transform.scale(image, image_size)

# Get the rectangle for the image and center it
image_rect = scaled_image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)
    
    # Blit (draw) the image onto the screen
    screen.blit(scaled_image, image_rect)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

