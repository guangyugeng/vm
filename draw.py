import pygame
import random
import numpy as np
#

import sys


def drawPiont(x, y, screen):
    position = (x, y)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    screen.set_at(position, color)


# def drawPiont(screen, memory):
#     mem = memory[-100:]
#     print(type)
#     positions = np.array(mem).reshape((10, 10))
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     for i in range(len(positions)):
#         for j in range(len(positions[0])):
#             if positions[i][j] != 0:
#                 screen.set_at((i, j), color)


def main():
    width, height = 10, 10
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    fps = 30

    while running:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        drawPiont(x, y, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(fps)


def creat_screen():
    pygame.init()

    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption("My First Screen")

    while True:
        screen.fill((0,0,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    # main()
    creat_screen()

