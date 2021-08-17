import pygame

# initialise the pygame library and functions.
pygame.init()

pygame.display.set_caption("Space Invaders Beta")
titleIcon = pygame.image.load('titleIcon.png')
pygame.display.set_icon(titleIcon)

# setting up the gamescreen
height = 1000
width = 500
gameScreen = pygame.display.set_mode((height, width))


# player

playerImage = pygame.image.load('spaceship.png')
playerPosX = 450
playerChangeInX = 0
playerPosY = 400

# enemy

enemyImage = pygame.image.load('aliens.png')
enemyPosX = 450
enemyChangeInX = 0.1
enemyPosY = 100
enemyChangeInY = 0.1


def player(x, y):
    gameScreen.blit(playerImage, (x, y))


def enemy(x, y):
    gameScreen.blit(enemyImage, (x, y))


def playerBoundaryChecker(x):
    if x < 0:
        x = 0
    elif x > 935:
        x = 935
    return x




# game loop
# keeps the pygame window from closing, until the player closes it themself
isGameRunning = True

while isGameRunning:
    gameScreen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isGameRunning = False

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeInX = -0.3

            if event.key == pygame.K_RIGHT:
                playerChangeInX = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeInX = 0.0

    playerPosX += playerChangeInX
    playerPosX = playerBoundaryChecker(playerPosX)
    player(playerPosX, playerPosY)

    enemyPosX += enemyChangeInX
    if enemyPosX >= 935:
        enemyChangeInX = -0.1
        enemyPosY += 40
    elif enemyPosX <= 0:
        enemyChangeInX = 0.1
        enemyPosY += 40


    enemy(enemyPosX, enemyPosY)

    pygame.display.update()
