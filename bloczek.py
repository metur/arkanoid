import pygame


class Bloczek:
    def __init__(self, screen, posx, posy, durability=1, color="GRAY", typ="regular"):
        self.screen = screen
        self.color = color
        self.width = 50
        self.height = 25
        self.posX = posx
        self.posY = posy
        self.durability = durability
        self.typ = typ

    def __getitem__(self, item):
        return getattr(self, item)

    def get_x(self):
        return self.posX

    def get_y(self):
        return self.posY

    def draw_bloczek(self):
        if self.color == "RED":
            self.color = (1, 0, 0)
        elif self.color == "GREEN":
            self.color = (0, 1, 0)
        elif self.color == "BLUE":
            self.color = (0, 0, 1)
        elif self.color == "GRAY":
            self.color = (1, 1, 1)

        if self.durability == 1:
            color = tuple(64*x for x in self.color)
        elif self.durability == 2:
            color = tuple(128*x for x in self.color)
        elif self.durability == 3:
            color = tuple(192*x for x in self.color)
        elif self.durability == 4:
            color = tuple(255*x for x in self.color)
        pygame.draw.rect(self.screen, color, [self.posX, self.posY, self.width, self.height])
