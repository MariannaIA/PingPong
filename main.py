#print('Hello, World!')
import pygame as pg
pg.init()
from time import time as tm

def get_events():
    global run
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_w:
                player_1.speed = -5
            if e.key == pg.K_s:
                player_1.speed = 5
            if e.key == pg.K_UP:
                player_2.speed = -5
            if e.key == pg.K_DOWN:
                player_2.speed = 5
        if e.type == pg.KEYUP:
            if e.key == pg.K_w:
                player_1.speed = 0
            if e.key == pg.K_s:
                player_1.speed = 0
            if e.key == pg.K_UP:
                player_2.speed = 0
            if e.key == pg.K_DOWN:
                player_2.speed = 0
class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, x, y, w, h, speed,):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def update(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        self.rect.y += self.speed

class Ball(GameSprite):
    def init(self):
        self.speed_x = self.speed
        self.speed_y = self.speed
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 540:
            self.speed_y *= -1
        if self.rect.colliderect(player_1.rect) or self.rect.colliderect(player_2.rect):
            self.speed_x *= -1

win = pg.display.set_mode((1200,600))
pg.display.set_caption('Ping-pong')
win.fill((108, 149, 241))

run = True
finish = False
clock = pg.time.Clock()
start_game = False

player_1 = Player('racetca1.png', 20, 220, 100, 100, 0)
player_2 = Player('racetca2.png', 1080, 220, 100, 100, 0)
ball = Ball('ball.png', 560, 220, 60, 60, 5)
ball.init()

start = tm()
while run:
    get_events()
    if not finish:
        end = tm()
        if end - start > 3:
            start_game = True
        win.fill((108, 149, 241))
        player_1.move()
        player_1.update()
        player_2.move()
        player_2.update()
        if start_game:
            ball.move()
            ball.update()
        if ball.rect.x < 5:
            res = 'Player 1 losed!'
            finish = True
        if ball.rect.x > 1135:
            res = 'Player 2 losed!'
            finish = True
    else:
        label = pg.font.SysFont('verdana', 65).render(res, True, (255, 255, 255))
        win.blit(label, (373, 220))
    pg.display.update()
    clock.tick(60)