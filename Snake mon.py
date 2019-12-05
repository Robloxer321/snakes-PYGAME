import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx =1, dirny=0, color=(255, 0, 0)):

    def move(self, dirnx, dirny):

    def draw(self, surface, eyes=False):
    
class snake(object):
    body =[ ]
    turns = { }
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self,head)
        self.dirnx = 0
        self.dirny = 1

    def move (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys  = pygame.key.get_pressed()

            for key in keys:
                if keys [pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[ : ]] = [ self.dirnx, self.dirny]

                elif keys [pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[ : ]] = [ self.dirnx, self.dirny]

               elif keys [pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[ : ]] = [ self.dirnx, self.dirny]

                elif keys [pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[ : ]] = [ self.dirnx, self.dirny]
        for i, c in enumerate(self.body):
            p = c.pos[ : ]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len (self.body)-1:
                    self.turns.pop(p)
                
        
def drawGrid(w, rows, surface):
    sizeting = w // rows

    x = 0
    y=0
    for 1 in range(rows):
        x = x + sizeting
        y = y+ sizeting

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w)
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y)
                          
                         
def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()

    
def main():
    global rows, width
    width = 600
    height = 600
    rows =30
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0)), (10,10)
    flag = true

    clock = pyagme.time.Clock()
    
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)
        
    
    
