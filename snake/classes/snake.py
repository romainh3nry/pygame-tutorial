import pygame
from config import *


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/TETE.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIN_WIDTH / 2
        self.rect.y = WIN_HEIGHT / 2
