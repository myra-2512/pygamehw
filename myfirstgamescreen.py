import pygame


pygame.init()


screen_width = 500
screen_height = 500
screen_size = (screen_width, screen_height)
background_color = (58, 58, 58)


screen = pygame.display.set_mode(screen_size)


pygame.display.set_caption("My first game screen")


image = pygame.image.load('Hello.png') 
image_size = (300, 300)
scaled_image = pygame.transform.scale(image, image_size)


image_rect = scaled_image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background_color)
    
    
    screen.blit(scaled_image, image_rect)
    
    
    pygame.display.flip()


pygame.quit()

