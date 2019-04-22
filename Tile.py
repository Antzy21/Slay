from numpy import sin, pi
from Hexagon import Hexagon

class Tile:
    def __init__(self, gameDisplay, i, j, testSize, player):
        self.x = testSize * (i * 2 * (sin(pi/3))**2 + 1)
        if i % 2 == 0:
            self.y = testSize * (j * 2 * sin(pi/3) + 1)
        else:
            self.y = testSize * ((j * 2 * sin(pi/3) + 1) + sin(pi/3))
        self.i = i
        self.j = j
        self.player = player
        self.hex = Hexagon(gameDisplay, (self.x,self.y), size=testSize, color=self.player.color)
        self.hex.draw()
    contains = None
    highlighted = False
    province = None
    is_capital = False
    
    def highlight(self, grid):
        self.highlighted = True
        self.hex.highlight(50)
        if self.province != None:
            if self.is_capital:
                self.capital_refresh(grid)
                self.province.select(grid)
            if self.province.selected:
                self.select(grid)
    
    def capital_refresh(self, grid):
        self.hex.draw_with_text(str(self.province.money))
        self.hex.draw_house()

    def remove_highlight(self, grid):
        self.highlighted = False
        self.hex.highlight(-50)
        if self.province != None:
            if self.is_capital:
                self.hex.draw_with_text(str(self.province.money))
                self.hex.draw_house()
            if self.province.selected:
                self.select(grid)

    def is_moused_over(self, pos, grid):
        contained = self.hex.contains_position(pos)
        
        if self.province == None or not self.province.selected:
            if (contained and not self.highlighted):
                self.highlight(grid)
            elif (not contained and self.highlighted):
                self.remove_highlight(grid)
        return(self.highlighted)
    
    def select(self, grid):
        surroundings = self.surroundings(grid)
        for e, edge in enumerate(surroundings):
            try:
                extend_back = surroundings[e-1].province == self.province
            except AttributeError:
                extend_back = False
            try:
               extend_forward = surroundings[(e+1)%6].province == self.province
            except AttributeError:
                extend_forward = False
            if edge != None and edge.province == self.province:
                pass
            else:
                self.hex.draw_side(e, extend_back, extend_forward)

    def surroundings(self, grid):
        surroundings = []
        s = self.i%2
        
        try: # Above
            if self.j+(s-1) >= 0:
                surroundings.append(grid[self.i][self.j-1])
            else:
                surroundings.append(None)
        except IndexError:
            surroundings.append(None)
        
        try: # Top right
            if self.j+(s-1) >= 0:
                surroundings.append(grid[self.i + 1][self.j+(s-1)])
            else:
                surroundings.append(None)
        except IndexError:
            surroundings.append(None)

        try: # Bottom right
            surroundings.append(grid[self.i + 1][self.j+s])
        except IndexError:
            surroundings.append(None)
        
        try: # Below
            surroundings.append(grid[self.i][self.j+1])
        except IndexError:
            surroundings.append(None)
        
        try: # Bottom left
            if self.i-1 >= 0:
                surroundings.append(grid[self.i - 1][self.j+s])
            else:
                surroundings.append(None)
        except IndexError:
            surroundings.append(None)
        
        try: # Top left
            if self.j+(s-1) >= 0 and self.i-1 >= 0:
                surroundings.append(grid[self.i - 1][self.j+(s-1)])
            else:
                surroundings.append(None)
        except IndexError:
            surroundings.append(None)

        return(surroundings)
