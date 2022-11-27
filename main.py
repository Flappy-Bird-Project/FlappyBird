from turtle import back
import pygame, sys
import random


pygame.init()
screen = pygame.display.set_mode((300,550)) # -> taille de la fenêtre
pygame.display.set_caption("Flappy Bird") # -> Nom de la fenêtre


def MainGame(): # -> fonction principale
    x = 100 # -> coordonnées de l'oiseau
    y = 250 # ->pareil
    gameOver = False  

    width = 20 # -> taille de l'oiseau
    height = 20

    vel = 100 # -> "velocité" simulée
    speed = 4 # -> vitesse de l'oiseau

    fps = 60
    clock = pygame.time.Clock()
    score = []

    background = pygame.image.load("background.png").convert() # -> telecharger l'image de fond
    background = pygame.transform.scale2x(background) # -> agrandir celle-ci de 2x
    gameOverScreen = pygame.image.load("GameOver.png").convert_alpha() # -> telecharger l'image de fond quand on a perdu
    gameOverBg = pygame.image.load("backgroundLose.jpg").convert()# ->idem

    pipe1 = pygame.image.load("TopSprite.png").convert_alpha() # -> telecharger le tuyau d'en haut
    pipe1 = pygame.transform.scale2x(pipe1)
    pipe2 = pygame.image.load("BottomePipe.png").convert_alpha() # ->telecharger le tuyau d'en bas
    pipe2 = pygame.transform.scale2x(pipe2)

    pipeX = 200 # -> coordonée X des tuyaux

    pipeY = random.randint(-230,0) # -> coordonnée Y du tuyau d'en haut
    pipeY1 = pipeY + 450 # -> coordonnée Y du tuyau d'en bas
    
    while True: # -> permet de creer un fenetre et de la laisser ouverte

        if pipeX > -100 and gameOver == False: # -> Condition qui fait bouger les tuyau de droite a gauche (effet d'optique)
            pipeX -= 2

        if y <= 530: # -> Simule la gravité
            y += speed
        for event in pygame.event.get(): # -> recupère tout les evenements qui se passent dans la fenetre
            if event.type == pygame.QUIT: # Ferme la fenetre si on appuie sur la croix
                pygame.quit()
                sys.exit()
            
            # Si la barre espace est pressée alors le personnage saute
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and y >= 0 and gameOver == False:
                    y -= vel
                if event.key == pygame.K_RETURN and gameOver == True:
                    gameOver = False
                    pygame.init()
        
        screen.blit(background, (0,0)) # -> affiche le fond

        if pipeX < -80: # -> Si les tuyaux sortent de l'ecran, le déplacer devant l'oiseau
            pipeX = 300
            pipeY = random.randint(-230,0)
            pipeY1 = pipeY + 450
            screen.blit(pipe1, (pipeX, pipeY))
            screen.blit(pipe2, (pipeX, pipeY1))
        
        screen.blit(pipe1, (pipeX, pipeY)) # -> afficher les premiers tuyaux
        screen.blit(pipe2, (pipeX, pipeY1))

        pygame.draw.rect(screen, (235,255,0), (x, y, width, height)) # -> dessine l'oiseau

        if x == pipeX and pipeY < y < pipeY1 and gameOver == False: # -> Si l'oiseau est entre les 2 tuyaux ajouter 1 au score
            score.append(1)
            print(len(score))

        if pipeX -5 < x < pipeX +5: # -> Si l'oiseau touche les tuyaux arreter le jeu
            if 0 < y < pipeY + 320 or pipeY1 < y < 550:
                gameOver = True
                
                
        if gameOver == True: # -> Si le jeu est perdu, afficher l'ecran de fin
            screen.blit(gameOverBg, (0,0))
            screen.blit(gameOverScreen, (0,0))  

        pygame.display.flip()
        clock.tick(fps) # -> met les fps a 60

MainGame()
