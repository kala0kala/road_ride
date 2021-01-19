import pygame
import random
import sys

#ROZMIARY
SCREEN_SIZE = 600 #WIELKOŚĆ EKRANU

#KOLORY
GREEN = (50,205,50) #KOLOR ZIELONY
BLACK = (0,0,0) #KOLOR CZARNY

FPS = 15 # zmienna potrzebna do ustalenia szybkości gry

#pozycje
car_position = [SCREEN_SIZE/2, 350] #pozycja auta
road_position = [130, 0] #pozycja drogi
bush_position = [35,100] #pozycja krzaku
roadx = [130,-540] #pozycja drugiej drogi
cars_position_x = [random.randint(140,382),random.randint(140,382)] #pozycja w osi x auta jadącego na nas
cars_position_y = [-140, -550] #pozycja w osi y auta jadącego na nas
coin_position_x = random.randint(150,372) # pozycja monety w osi x
coin_position_y = [-140, -210, -280] #pozycja monety w osi y

pygame.init() #uruchamia pygame
pygame.font.init() #uruchamia czcionkę w pygame

gameDisplay = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) #generuje okno
clock = pygame.time.Clock() #dodaje czas
roads = pygame.image.load('r14.png') #ładuje drogę do gry
car = pygame.image.load('8.png') #ładuje auto do gry
bush = pygame.image.load('01.png') #ładuje krzak dogry
cars = [pygame.image.load('3.png'),pygame.image.load('2.png')] #ładuje auto do gry
coins = pygame.image.load('coin.png') #ładuje monety do gry
font = pygame.font.SysFont("fixedsys", 60) # czcionka i jej wielkość
font1 = pygame.font.SysFont("fixedsys", 40) # kolejna czcionka i jej wielkość

pressed_left = 0 #potrzebne do poruszania się w lewo
pressed_right = 0 #potrzebne do poruszania się w prawo

