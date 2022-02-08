import pygame
from config import *
from .spritesBase import SpriteBase


class Rocket(SpriteBase):
    def __init__(self, screen, x, y, img):
        super().__init__(screen, x, y, img)
        self.width = WIDTH_ROCKET
        self.height = HEIGHT_ROCKET
        self.speed = 0

    def move_right(self):
        self.speed = 4

    def move_left(self):
        self.speed = -4

    def save_position(self):
        self.rect.x += self.speed
