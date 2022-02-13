import pygame


class Carre(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200

        self.move = 3

    def update(self):
        self.rect.x += self.move
        if self.rect.x > 320:
            self.rect.x = 320
            self.move = -3
        elif self.rect.x <= 0:
            self.rect.x = 0
            self.move = 3


pygame.init()
screen = pygame.display.set_mode((400, 400))
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 255))
screen.blit(background, (0, 0))

pygame.display.set_caption("Bouncing Square")
clock = pygame.time.Clock()

x = 300
move = 3

all_sprites = pygame.sprite.Group()
carre = Carre()
all_sprites.add(carre)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    all_sprites.clear(screen, background)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
