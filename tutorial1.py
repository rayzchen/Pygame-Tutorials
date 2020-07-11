import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame")

rect = pygame.Rect(100, 100, 100, 100)
clock = pygame.time.Clock()

x = y = 150

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]: x += 5
    if pressed[pygame.K_a]: x -= 5
    if pressed[pygame.K_w]: y -= 5
    if pressed[pygame.K_s]: y += 5
    rect.centerx = x
    rect.centery = y
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.flip()
    clock.tick(60)