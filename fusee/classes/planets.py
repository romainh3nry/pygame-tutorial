import pygame
from config import *
from .spritesBase import SpriteBase


class Planet(SpriteBase):
    def __init__(self, screen, x, y, img):
        super().__init__(screen, x, y, img)
        self.width = WIDTH_PLANET
        self.height = HEIGHT_PLANET
        self.speed = 3

    def scroll(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = randint(50, 500)
            self.rect.y = 25
