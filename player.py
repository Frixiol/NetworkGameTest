import  pygame
import random
import math

class Player():
    def __init__(self,id):
        self.id = id
        self.data = "player"
        self.x = random.randint(0, 690)
        self.y = random.randint(0, 690)
        self.width = 50
        self.height = 50
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.rect = (self.x,self.y,self.width,self.height)
        self.vel = 3
        self.score = 0
        self.health = 100


    def draw(self, win):
        pygame.draw.rect(win,self.color,self.rect)
        pygame.draw.rect(win,(230,0,0),(self.x-25,self.y-20,self.health,10))
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render(str(self.score), 1, (20, 20, 20))
        win.blit(text, (self.x+10,self.y+10))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x,self.y,self.width, self.height)

    def rotate(self):
        mouse_x,mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.angle = math.atan2(rel_y,rel_x)
        return self.angle

    def position(self):
        self.score -= 1
        self.x = random.randint(0, 690)
        self.y = random.randint(0, 690)
        self.update()