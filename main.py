import pygame
import random

# initlize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# tittle and icon
pygame.display.set_caption("Space Action")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# adding a player to game
playerImg = pygame.image.load('spacecraft.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0


def palyer(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game Loop
running = True
while running:
    # rgb code here
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystrock is pressed wether itz rigth or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    palyer(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
