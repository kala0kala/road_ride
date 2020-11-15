
import pygame

#ROZMIARY
CAR_SIZE_X = 40 #WYSOKOŚĆ PALETKI
CAR_SIZE_Y = 40 #SZEROKOŚĆ PALETKI
SCREEN_SIZE = 600 #WIELKOŚĆ EKRANU

#KOLORY
GREEN = (0,255,0) #KOLOR ZIELONY
PINK = (255,20,147) #KOLOR RÓŻOWY
BLACK = (0,0,0) #KOLOR CZARNY

FPS = 10


car_position = [SCREEN_SIZE/2, SCREEN_SIZE-CAR_SIZE_Y] #pozycja paletki

pygame.init()

gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) #generuje okno
clock = pygame.time.Clock() #dodaje czas


pressed_left = 0 #potrzebne do poruszania się w lewo
pressed_right = 0 #potrzebne do poruszania się w prawo
pressed_up = 0 #potrzebne do poruszania się w górę
pressed_down = 0 #potrzebne do poruszania się w dół
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

            elif event.key == pygame.K_LEFT:        # ruch w lewo    #  jeśli klawisz jest wciśnięty to pressed_[...] ma wartość
                pressed_left = 1                                     #  1, co wprawia w ruch obiekt w ruch
            elif event.key == pygame.K_RIGHT:     # ruch w prawo     ###
                pressed_right = 1                                    ###
            elif event.key == pygame.K_UP:        # ruch w górę      ###
                pressed_up = 1                                       ###
            elif event.key == pygame.K_DOWN:     # ruch w dół        ###
                pressed_down = 1

        elif event.type == pygame.KEYUP:      # jeśli klawisz nie jest wciśnięty, to pressed_[...] ma wartość 0,
            if event.key == pygame.K_LEFT:       # co sprawia, że obiekt się nie rusza
                pressed_left = 0              ###
            elif event.key == pygame.K_RIGHT:  ###
                pressed_right = 0             ###
            elif event.key == pygame.K_UP:    ###
                pressed_up = 0               ###
            elif event.key == pygame.K_DOWN:  ###
                pressed_down = 0

    if pressed_left ==1:
        car_position[0]-=5
    if pressed_right == 1:
        car_position[0]+=5
    if pressed_up == 1:
        car_position[1]-=5
    if pressed_down == 1:
        car_position[1]+=5

    gameDisplay.fill(BLACK) #maluje tło na nowo

    pygame.draw.rect(gameDisplay, PINK, (car_position[0], car_position[1], CAR_SIZE_X, CAR_SIZE_Y)) #rysuje auto (Różowy kwadrat)
    pygame.display.update() #aktualizuje wyświetlany obraz
    clock.tick(FPS)