ruch = 1 #potrzebne do poruszania się obiektów w grze
money = 1 # potrzebne do wyświetlania monet
score = ["0"] # potrzebne do zapisywania wyniku
scorex = 0
counting_time = 1 #potrzebne do liczenia czasu

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

    gameDisplay.fill(GREEN) #maluje tło na nowo

    road1 = gameDisplay.blit(roads, (roadx[0],roadx[1])) # generuje i ustawia drogę w pozycji x,y
    road2 = gameDisplay.blit(roads, (road_position[0],road_position[1])) # generuje i ustawia drogę w pozycji x,y
    bush1 = gameDisplay.blit(bush, (bush_position[0],bush_position[1])) #generuje krzaka
    if money == 1:       #jeśli wykryta jest moneta
        coins0 = gameDisplay.blit(coins, (coin_position_x,coin_position_y[0]))     #generuje i ustawia monetę w pozycji x, y
        coins1 = gameDisplay.blit(coins, (coin_position_x,coin_position_y[1]))  ###
        coins2 = gameDisplay.blit(coins, (coin_position_x,coin_position_y[2]))  ###
    carx0 = gameDisplay.blit(cars[0], (cars_position_x[0],cars_position_y[0])) # generuje i ustawia auto jadące na nas w pozycji x,y
    carx1 = gameDisplay.blit(cars[1], (cars_position_x[1],cars_position_y[1])) ###

    pygame.display.update() #aktualizuje wyświetlany obraz

    car1 = gameDisplay.blit(car, (car_position[0],car_position[1])) # generuje i ustawia auto gracza w pozycji x,y
    text1 = font1.render("SCORE", True, (0,0,0))
    text = font.render(score[0], True, (0,0,0))  # Generuje teksr
    text2 = font1.render("TIME", True, (0,0,0))
    gameDisplay.blit(text1, (470,20))           #Wyświetla wynik
    gameDisplay.blit(text, (490,50))
    gameDisplay.blit(text2, (470,95))
    if counting_time == 1: #liczenie czasu
        time = pygame.time.get_ticks()/1000 #generuje czas i przelicza go na sekundy
    gameDisplay.blit(font.render(str(time), True, (0,0,0)), (490, 120)) #wyświetla czas

    if ruch == 1: # mechanizm sprawiający, że wszystkie obiekty w grze się ruszają
        if pressed_left ==1:  #odpowiada za ruch auta w prawo i lewo
            car_position[0]-=10  # jeśli wsiśnięta jest strzałka prawo/lewo
        if pressed_right == 1: ###
            car_position[0]+=10 ###

        if car_position[0] < 130: #zatrzymuje auto na drodze i nie pozwala mu wjechać na trawę
            car_position[0] = 130 ###
        elif car_position[0] > 392: ###
            car_position[0] = 392 ###

        bush_position[1]= bush_position[1]+5 #ruch krzaka w dół cały czas o 5 pix
        road_position[1] = road_position[1]+5 #ruch drugiej drogi w dół cały czas o 5 pix

        if road_position[1]>= 0:    #mechanizm, żeby droga się ruszała
            roadx[1] = roadx[1] + 5   # gra generuje dwie drogi: droga1, droga2
        if road_position[1] == 530:   #obie się jakoś tak przesuwają, że wygląda, jakby była 1 droga, która cały czas się przemieszcza
            road_position[1] = -5   ###
        if roadx[1] == -5:            ###
            roadx[1] = -540       ###

        for i in range(len(cars_position_y)):
            cars_position_y[i] = cars_position_y[i] +10 #ruch auta jadącego na nas o 10 pix w dół
        for i in range(len(coin_position_y)):
            coin_position_y[i] = coin_position_y[i] + 5 #ruch monety w dół o 5 pix
    

    if bush_position[1] == 615: #ogranicza ruch krzaka do powierzchni piędzy pix 0, a pix 615 w osi y
        bush_position[1] = 0 ###

    for i in range(len(cars_position_y)):
        if cars_position_y[i] >=615:  # ogranicza ruch auta jadącego na nas do powierzchni między pix -140, a pix 615 w osi y
            cars_position_y[i] = -140 ###
            cars_position_x[i] = random.randint(140,382) #jeśli auto jadące na nas wyjedzie poza okno gry, generuje nowe położenie w osi x

    for i in range(len(coin_position_y)):
        if coin_position_y[i] >=615:           #jeśli pozycja y monety będzie większa niż 615 pix
            coin_position_y[i] = -140          #moneta zmienia sfoją pozycję y na -140 pix
            coin_position_x = random.randint(150,372)  #generuje nową pozycję x monety

    if car1.colliderect(carx0) or car1.colliderect(carx1): #jeśli wystąpi kolizja naszego auta z autem jadącym na nas:
        counting_time = 0 #czas się zatrzymuje
        ruch = 0 #ruch się zatrzymuje

    if ruch == 0:
        text3 = font1.render("TIME: " + str(time), True, (0,0,0)) #generuje tekst pokazujący czas
        text4 = font1.render("SCORE: " + score[0], True, (0,0,0)) # generuje tekst pokazujący wynik
        text5 = font.render("GAME OVER!!!", True, (0,0,0)) #generuje tekst "koniec gry"
        pygame.draw.rect(gameDisplay, (178, 34, 34), (50, 150, 500, 300)) #generuje planszę:
        gameDisplay.blit(text5, (155,190)) # wyświetlającą napis "koniec gry"
        gameDisplay.blit(text4, (160,260))    # wyświetlającą wynik
        gameDisplay.blit(text3, (160,310))   # wyświetlającą czas

        pygame.display.flip()

    if car1.colliderect(coins0):   # jeśli auto zderzy się z monetą
        if money == 1:
            scorex = scorex + 5  # dodają się punkty do wyniku
            scorey = str(scorex)  # zachodzi magia, żeby wynik się dobrze przetworzył i wyświetlił
            score[0] = scorey     ###
            money = 0  # moneta zmienia swoją wartość na 0 i znika
    if money == 0: #jeśli moneta zniknęła
        coin_position_y[0] = -340 #zmienia pozycję y na -340 pix
        money = 1  #zmienia swoją wartość na 1, żeby móc się póżniej pojawić

    if car1.colliderect(coins1):   # jeśli auto zderzy się z monetą
        if money == 1:
            scorex = scorex + 5  # dodają się punkty do wyniku
            scorey = str(scorex)  # zachodzi magia, żeby wynik się dobrze przetworzył i wyświetlił
            score[0] = scorey     ###
            money = 0  # moneta zmienia swoją wartość na 0 i znika
    if money == 0: #jeśli moneta zniknęła
        coin_position_y[1] = -350 #zmienia pozycję y na -340 pix
        money = 1  #zmienia swoją wartość na 1, żeby móc się póżniej pojawić

    if car1.colliderect(coins2):   # jeśli auto zderzy się z monetą
        if money == 1:
            scorex = scorex + 5  # dodają się punkty do wyniku
            scorey = str(scorex)  # zachodzi magia, żeby wynik się dobrze przetworzył i wyświetlił
            score[0] = scorey     ###
            money = 0  # moneta zmienia swoją wartość na 0 i znika
        coin_position_x = random.randint(150,372)  #generuje nową pozycję x monety
    if money == 0: #jeśli moneta zniknęła
        coin_position_y[2] = -360 #zmienia pozycję y na -340 pix
        money = 1  #zmienia swoją wartość na 1, żeby móc się póżniej pojawić

    pygame.display.update() #aktualizuje wyświetlany obraz
    clock.tick(FPS)  #szybkość gry
