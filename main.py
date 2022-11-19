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

fps = 60
clock = pygame.time.Clock()

#bird = pygame.image.load("flappyBird.png").convert_alpha()
#bird = pygame.transform.scale(bird, (120,70))
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale2x(background)

while True:
    if y<=530: # Simule la gravité
        y += speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Ferme la fenetre si on appuie sur la croix
            pygame.quit()
            sys.exit()
        # Si la barre espace est pressée alors le personnage saute
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and y>=0:
                y -= vel
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (235,255,0), (x, y, width, height))
    pygame.display.flip()
    clock.tick(fps)
