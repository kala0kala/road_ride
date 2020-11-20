
import pygame

#ROZMIARY
CAR_SIZE_X = 40 #WYSOKOŚĆ AUTA
CAR_SIZE_Y = 40 #SZEROKOŚĆ AUTA
SCREEN_SIZE = 600 #WIELKOŚĆ EKRANU

#KOLORY
GREEN = (50,205,50) #KOLOR ZIELONY

FPS = 10

#pozycje
car_position = [SCREEN_SIZE/2, 350] #pozycja auta
road_position = [130, 0] #pozycja drogi
bush_position = [35,100] #pozycja krzaka

pygame.init()

gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) #generuje okno
clock = pygame.time.Clock() #dodaje czas
roads = pygame.image.load('r1.png') #ładuje drogę do gry
car = pygame.image.load('cars\8.png') #ładuje auto do gry
bush = pygame.image.load('01.png')


pressed_left = 0 #potrzebne do poruszania się w lewo
pressed_right = 0 #potrzebne do poruszania się w prawo
#pressed_up = 0 #potrzebne do poruszania się w górę
#pressed_down = 0 #potrzebne do poruszania się w dół


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
            #elif event.key == pygame.K_UP:    ###
                #pressed_up = 0               ###
            #elif event.key == pygame.K_DOWN:  ###
            #    pressed_down = 0

    if pressed_left ==1: #ruch auta, kiedy wciśnięty klawisz
        car_position[0]-=5 ###
    if pressed_right == 1: ###
        car_position[0]+=5 ###
    #if pressed_up == 1:
    #    car_position[1]-=5
    #if pressed_down == 1:
    #    car_position[1]+=5

    if car_position[0] < 130: #zatrzymuje auto na drodze i nie pozwala mu wyjechać na trawę
        car_position[0] = 130 ###
    elif car_position[0] > 392: ###
        car_position[0] = 392 ###


    gameDisplay.fill(GREEN) #maluje tło na nowo

    gameDisplay.blit(roads, (road_position[0],road_position[1])) # generuje i ustawia auto w pozycji x,y
    gameDisplay.blit(bush, (bush_position[0],bush_position[1])) #generuje krzaka
    pygame.display.update() #aktualizuje wyświetlany obraz

    gameDisplay.blit(car, (car_position[0],car_position[1])) # generuje i ustawia auto w pozycji x,y

    pygame.display.update() #aktualizuje wyświetlany obraz
    clock.tick(FPS)
