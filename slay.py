import pygame
from Player import Player
from Tile import Tile
import numpy as np
import random
import time

pygame.init()

clock = pygame.time.Clock()

number_of_players = 4
size = 50
gridX = 10
gridY = 10

d_x = int(((2-np.cos(np.pi/3))*gridX+np.cos(np.pi/3))*size)
d_y = int(((2*np.sin(np.pi/3))*gridY+1)*size)
displaySize = (d_x, d_y)
gameDisplay = pygame.display.set_mode(displaySize)

def update_display(gameDisplay, grid, mouse_pos):
    for row in grid:
        for tile in row:
            tile.is_moused_over(mouse_pos, grid)
    pygame.display.update()

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse_pos = pygame.mouse.get_pos()
        clock.tick(30)
        update_display(gameDisplay, grid, mouse_pos)                      

def setup(seed, number_of_players, testSize=40):
    players = []
    for n in range(number_of_players):
        players.append(Player(n))
    if seed is None:
        grid = []
    else:
        grid = []
    for i in range(0, gridX):
        grid.append([])
        for j in range(0, gridY):
            player = players[random.randint(0,number_of_players-1)] 
            grid[i].append(Tile(gameDisplay, i, j, testSize, player))
            pygame.display.update()
            surroundings = grid[i][j].surroundings(grid)
            for neighbour in surroundings:
                if neighbour == None:
                    pass
                elif neighbour.player.number == grid[i][j].player.number:
                    if grid[i][j].province == None and neighbour.province == None:
                        player.new_province(grid[i][j],neighbour)
                    elif neighbour.province != None:
                        neighbour.province.evaluate_new_tile(grid[i][j])
                    elif grid[i][j].province != None:
                        grid[i][j].province.evaluate_new_tile(neighbour)
    for player in players:
        for province in player.provinces:
            province.money = province.size
            province.capital.capital_refresh(grid)





    return grid

grid = setup(None, number_of_players, size)
# findProvinces(grid)
game()
