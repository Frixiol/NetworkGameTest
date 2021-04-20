import random
import pygame
import math

class Fruit:
    def __init__(self):
        self.x = random.randint(0,690)
        self.y = random.randint(0,690)
        self.width = 20
        self.height = 20
        self.color = (0,0,0)
        self.rect = (self.x, self.y, self.width, self.height)
        self.id = "fruit"

    def draw(self, win):
        pygame.draw.rect(win,self.color,self.rect)

    def collision(self,px,py,pwidth,pheight):
        sx = self.x+self.width/2
        sx = self.x + self.width / 2

        if px < self.x + self.width and px + pwidth > self.x:
            if py < self.y + self.height and py + pheight > self.y:
                self.position()
                return 1

        return 0

    def position(self):
        self.x = random.randint(0, 690)
        self.y = random.randint(0, 690)
        self.rect = (self.x, self.y, self.width, self.height)

class Bullet:
    def __init__(self,x,y,angle,shooter):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.rect = (self.x, self.y, self.width, self.height)
        self.id = "bullet"
        self.shooter = shooter
        self.dx = math.cos(angle)*5
        self.dy = math.sin(angle)*5

    def draw(self, win):
        pygame.draw.rect(win,self.color,self.rect)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.rect = (self.x, self.y, self.width, self.height)
        if self.x + self.width < 0 or 700 < self.x or self.y + self.height > 700 or 0 > self.y :
            return True
        return False

    def player_col(self, px, py, pwidth, pheight):
        sx = self.x + self.width / 2
        sx = self.x + self.width / 2

        if px < self.x + self.width and px + pwidth > self.x:
            if py < self.y + self.height and py + pheight > self.y:
                return True

        return False

    def define_numb(self,numb):
        self.numb = numb