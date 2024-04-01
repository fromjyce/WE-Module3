import pygame
import sys

pygame.init()

width = 950
height = 750

background_color = (13, 116, 47)  # usual green colour

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Diamond Bidding Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    pygame.display.flip()

pygame.quit()
sys.exit()
