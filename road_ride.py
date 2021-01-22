import pygame
import random
import sys

SCREEN_SIZE = 600

GREEN = (50,205,50)
BLACK = (0,0,0)

FPS = 15

car_position = [SCREEN_SIZE/2, 350]
road_position = [130, 0]
bush_position = [35, 100]
roadx = [130, -540]
cars_position_x = [random.randint(140, 382), random.randint(140, 382)]
cars_position_y = [-140, -550]
coin_position_x = random.randint(150, 372)
coin_position_y = [-140, -210, -280]
pygame.init()
pygame.font.init()

gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()
roads = pygame.image.load('r14.png')
car = pygame.image.load('8.png')
bush = pygame.image.load('01.png')
cars = [pygame.image.load('3.png'), pygame.image.load('2.png')]
coins = pygame.image.load('coin.png')
font = pygame.font.SysFont("fixedsys", 60)
font1 = pygame.font.SysFont("fixedsys", 40)

pressed_left = 0
pressed_right = 0

ruch = 1
money = 1
score = ["0"]
scorex = 0
counting_time = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

            elif event.key == pygame.K_LEFT:
                pressed_left = 1
            elif event.key == pygame.K_RIGHT:
                pressed_right = 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressed_left = 0
            elif event.key == pygame.K_RIGHT:
                pressed_right = 0

    gameDisplay.fill(GREEN)

    road1 = gameDisplay.blit(roads, (roadx[0], roadx[1]))
    road2 = gameDisplay.blit(roads, (road_position[0], road_position[1]))
    bush1 = gameDisplay.blit(bush, (bush_position[0], bush_position[1]))
    if money == 1:
        coins0 = gameDisplay.blit(coins, (coin_position_x, coin_position_y[0]))
        coins1 = gameDisplay.blit(coins, (coin_position_x, coin_position_y[1]))
        coins2 = gameDisplay.blit(coins, (coin_position_x, coin_position_y[2]))
    carx0 = gameDisplay.blit(cars[0], (cars_position_x[0], cars_position_y[0]))
    carx1 = gameDisplay.blit(cars[1], (cars_position_x[1], cars_position_y[1]))

    pygame.display.update()

    car1 = gameDisplay.blit(car, (car_position[0], car_position[1]))
    text1 = font1.render("SCORE", True, (0, 0, 0))
    text = font.render(score[0], True, (0, 0, 0))
    text2 = font1.render("TIME", True, (0, 0, 0))
    gameDisplay.blit(text1, (470, 20))
    gameDisplay.blit(text, (490, 50))
    gameDisplay.blit(text2, (470, 95))
    if counting_time == 1:
        time = pygame.time.get_ticks()/1000
    gameDisplay.blit(font.render(str(time), True, (0, 0, 0)), (490, 120))

    if ruch == 1:
        if pressed_left == 1:
            car_position[0] -= 10
        if pressed_right == 1:
            car_position[0] += 10

        if car_position[0] < 130:
            car_position[0] = 130
        elif car_position[0] > 392:
            car_position[0] = 392

        bush_position[1] = bush_position[1] + 5
        road_position[1] = road_position[1] + 5

        if road_position[1] >= 0:
            roadx[1] = roadx[1] + 5
        if road_position[1] == 530:
            road_position[1] = -5
        if roadx[1] == -5:
            roadx[1] = -540

        for i in range(len(cars_position_y)):
            cars_position_y[i] = cars_position_y[i] + 10
        for i in range(len(coin_position_y)):
            coin_position_y[i] = coin_position_y[i] + 5

    if bush_position[1] == 615:
        bush_position[1] = 0

    for i in range(len(cars_position_y)):
        if cars_position_y[i] >= 615:
            cars_position_y[i] = -140
            cars_position_x[i] = random.randint(140, 382)

    for i in range(len(coin_position_y)):
        if coin_position_y[i] >= 615:
            coin_position_y[i] = -140
            coin_position_x = random.randint(150, 372)

    if car1.colliderect(carx0) or car1.colliderect(carx1):
        counting_time = 0
        ruch = 0

    if ruch == 0:
        text3 = font1.render("TIME: " + str(time), True, (0, 0, 0))
        text4 = font1.render("SCORE: " + score[0], True, (0, 0, 0))
        text5 = font.render("GAME OVER!!!", True, (0, 0, 0))
        pygame.draw.rect(gameDisplay, (178, 34, 34), (50, 150, 500, 300))
        gameDisplay.blit(text5, (155, 190))
        gameDisplay.blit(text4, (160, 260))
        gameDisplay.blit(text3, (160, 310))

        pygame.display.flip()

    if car1.colliderect(coins0):
        if money == 1:
            scorex = scorex + 5
            scorey = str(scorex)
            score[0] = scorey
            money = 0
    if money == 0:
        coin_position_y[0] = -340
        money = 1

    if car1.colliderect(coins1):
        if money == 1:
            scorex = scorex + 5
            scorey = str(scorex)
            score[0] = scorey
            money = 0
    if money == 0:
        coin_position_y[1] = -350
        money = 1

    if car1.colliderect(coins2):
        if money == 1:
            scorex = scorex + 5
            scorey = str(scorex)
            score[0] = scorey
            money = 0
        coin_position_x = random.randint(150, 372)
    if money == 0:
        coin_position_y[2] = -360
        money = 1

    pygame.display.update()
    clock.tick(FPS)
