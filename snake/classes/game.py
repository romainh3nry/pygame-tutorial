import pygame
from config import *
from .snake import Snake


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.screen.fill(WHITE)
        pygame.display.set_caption("SNAKE")
        self.snake_group = pygame.sprite.Group()
        self.snake = Snake()

    def run(self):

        running = True
        while running:

            self.snake_group.add(self.snake)
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def update(self):
        self.snake_group.draw(self.screen)
        pygame.display.update()
