import pygame
#initlize the pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))

# tittle and icon
pygame.display.set_caption("Space Action")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# adding a player spaceship
playerImg = pygame.image.load('spacecraft.png')
playerX = 370
playerY = 480

def palyer(x,y):
    screen.blit(playerImg,(x,y))

#game Loop
running = True
while running:
    #rgb code here
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    palyer(playerX,playerY)
    pygame.display.update()