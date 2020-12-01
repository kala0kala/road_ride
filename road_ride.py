
import pygame
import random

#ROZMIARY
SCREEN_SIZE = 600 #WIELKOŚĆ EKRANU

#KOLORY
GREEN = (50,205,50) #KOLOR ZIELONY

FPS = 10

#pozycje
car_position = [SCREEN_SIZE/2, 350] #pozycja auta
road_position = [130, 0] #pozycja drogi
bush_position = [35,100] #pozycja krzaku
roadx = [130,-540] #pozycja drugiej drogi
cars_position_x = random.randint(140,382) #pozycja w osi x auta jadącego na nas
cars_position_y = -140 #pozycja w osi y auta jadącego na nas


pygame.init()

gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) #generuje okno
clock = pygame.time.Clock() #dodaje czas
roads = pygame.image.load('r14.png') #ładuje drogę do gry
car = pygame.image.load('cars\8.png') #ładuje auto do gry
bush = pygame.image.load('01.png')
cars = pygame.image.load('3.png') #ładuje drogę do gry

pressed_left = 0 #potrzebne do poruszania się w lewo
pressed_right = 0 #potrzebne do poruszania się w prawo
#pressed_up = 0 #potrzebne do poruszania się w górę
#pressed_down = 0 #potrzebne do poruszania się w dół
ruch = 1


while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #jeśli klikniesz Esc, wyjdziesz z gry
                exit()

            elif event.key == pygame.K_LEFT:        # ruch w lewo    #  jeśli klawisz jest wciśnięty to pressed_[...] ma wartość
                pressed_left = 1                                     #  1, co wprawia w ruch obiekt w ruch
            elif event.key == pygame.K_RIGHT:     # ruch w prawo     ###
                pressed_right = 1                                    ###

        elif event.type == pygame.KEYUP:      # jeśli klawisz nie jest wciśnięty, to pressed_[...] ma wartość 0,
            if event.key == pygame.K_LEFT:       # co sprawia, że obiekt się nie rusza
                pressed_left = 0              ###
            elif event.key == pygame.K_RIGHT:  ###
                pressed_right = 0             ###


    if pressed_left ==1:  #odpowiada za ruch auta w prawo i lewo
        car_position[0]-=5  # jeśli wsiśnięta jest strzałka prawo/lewo
    if pressed_right == 1: ###
        car_position[0]+=5 ###


    if car_position[0] < 130: #zatrzymuje auto na drodze i nie pozwala mu wujechać na trawę
        car_position[0] = 130 ###
    elif car_position[0] > 392: ###
        car_position[0] = 392 ###


    gameDisplay.fill(GREEN) #maluje tło na nowo

    road1 = gameDisplay.blit(roads, (roadx[0],roadx[1])) # generuje i ustawia drogę w pozycji x,y
    road2 = gameDisplay.blit(roads, (road_position[0],road_position[1])) # generuje i ustawia drogę w pozycji x,y
    bush1 = gameDisplay.blit(bush, (bush_position[0],bush_position[1])) #generuje krzaka
    carx = gameDisplay.blit(cars, (cars_position_x,cars_position_y)) # generuje i ustawia auto w pozycji x,y

    pygame.display.update() #aktualizuje wyświetlany obraz

    car1 = gameDisplay.blit(car, (car_position[0],car_position[1])) # generuje i ustawia auto w pozycji x,y

    if ruch == 1:
        bush_position[1]= bush_position[1]+5 #ruch krzaka w dół cały czas o 5 pix
        road_position[1] = road_position[1]+5 #ruch drufiej drogi w dół czły czas o 5 pix
        cars_position_y = cars_position_y +10 #ruch auta jadącego na nas o 10 pix w dół

    if bush_position[1] == 615: #ogranicza ruch krzaka do powierzchni piędzy pix 0, a pix 615 w osi y
        bush_position[1] = 0 ###

    if cars_position_y >=615:  # ogranicza ruch auta jadącego na nas do powierzchni między pix -140, a pix 615 w osi y
        cars_position_y = -140 ###
        cars_position_x = random.randint(140,382) #jeśli auto jadące na nas wyjedzie poza okno gry, generuje nowe położenie w osi x

    if road_position[1]>= 0:    #mechanizm, żeby droga się ruszała
        roadx[1] = roadx[1] + 5   # gra generuje dwie drogi: droga1, droga2
    if road_position[1] == 530:   #obie się jakoś tak przesuwają, że wygląda, jakby była 1 droga, która cały czas się przemieszcza
        road_position[1] = -5   ###
    if roadx[1] == -5:            ###
        roadx[1] = -540       ###

    if car1.colliderect(carx): #jeśli wystąpi kolizja naszego auta z autem jadącym na nas
        exit()                 # następuje wyjście z gry

    pygame.display.update() #aktualizuje wyświetlany obraz
    clock.tick(FPS)
