import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

pygame.init()

screen = pygame.display.set_mode((550, 450))
icon = pygame.image.load('brush.png')
pygame.display.set_icon(icon)

x = 100
y = 100
width = 5
height = 5
vel = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0) 


pygame.display.set_caption("Your World")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
display_main = True
main_page = 1
done = False
# -------- Main Page Loop -----------
while not done and display_main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            main_page += 1
            if main_page == 3:
                display_main = False
 
    # Set the screen background
    screen.fill(WHITE)

    if main_page == 1:
        # Welcome page, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        text = font.render("Welcome to Your World!", True, BLACK)
        screen.blit(text, [10, 10])
 
        text = font.render("Page 1", True, BLACK)
        screen.blit(text, [10, 40])
 
    if main_page == 2:
        # Draw instructions, page 2
        text = font.render("Use the arrow keys to draw what you want!", True, BLACK)
        screen.blit(text, [10, 10])
        text = font.render("Hold the ASDW keys to change colour!", True, BLACK)
        screen.blit(text, [10, 40])
        text = font.render("And have fun!", True, BLACK)
        screen.blit(text, [10, 70])
 
        text = font.render("Page 2", True, BLACK)
        screen.blit(text, [10, 100])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()





pygame.quit()