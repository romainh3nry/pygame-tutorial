import pygame
from config import *
from .planets import Planet
from .rocket import Rocket


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font(None, 24)
        self.points = 0
        self.score = self.font.render(f"{self.points} points", True, (255, 0, 0))
        self.rocket = Rocket(self.screen, XX_ROCKET, YY_ROCKET, "./img/FUSEE.png")
        self.planet_1 = Planet(self.screen, XX_PLANET, YY_PLANET, "./img/PLANETE.png")
        self.planet_2 = Planet(
            self.screen, XX_PLANET + XX_BETWEEN_PLANET, YY_PLANET + YY_BETWEEN_PLANET, "./img/PLANETE.png"
        )
        self.running = True
        self.clock = pygame.time.Clock()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_RIGHT:
                    self.rocket.move_right()
            elif event.type == pygame.KEYUP:
                self.rocket.move_left()

    def update_score(self):
        if self.planet_1.rect.y > HEIGHT - 10 or self.planet_2.rect.y > HEIGHT - 10:
            self.points += 1
            self.score = self.font.render(f"{self.points} points", True, (255, 0, 0))

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.screen.fill(BACKGROUND_COLOR)
            self.screen.blit(self.score, (0, 0))
            self.screen.blit(self.rocket.img, self.rocket.rect)
            self.screen.blit(self.planet_1.img, self.planet_1.rect)
            self.screen.blit(self.planet_2.img, self.planet_2.rect)

            self.handle_input()
            self.rocket.save_position()
            self.planet_1.scroll()
            self.planet_2.scroll()
            self.update_score()

            if self.rocket.rect.colliderect(self.planet_1) or self.rocket.rect.colliderect(self.planet_2):
                self.running = False
            pygame.display.update()
