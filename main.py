from turtle import back
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((300,550))
pygame.display.set_caption("Flappy Bird")

x = 100
y = 250

width = 20
height = 20

vel = 50
speed = 4

delay = 10
fps = 60
clock = pygame.time.Clock()

#bird = pygame.image.load("flappyBird.png").convert_alpha()
#bird = pygame.transform.scale(bird, (120,70))
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale2x(background)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(fps)
    delay -= 1
    if y<=530:
        y += speed
    keys = pygame.key.get_pressed()
    ## Si le delay est ecoulée alors on peut sauter
    if delay <=0:
        # Si la barre espace est pressée alors
        if keys[pygame] and y>=0:
            y -= vel
            #KEYODWN a utiliser
            delay = 10
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (235,255,0), (x, y, width, height))
    pygame.display.update()
