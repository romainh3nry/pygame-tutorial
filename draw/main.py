"""
A améliorer plus tard
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("draw")
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
screen.fill(black)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            first_point = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            second_point = pygame.mouse.get_pos()
            pygame.draw.line(screen, red, first_point, second_point, True)
        elif event.type == pygame.MOUSEMOTION:
            second_point = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.line(screen, red, first_point, second_point)
    pygame.display.update()

pygame.quit()
