import pygame
pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Bubble Blaster")

clock = pygame.time.Clock()

x = y = 150

points = [[-20, -20], [30, 0], [-20, 20]]

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

    new_points = [[x1 + x, y1 + y] for x1, y1 in points]
    
    screen.fill((0, 0, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 2)
    pygame.draw.polygon(screen, (255, 0, 0), new_points)
    pygame.display.flip()
    clock.tick(60)