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
enemyChangeInY = 0.1  # the change when it enemy hits the wall

# bullet
bulletImage = pygame.image.load('bullet.png')
bulletPosX = 0
bulletPosY = 0
bulletYChange = 0.5
global bullet_state
bullet_state = "ready"


def player(x, y):
    gameScreen.blit(playerImage, (x, y))


def enemy(x, y):
    gameScreen.blit(enemyImage, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    gameScreen.blit(bulletImage, (x + 23, y + 5))


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

            #the bullet will only fire if the bullet state is ready, so we can't fire two or
            #more in quick succession
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletPosX = playerPosX
                bulletPosY = playerPosY
                fire_bullet(bulletPosX, bulletPosY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeInX = 0.0

    playerPosX += playerChangeInX
    playerPosX = playerBoundaryChecker(playerPosX)
    player(playerPosX, playerPosY)

    if bullet_state is "fire":
        fire_bullet(bulletPosX, bulletPosY)
        bulletPosY -= bulletYChange
    if bulletPosY <= 2:
        bullet_state = "ready"
        #once the bullet crosses the boundary, we can change it back to ready,
        #so no need to 'draw' again.


    enemyPosX += enemyChangeInX
    if enemyPosX >= 935:
        enemyChangeInX = -0.1
        enemyPosY += 40
    elif enemyPosX <= 0:
        enemyChangeInX = 0.1
        enemyPosY += 40

    enemy(enemyPosX, enemyPosY)

    pygame.display.update()
