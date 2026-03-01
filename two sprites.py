import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Controlled Sprite Game")

sprite1 = pygame.Rect(100, 150, 80, 80)  # controlled sprite
sprite2 = pygame.Rect(400, 150, 80, 80)  # static sprite

color1 = (255, 0, 0)
color2 = (0, 0, 255)

running = True
clock = pygame.time.Clock()
speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.x -= speed
    if keys[pygame.K_RIGHT]:
        sprite1.x += speed
    if keys[pygame.K_UP]:
        sprite1.y -= speed
    if keys[pygame.K_DOWN]:
        sprite1.y += speed

    # keep sprite1 inside the screen
    sprite1.x = max(0, min(sprite1.x, 600 - sprite1.width))
    sprite1.y = max(0, min(sprite1.y, 400 - sprite1.height))

    window.fill((0, 0, 0))
    pygame.draw.rect(window, color1, sprite1)
    pygame.draw.rect(window, color2, sprite2)
    pygame.display.flip()
    clock.tick(60)