from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def rec():
    x = 400
    y = 90
    while (x<780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.01)
    while y<570:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=2
        delay(0.01)
    while x>20:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=2
        delay(0.01)
    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=2
        delay(0.01)
    while x<400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.01)

def cir():
    theta = 180
    num = 0
    while True:
        clear_canvas_now()
        grass.draw_now(400,30)
        x1 = 250*math.sin(theta/360*2*math.pi)
        y1 = 250*math.cos(theta/360*2*math.pi)
        character.draw_now(400 + x1,340 + y1)
        theta += 2
        num += 2
        delay(0.01)
        if num == 360:
            break

while True:
   cir()
   rec()

close_canvas()
