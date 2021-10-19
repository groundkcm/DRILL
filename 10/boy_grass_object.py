from pico2d import *
from random import randint

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = randint(100, 700), 90
        self.frame = 0

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

big = 0
class Ball:
    def __init__(self):
        global big
        big = (big + 1) % 4
        if big == 0:
            self.image_big = load_image('ball41x41.png')
        else:
            self.image = load_image('ball21x21.png')
        self.x, self.y = randint(100, 700), 599

    def update(self):
        global big
        big += 1
        if self.y <= 60:
            self.y = 60
            return
        self.y -= 0.5 * big

    def draw(self):
        global big
        big = (big + 1) % 4
        if big == 0:
            self.image_big.draw(self.x, self.y)
        else:
            self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
# boy = Boy()
team = [Boy() for i in range(10+1)]
group = [Ball() for i in range(20+1)]

running = True
# game main loop code
while running:

    handle_events()

    big = 0
    for ball in group:
        ball.update()
    for boy in team:
        boy.update()

    big = 0
    clear_canvas()
    grass.draw()
    for ball in group:
        ball.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)
# finalization code