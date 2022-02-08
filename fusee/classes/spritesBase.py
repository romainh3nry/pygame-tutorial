import pygame
from config import *


class SpriteBase(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, img):
        super().__init__()
        self.screen = screen
        self.img = pygame.image.load(img).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
