import pygame
from arkanoid import Arkanoid

pygame.init()

WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN.fill(BLACK)
pygame.display.flip()


def text_to_screen(screen, text, x, y, size=50,
                   color=(255, 255, 255), font_type='Comic Sans MS'):
    try:

        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as e:
        print('Font Error, saw it coming')
        raise e


myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            print("Key is pressed!")
            if event.key == pygame.K_RETURN:
                print("wcisnelem enter")
                text_to_screen(SCREEN, "POZDRO DLA MILOSZA :D:D:D:D:D", 0, 0)
            if event.key == pygame.K_ESCAPE:
                print("Dzieki!")
                is_running = False
            if event.key == pygame.K_q:
                text_to_screen(SCREEN, "HEJO", 0, 0, color=RED)
            if event.key == pygame.K_w:
                text_to_screen(SCREEN, "HEJO", 0, 0, color=GREEN)
            if event.key == pygame.K_e:
                text_to_screen(SCREEN, "HEJO", 0, 0, color=BLUE)
            if event.key == pygame.K_r:
                text_to_screen(SCREEN, "HEJO", 0, 0, color=YELLOW)
            if event.key == pygame.K_c:
                pygame.draw.circle(SCREEN, WHITE, (100, 150), 10)
            if event.key == pygame.K_a:
                arkanoid = Arkanoid(SCREEN, WIDTH, HEIGHT)
                arkanoid.gra()
        pygame.display.flip()

pygame.quit()
