import pygame
from config import *
from .snake import Snake


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("SNAKE")
        self.group = pygame.sprite.Group()
        self.snake = Snake()
        self.clock = pygame.time.Clock()

    def run(self):

        running = True
        self.group.add(self.snake)
        while running:
            self.clock.tick(60)
            self.screen.fill(WHITE)
            self.group.draw(self.screen)
            self.group.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
                        self.snake.direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
                        self.snake.direction = 'RIGHT'
                    elif event.key == pygame.K_UP and self.snake.direction != 'DOWN':
                        self.snake.direction = 'UP'
                    elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
                        self.snake.direction = 'DOWN'

            pygame.display.update()
