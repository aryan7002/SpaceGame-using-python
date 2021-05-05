import pygame
import random

# initlize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.jpg')  # your background image here

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
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40

# bullet
# redy = you cant see the bullet on screen
# fire = bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.9
bullet_state = "redy"


def palyer(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# game Loop
running = True
while running:
    # rgb code here
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystrock is pressed wether itz rigth or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'redy':
                    # get the current x cordinate of spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundries of spaceship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "redy"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    palyer(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
