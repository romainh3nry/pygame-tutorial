import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Chap 4')
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)
white = pygame.Color(255, 255, 255)
orange = pygame.Color(255, 165, 0)
cyan = pygame.Color(0, 255, 255)
screen.fill(black)

# draw lines
points = [(0, 0), (50, 100), (100, 150), (250, 200), (400, 400)]
points2 = [(0, 0), (100, 50), (150, 100), (200, 250)]
pygame.draw.lines(screen, blue, False, points)
pygame.draw.lines(screen, green, True, points2)

# draw polygon
points3 = [(200, 200), (250, 300), (300, 325), (400, 350)]
pygame.draw.polygon(screen, yellow, points3)

# draw a circle
pygame.draw.circle(screen, white, (200, 200), 100, True)

# draw ellipse
xx_left = 100
yy_top = 150
small_axe = 100
big_axe = 200

pygame.draw.ellipse(screen, orange, (xx_left, yy_top, big_axe, small_axe), True)

# anti aliasing
pygame.draw.line(screen, cyan, (0, 200), (200, 0))
pygame.draw.line(screen, red, (0, 400), (400, 0))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
