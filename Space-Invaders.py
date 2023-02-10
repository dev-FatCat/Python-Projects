import pygame

pygame.init()

win = pygame.display.set_mode((750, 750))

pygame.display.set_caption('Space Invaders')

white = (255, 255, 255)

black = (0, 0, 0)

green = (0, 255, 0)

red = (255, 0, 0)

def redraw():
    win.fill(black)
    pygame.display.update()

run = True

while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redraw()

pygame.quit