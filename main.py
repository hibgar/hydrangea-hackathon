import pygame
import requests
from pygame import mixer
from replit import audio
pygame.init()

screen = pygame.display.set_mode((550, 450))
icon = pygame.image.load('brush.png')
pygame.display.set_icon(icon)
mixer.music.load("In_a_Moments_Embrace.wav")
mixer.music.play(0)
source = audio.play_file("In_a_Moments_Embrace.wav")


x = 100
y = 100
width = 5
height = 5
vel = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)


pygame.display.set_caption("Instruction Screen")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
display_instructions = True
instruction_page = 1
data = open('untitled.txt', 'r+')
num = data.read()


done = False
# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 4:
                display_instructions = False
                running = True

    # Set the screen background
    screen.fill(WHITE)
    if num > '2':
        your_world = pygame.image.load('your world.png')
        screen.blit(your_world, (20, 0))
    if num > '23242325':
        our_world = pygame.image.load('our world.png')
        screen.blit(our_world, (20, 0))

    if instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
        if num > '2':
            text = font.render("Welcome back! How was your day?", True, BLACK)
            screen.blit(text, [10, 10])
        else:
            text = font.render("Welcome! How was your day?", True, BLACK)
            screen.blit(text, [10, 10])
        text = font.render("Let's play a game!", True, BLACK)
        screen.blit(text, [10, 40])

    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render(
            "Use the arrow keys to draw what you want!", True, BLACK)
        screen.blit(text, [10, 10])

        text = font.render("Use white (D key) for what went well", True, BLACK)
        screen.blit(text, [10, 40])
        text = font.render(
            "Use purple (A key) for feeling powerful.", True, PURPLE)
        screen.blit(text, [10, 70])
        text = font.render("Use red (S key) for feeling angry.", True, RED)
        screen.blit(text, [10, 100])
        text = font.render("Use green (W key) for calmness.", True, GREEN)
        screen.blit(text, [10, 130])
        text = font.render(
            "Use black (no key) for what went bad.", True, BLACK)
        screen.blit(text, [10, 160])

    if instruction_page == 3:
        if num == '2':
            text = font.render("By the way, we awarded you " +
                               num + " points!", True, BLACK)
            screen.blit(text, [10, 10])
            text = font.render(
                "It's a gift for having opened our game.", True, BLACK)
            screen.blit(text, [10, 40])
            text = font.render("Now to go have fun!", True, BLACK)
            screen.blit(text, [10, 70])
        else:
            text = font.render("You have: ", True, BLACK)
            screen.blit(text, [10, 10])
            text = font.render(num + " points", True, BLACK)
            screen.blit(text, [10, 40])
            text = font.render("Thanks for playing our game.", True, BLACK)
            screen.blit(text, [10, 70])
            text = font.render("Now to go have fun!", True, BLACK)
            screen.blit(text, [10, 100])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


image = pygame.image.load('canvas.png')
pygame.display.set_caption("Painting Game")


screen.blit(image, (0, -100))
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            point = int(num)
            point += 1
            point = str(point)
            data.write(point)
            print(point)
            data.close()
            pygame.image.save(screen, './output.png')
            r = requests.post(
                "https://api.deepai.org/api/deepdream",
                files={
                    'image': open('./output.png', 'rb'),
                },
                headers={'api-key': '7aee7d43-d368-4cde-8772-fe56ed39addb'}
            )
            print(r.json())
            url = "https://lunapic-photo-effects.p.rapidapi.com/v2/api-call.php"
            querystring = {"filter": "Rainbow", "url": "./output.png"}
            headers = {
                'x-rapidapi-key': "a4c3797463msha2b52cd762d7d52p1ca963jsn2d50dfa178a4",
                'x-rapidapi-host': "lunapic-photo-effects.p.rapidapi.com"
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= 60:
        x -= vel

    if keys[pygame.K_RIGHT] and x <= 520:
        x += vel

    if keys[pygame.K_UP] and y >= 70:
        y -= vel

    if keys[pygame.K_DOWN] and y <= 420:
        y += vel
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    if keys[pygame.K_a]:
        pygame.draw.rect(screen, (100, 50, 100), (x, y, width, height))
    if keys[pygame.K_d]:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    if keys[pygame.K_s]:
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    if keys[pygame.K_w]:
        pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            screen.fill(pygame.image.load('canvas.png'))
            pygame.display.update()

    pygame.display.update()

pygame.quit()
