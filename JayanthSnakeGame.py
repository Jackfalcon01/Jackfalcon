import pygame
from pygame.locals import *
import sys
from time import sleep

direction = "L"

# Colours
SnakeColor = (250, 250, 255)
BGColor = (50, 50, 50)
FoodColor = (255, 60, 60)

# global Variables
x = 15
y = 15

# pyGame Init
windowHeight, windowWidth = 600, 600
window = pygame.display.set_mode((windowHeight, windowWidth))
pygame.display.set_caption("SnakeGame")


def drawRect(Color, Coord):  # Draw Function
    xCoord = Coord[0] * 20
    yCoord = Coord[1] * 20
    pygame.draw.rect(window, Color, (yCoord, xCoord, 20, 20))


def refreshScreen():
    window.fill(BGColor)


def gameLoop():
    sleep(0.1)
    refreshScreen()
    global direction
    global x, y

    # U = up, D = Down , L=Left, R=right

    if direction == "U":
        y += 1
        drawRect(SnakeColor, (x, y))

    if direction == "D":
        y -= 1
        drawrect(SnakeColor, (x, y))

    if direction == "R":
        x += 1
        drawRect(SnakeColor, (x, y))

    if direction == "L":
        x -= 1
        drawRect(SnakeColor, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_w:
                if not direction == "D":
                    direction = "U"
            if event.key == pygame.K_s:
                if not direction == "U":
                    direction = "D"
            if event.key == pygame.K_a:
                if not direction == "R":
                    direction = "L"
            if event.key == pygame.K_d:
                if not direction == "L":
                    direction = "R"
    gameLoop()
    pygame.display.update()
