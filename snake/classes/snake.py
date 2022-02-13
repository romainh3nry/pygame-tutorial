import pygame
from config import *


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./img/TETE.png").convert_alpha()
        self.head = self.image
        self.rect = self.image.get_rect()
        self.rect.x = WIN_WIDTH / 2
        self.rect.y = WIN_HEIGHT / 2
        self.speed = 4
        self.direction = "LEFT"
        self.group = pygame.sprite.Group()

    def update(self):
        current_x = self.rect.x
        current_y = self.rect.y

        if self.direction == 'LEFT':
            self.image = pygame.transform.rotate(self.head, 90)
            self.rect.x -= self.speed
        elif self.direction == 'RIGHT':
            self.image = pygame.transform.rotate(self.head, -90)
            self.rect.x += self.speed
        elif self.direction == 'UP':
            self.image = pygame.transform.rotate(self.head, 0)
            self.rect.y -= self.speed
        elif self.direction == 'DOWN':
            self.image = pygame.transform.rotate(self.head, 180)
            self.rect.y += self.speed
