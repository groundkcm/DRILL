from random import randint
from pico2d import *
import game_world
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)  # 10 픽셀에 3, 새의 크기는 100픽셀 -> 30 cm
RUN_SPEED_KMPH = 1.0  # 속도 1km/H
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, self.num = randint(100, 1500), randint(150, 500), randint(1, 2)
        self.velocity = 1
        self.frame = 0
        if self.num == 1:
            self.dir = -1
        else:
            self.dir = 1

    # def get_bb(self):
    #     # fill here
    #     return 0,0,0,0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # fill here for draw

    def update(self):
        self.velocity += RUN_SPEED_PPS * self.dir
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.x >= 1600 - 150 and self.dir == 1:
            self.dir = -1
        elif self.x <= 50 and self.dir == -1:
            self.dir = 1
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(50, self.x, 1600 - 100)

    #fill here for def stop
