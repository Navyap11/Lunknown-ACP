import pygame
import random

pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sprite Color Change")

sprite1 = pygame.Rect(100, 150, 80, 80)
sprite2 = pygame.Rect(400, 150, 80, 80)

color1 = (255, 0, 0)
color2 = (0, 0, 255)

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)  # change colors every 1 second

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    window.fill((0, 0, 0))
    pygame.draw.rect(window, color1, sprite1)
    pygame.draw.rect(window, color2, sprite2)
    pygame.display.flip()
    clock.tick(60)