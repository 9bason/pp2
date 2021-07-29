import pygame
from random import randint

pygame.init()

pygame.mixer.init()

size = (1024, 720)
fps = 30  # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.update()

background = 'background.png'
background = pygame.image.load(background)
background = pygame.transform.scale(background, size)

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

block_size = 20

player_x, player_y = 500, 500
x_diff, y_diff = 0, 0

counter = 0

foods = []


class Unit:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,
                                y,
                                block_size * 2,
                                block_size)

    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())

    def get_rect(self):
        return pygame.Rect(self.x,
                           self.y,
                           block_size * 2,
                           block_size)


player = Unit(BLUE, player_x, player_y)

score = 0

done = False
# Game loop
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            y_diff = -10
        if keys[pygame.K_DOWN]:
            y_diff = 10
        if keys[pygame.K_RIGHT]:
            x_diff = 10
        if keys[pygame.K_LEFT]:
            x_diff = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_diff = 0
            if event.key == pygame.K_DOWN:
                y_diff = 0
            if event.key == pygame.K_RIGHT:
                x_diff = 0
            if event.key == pygame.K_LEFT:
                x_diff = 0

    player.x += x_diff
    player.y += y_diff

    screen.blit(background, (0, 0))

    player.display(screen)

    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(f'Score: {score}', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (50, 50)
    screen.blit(text, textRect)

    counter += 1
    counter %= fps * 2

    if counter % (fps // 2) == 0:
        foods.append(Unit(RED, randint(10, size[0] - 10), 0))
    if counter % (fps) == 0:
        foods.append(Unit(GREEN, randint(10, size[0] - 10), size[1]))

    for food in foods:
        if food.color == RED:
            food.y += 5
        if food.color == GREEN:
            food.y -= 5
            food.x += randint(-3,3)

    for i, food in enumerate(foods):
        if food.y > size[1] or food.y < 0:
            del foods[i]

    for i, food in enumerate(foods):
        if player.get_rect().colliderect(food.get_rect()):
            del foods[i]
            if food.color == RED:
                score -= 1
            else:
                score += 1

    for food in foods:
        food.display(screen)

    pygame.display.flip()
    clock.tick(fps)
