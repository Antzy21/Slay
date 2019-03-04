import pygame
import numpy as np
import random
import time

pygame.init()

clock = pygame.time.Clock()

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
cyan = (0, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (255, 0, 255)
colors = [blue, green, red, cyan, purple]

Dy = np.sin(np.pi/3)
Dx = np.cos(np.pi/3)

dimensions = 500
displaySize = (dimensions, dimensions)
gameDisplay = pygame.display.set_mode(displaySize)

class Position:
    def __init__(self, x, y, i, j, player):
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.player = player
        self.color = colors[player]
    contains = None

class Province:
    tiles = []
    money = 0

    def add(self, tile):
        self.tiles.append(tile)
    def combine(self,prov2):
        self.tiles.extend(prov2.tiles)
        self.money += prov2.money
        del prov2

class Kingdom:
    provinces = []

class Tree:
    def __init__(self, pos):
        self.position = pos

    def display(self):
        pygame.draw.rect(gameDisplay, white, (self.position.x, self.position.y, 10, 30))

def make_hex(x, y, size=40, color=green):
    dy = Dy*size
    dx = Dx*size
    points = [(x-size, y),
              (x-dx, y+dy),
              (x+dx, y+dy),
              (x+size, y),
              (x+dx, y-dy),
              (x-dx, y-dy)]
    pygame.draw.polygon(gameDisplay, color, points)
    pygame.draw.polygon(gameDisplay, white, points, 3)

def message_display(text='"insert text"', text_size=20, position=(dimensions/2, dimensions/2), colour=white):
    large_text = pygame.font.Font('freesansbold.ttf', text_size)
    text_surface = large_text.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    gameDisplay.blit(text_surface, text_rect)

def make_hex_with_text(x, y, text, color, size=40):
    make_hex(x, y, size, color)
    message_display(text, position=(x, y))

def display(grid):
    for row in grid:
        for hex in row:
            make_hex_with_text(hex.x, hex.y, str(hex.i)+str(hex.j), hex.color)
            pygame.display.update()

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        clock.tick(60)
        pygame.display.update()

def setup(seed, testSize=40):
    if seed is None:
        grid = []
    else:
        grid = []
    for i in range(0, gridX-1):
        grid.append([])
        for j in range(0, gridY-1):
            player = random.randint(0,4)
            x = testSize * (i * 2 * Dy * Dy + 1)
            y = testSize * (j * 2 * Dy + 1)
            s = testSize * Dy
            if i % 2 == 0:
                grid[i].append(Position(x, y, i, j, player))
            else:
                grid[i].append(Position(x, y+s, i, j, player))
    return grid

def findProvinces(grid):
    for row in grid:
        for hex in row:
            print(hex.color)
            for sur in surroundings(grid, hex):
                if sur.color == hex.color:
                    '''They need connecting'''

def surroundings(grid, hex):
    surroundings = []
    if hex.j > 0: # Above
        surroundings.append(grid[hex.i - 1][hex.j])
    if hex.i%2==1 or hex.j != 0:
        if hex.i > 0: # Top left
            surroundings.append(grid[hex.i - 1][hex.j-1])
        if hex.i < gridX:  # Top right
            surroundings.append(grid[hex.i + 1][hex.j])
    if hex.i%2==0 or hex.j != gridY:
        if hex.i > 0: # Bottom left
            surroundings.append(grid[hex.i - 1][hex.j+1])
        if hex.i < gridX:  # Bottom right
            surroundings.append(grid[hex.i + 1][hex.j])
    if hex.i < gridX-1: # Below
        surroundings.append(grid[hex.i - 1][hex.j])
    return surroundings

gridX = 6
gridY = 7
grid = setup(seed = None)
display(grid)
# findProvinces(grid)
game()
