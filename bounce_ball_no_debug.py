#Ball Bouncing Physics
import pygame as pg
import sys
from pygame.locals import *
pg.init()
screen =  pg.display.set_mode((500,500))
clock = pg.time.Clock()
surface = pg.display.get_surface()
width = surface.get_width()
height = surface.get_height()
x = 100
y = 0
speedx = 8
speedy = 8
while True:
    clock.tick(20)
    screen.fill((0,0,0))
    pg.draw.circle(screen, (0,0,255), (x+20,y+20), 20)
    #x collisions
    if x + speedx + 40 > width:
        x += width - (x + 40)
    elif x + speedx < 0:
        x -= x - 0
    if x <= 0 or x + 40 >= width:
        speedx = -speedx
    #y collisions
    if y + speedy + 40 > height:
        y += height - (y + 40)
    elif y + speedy < 0:
        y -= y - 0
    if y <= 0 or y + 40 >= height:
        speedy = -speedy
    y += speedy
    x += speedx
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
