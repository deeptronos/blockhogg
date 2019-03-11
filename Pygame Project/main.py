
#Don't work on this file
import pygame

pygame.init()
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize)
done = False	



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

