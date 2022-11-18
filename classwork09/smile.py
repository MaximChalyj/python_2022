import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
circle(screen, (255, 0, 0), (150, 175), 20)
circle(screen, (0, 0, 0), (150, 175), 10)
circle(screen, (255, 0, 0), (250, 175), 15)
circle(screen, (0, 0, 0), (250, 175), 7.5)
polygon(screen, (0, 0, 0), [(100, 100/3**0.5 + 175 - 190/3**0.5),
                            (180, 180/3**0.5 + 175 - 190/3**0.5),
                            (180 + 10/2, 180/3**0.5 + 175 - 190/3**0.5 - 10*3**0.5/2),
                            (100 + 10/2, 100/3**0.5 + 175 - 190/3**0.5 - 10*3**0.5/2)])
polygon(screen, (0, 0, 0), [(220, 220/3**0.5 + 175 - 220/3**0.5),
                            (300, 220/3**0.5 + 175 - 300/3**0.5),
                            (300 - 10/2, 220/3**0.5 + 175 - 300/3**0.5 - 10*3**0.5/2),
                            (220 - 10/2, 220/3**0.5 + 175 - 220/3**0.5 - 10*3**0.5/2)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()