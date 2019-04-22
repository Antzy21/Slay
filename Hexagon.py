import numpy as np
from HexSidesEnum import HexSidesEnum
from numpy import sin, cos, tan, pi
import pygame
from messageDisplay import message_display

class Hexagon:

    def __init__(self, gameDisplay, centre, size, color):
        self.x, self.y = centre
        self.colour = color
        self.size = size
        dy = sin(pi/3)*size
        dx = cos(pi/3)*size
        self.corners = [(self.x-dx, self.y-dy),
                        (self.x+dx, self.y-dy),
                        (self.x+size, self.y),
                        (self.x+dx, self.y+dy),
                        (self.x-dx, self.y+dy),
                        (self.x-size, self.y)
                        ]
        self.gameDisplay = gameDisplay
    
    def draw_side(self, side, extend_back, extend_forward):
        n1 = self.corners[side]
        n2 = self.corners[(side+1)%6]
        p1 = ((9*n1[0]+self.x)/10,
              (9*n1[1]+self.y)/10)
        p2 = ((9*n2[0]+self.x)/10,
              (9*n2[1]+self.y)/10)
        if extend_back:
            p1 = (p1[0]+(p1[0]-p2[0])/8,
                  p1[1]+(p1[1]-p2[1])/8)
        if extend_forward:
            p2 = (p2[0]+(p2[0]-p1[0])/8,
                  p2[1]+(p2[1]-p1[1])/8)
        pygame.draw.line(self.gameDisplay, (255,255,255), p1, p2, 4)

    def draw(self):
        pygame.draw.polygon(self.gameDisplay, self.colour, self.corners)
        pygame.draw.polygon(self.gameDisplay, (0,0,0), self.corners, 3)

    def draw_with_text(self, text=""):
        self.draw()
        message_display(self.gameDisplay, (self.x,self.y), text)

    def draw_house(self):
        points = [(self.x, self.y-self.size*2/3),
                  (self.x+self.size*2/3, self.y),
                  (self.x+self.size*1/2, self.y),
                  (self.x+self.size*1/2, self.y+self.size*2/3),
                  (self.x+self.size/9, self.y+self.size*2/3),
                  (self.x+self.size/9, self.y+self.size*1/3),
                  (self.x-self.size/9, self.y+self.size*1/3),
                  (self.x-self.size/9, self.y+self.size*2/3),
                  (self.x-self.size*1/2, self.y+self.size*2/3),
                  (self.x-self.size*1/2, self.y),
                  (self.x-self.size*2/3, self.y)]
        pygame.draw.polygon(self.gameDisplay, (255,255,255), points, 3)


    def highlight(self, change):
        c = self.colour
        self.colour = (c[0]+change, c[1]+change, c[2]+change)
        self.draw()

    def contains_position(self, pos):
        mouse_x, mouse_y = pos
        
        dy = sin(pi/3)*self.size
        dx = cos(pi/3)*self.size

        if self.x-dx <= mouse_x <= self.x+dx:
            if self.y-dy < mouse_y < self.y+dy:
                return True
        elif mouse_x > self.x+dx:
            if mouse_y >= self.y:
                return (linearInequality((self.x+self.size,self.y),(self.x+dx,self.y+dy),(mouse_x,mouse_y)))
            elif mouse_y < self.y:
                return (not linearInequality((self.x+self.size,self.y),(self.x+dx,self.y-dy),(mouse_x,mouse_y)))
        elif mouse_x < self.x-dx:
            if mouse_y >= self.y:
                return (linearInequality((self.x-self.size,self.y),(self.x-dx,self.y+dy),(mouse_x,mouse_y)))
            elif mouse_y < self.y:
                return (not linearInequality((self.x-dx,self.y-dy),(self.x-self.size,self.y),(mouse_x,mouse_y)))
        return False
    
def linearInequality(A=(0,5),B=(3,0),pos=(0,0)):
    g = (A[1]-B[1])/(A[0]-B[0])
    t = pos[1]-A[1] < g*(pos[0]-A[0])
    return(t)
