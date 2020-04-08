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
        # position = (x, y)
        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        # color = (r, g, b)
        # screen.set_at(position, color)
        drawPiont(x, y, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(fps)


def creat_screen():
    #初始化pygame
    pygame.init()

    #设置窗口大小并保存在screen对象中
    screen = pygame.display.set_mode((500,500))

    #设置窗口的名字
    pygame.display.set_caption("My First Screen")

    #游戏的主循环
    while True:
        #给屏幕填充蓝色
        screen.fill((0,0,255))

        #侦听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #先退出pygame窗口，再退出程序
                pygame.quit()
                sys.exit()

        #更新整个待显示的 Surface 对象到屏幕上
        pygame.display.flip()


if __name__ == '__main__':
    # main()
    creat_screen()

    # screen = pygame.display.set_mode((13, 12))
    # position = (1, 1)
    # r = random.randint(0, 255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)
    # color = (r, g, b)
    # screen.set_at(position, color)
    # pygame.display.flip()
