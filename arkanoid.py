import random

import pygame

from bala import Bala
from kijas import Kijas
from bloczek import Bloczek


def return_random_color():
    return random.randrange(255), random.randrange(255), random.randrange(255)


def odbicie(kierunek, obrot=True):
    if kierunek > 8:
        kierunek = random.randrange(7, 9)
    if kierunek < -8:
        kierunek = random.randrange(-9, -7)
    else:
        if random.randrange(100) > 69:
            kierunek = abs(kierunek) + random.randrange(0, 2)
    if obrot:
        kierunek *= -1
    return kierunek


class Arkanoid:
    lista_bal = []
    lista_bloczkow = []
    matryca_bloczkow: Bloczek = [[None for x in range(14)] for y in range(14)]

    def __init__(self, screen, width, height):
        print("Arkanoid class")
        self.SCREEN = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.add_bala()

    def interpret(self, textfile, level_map):
        with open(textfile) as f:
            lines = f.readlines()
            x = 0
            y = 0
            for line in lines:
                line_split = line.split(",")
                for line_splitted in line_split:
                    if line_splitted:
                        try:
                            if line_splitted[1]:
                                pass
                        except IndexError:
                            line_splitted += "4"
                        if line_splitted[0] == "R":
                            level_map[x][y] = Bloczek(self.SCREEN, y * 50 + 50, x * 25 + 25, int(line_splitted[1]), "RED")
                        if line_splitted[0] == "G":
                            level_map[x][y] = Bloczek(self.SCREEN, y * 50 + 50, x * 25 + 25, int(line_splitted[1]), "GREEN")
                        if line_splitted[0] == "B":
                            level_map[x][y] = Bloczek(self.SCREEN, y * 50 + 50, x * 25 + 25, int(line_splitted[1]), "BLUE")
                        if line_splitted[0] == "Y":
                            level_map[x][y] = Bloczek(self.SCREEN, y * 50 + 50, x * 25 + 25, int(line_splitted[1]))
                    y += 1
                x += 1
                y = 0

    def add_bala(self):
        if len(self.lista_bal) > 100:
            pass
        else:
            self.lista_bal.append(Bala(0, 0, return_random_color()))

    def pop_bala(self):
        try:
            self.lista_bal.pop()
        except IndexError:
            pass

    def remove_bala(self, bala):
        self.lista_bal.remove(bala)

    def add_bloczek_matryca(self):
        x = random.randrange(0, 14)
        y = random.randrange(0, 14)
        try:
            if self.matryca_bloczkow[x][y] is None:
                self.matryca_bloczkow[x][y] = Bloczek(self.SCREEN, y * 50 + 50, x * 25 + 25, random.randrange(1, 4),
                                                      random.choice(["RED", "GREEN", "BLUE", "GRAY"]))
            else:
                self.add_bloczek_matryca()
        except RecursionError:
            pass

    def remove_bloczek_matryca(self, x, y):
        self.matryca_bloczkow[x][y] = None

    def draw_kijas(self, kijas):
        pygame.draw.rect(self.SCREEN, (255, 255, 255),
                         [kijas.posX, self.HEIGHT - 50, kijas.width, kijas.height])

    def gra(self):
        kijas = Kijas()
        is_running = True
        while is_running:
            # print(len(self.lista_bal))
            kijas_max = self.WIDTH - kijas.width
            if pygame.mouse.get_pos()[0] > kijas_max:
                kijas.posX = kijas_max
            else:
                kijas.posX = pygame.mouse.get_pos()[0]
            pygame.time.delay(15)
            pygame.display.flip()
            self.SCREEN.fill((0, 0, 0))
            self.draw_kijas(kijas)
            for x, y in enumerate(self.matryca_bloczkow):  # Rysowanie bloczkow
                if y:
                    for z in y:
                        if z:
                            z.draw_bloczek()
            for bala in self.lista_bal:  # Zachowanie bali
                for x, y in enumerate(self.matryca_bloczkow):  # Wykrywanie kolizji z bloczkami
                    if y:
                        for z in y:
                            if z:
                                if z.posX - 5 < bala.posX + bala.dirX < z.posX + z.width + 5 \
                                        and z.posY - 5 < bala.posY + bala.dirY < z.posY + z.height + 5:
                                    if z.durability > 1:
                                        z.durability -= 1
                                    else:
                                        self.remove_bloczek_matryca(x, y.index(z))
                                    if bala.posX + bala.dirX - 5 < z.posX:
                                        bala.dirX = odbicie(bala.dirX)
                                    if bala.posX + bala.dirX + 5 > z.posX + z.width:
                                        bala.dirX = odbicie(bala.dirX)
                                    if bala.posY + bala.dirY - 5 < z.posY:
                                        bala.dirY = odbicie(bala.dirY)
                                    if bala.posY + bala.dirY + 5 > z.posY + z.height:
                                        bala.dirY = odbicie(bala.dirY)
                # bala.posX = bala.posX < self.WIDTH and bala.posX + bala.dirX or 0
                # bala.posY = bala.posY < self.HEIGHT and bala.posY + bala.dirY or 0 ZACHOWAC NA EASTER EGGA
                bala.posX += bala.dirX  # Poruszanie bali
                bala.posY += bala.dirY
                if bala.posY > self.HEIGHT:  # Odbijanie od ścian i spadanie w dół
                    self.remove_bala(bala)
                    # bala.dirY = odbicie(bala.dirY, True)
                if bala.posX + bala.dirX > self.WIDTH + bala.dirX:
                    bala.dirX = odbicie(bala.dirX)
                if bala.posX + bala.dirX < 0 - bala.dirX:
                    bala.dirX = odbicie(bala.dirX)
                if bala.posY + bala.dirY < 0 - bala.dirY:
                    bala.dirY = odbicie(bala.dirY)
                # Odbijanie od kijasa
                if self.HEIGHT - 50 < bala.posY \
                        and kijas.posX < bala.posX + bala.dirX < kijas.posX + kijas.width:
                    bala.dirY = odbicie(bala.dirY)
                    if kijas.posX < bala.posX < kijas.posX + kijas.width / 8:
                        bala.dirX = -6
                    elif kijas.posX < bala.posX < kijas.posX + kijas.width / 4:
                        bala.dirX = -4
                    elif kijas.posX < bala.posX < kijas.posX + kijas.width / 2:
                        bala.dirX = -2
                    elif kijas.posX + bala.dirX == kijas.posX + kijas.width / 2:
                        bala.dirX = 0
                    elif kijas.posX + kijas.width - kijas.width / 8 < bala.posX < kijas.posX + kijas.width:
                        bala.dirX = 6
                    elif kijas.posX + kijas.width - kijas.width / 4 < bala.posX < kijas.posX + kijas.width:
                        bala.dirX = 4
                    elif kijas.posX + kijas.width - kijas.width / 2 < bala.posX < kijas.posX + kijas.width:
                        bala.dirX = 2
                pygame.draw.circle(self.SCREEN, bala.color, (bala.posX, bala.posY), bala.radius)
            for event in pygame.event.get():  # Przyciskanie przycisków
                if event.type == pygame.QUIT:
                    is_running = False
                    print("Exit")
                if event.type == pygame.KEYDOWN:
                    print("Key is pressed!")
                    if event.key == pygame.K_q:
                        is_running = False
                        print("Exit")
                    if event.key == pygame.K_i:
                        self.interpret("level.txt", self.matryca_bloczkow)
                    if event.key == pygame.K_u:
                        print(self.matryca_bloczkow)
                    if event.key == pygame.K_a:
                        self.add_bala()
                    if event.key == pygame.K_d:
                        self.pop_bala()
                    if event.key == pygame.K_x:
                        self.add_bloczek_matryca()
                    if event.key == pygame.K_h:  # Wypisanie matrycy bloczkow
                        for x, y in enumerate(self.matryca_bloczkow):
                            for z in y:
                                if z:
                                    print(y)
            keys = pygame.key.get_pressed()  # checking pressed keys continously
            if keys[pygame.K_UP]:
                self.add_bloczek_matryca()
            if keys[pygame.K_DOWN]:
                self.remove_bloczek_matryca(random.randrange(0, 16), random.randrange(0, 15))
            if keys[pygame.K_a]:
                self.add_bala()
            if keys[pygame.K_d]:
                self.pop_bala()
            if keys[pygame.K_o]:
                if kijas.width > 100:
                    kijas.width -= 10
            if keys[pygame.K_p]:
                if kijas.width < kijas_max:
                    kijas.width += 10
