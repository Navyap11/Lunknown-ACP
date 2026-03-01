import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rectangle and Text Example")

rect = pygame.Rect(200, 150, 200, 100)
rect_color = (0, 128, 255)

font = pygame.font.Font(None, 36)
text = font.render("Hello Pygame!", True, (255, 255, 255))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))
    pygame.draw.rect(window, rect_color, rect)
    window.blit(text, (220, 180))
    pygame.display.flip()
    clock.tick(60)