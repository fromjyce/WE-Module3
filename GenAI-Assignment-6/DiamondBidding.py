import pygame
import sys
import time

pygame.init()

#screen width
width = 800
height = 600

background_color = (13, 116, 47)  # green

#screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame Window")

#images for splash screen
image1 = pygame.image.load(r'C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\Name.png')
image2 = pygame.image.load(r'C:\Users\jaya2\Visual Code\Module3\GenAI-Assignment-6\Images\PyGame.png')

image1_width = 250
image1_height = 250
image2_width = 315
image2_height = 175

image1 = pygame.transform.scale(image1, (image1_width, image1_height))
image2 = pygame.transform.scale(image2, (image2_width, image2_height))


def splash_screen():
    screen.fill(background_color)

    screen.blit(image1, ((width - image1_width) // 2, (height - image1_height) // 4))
    
    font = pygame.font.SysFont(None, 35)
    text_surface = font.render("Developed using", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, (height // 2) + 30))  
    screen.blit(text_surface, text_rect)

    screen.blit(image2, ((width - image2_width) // 2, (height - image2_height) // 4 * 3))

    pygame.display.flip()
    time.sleep(10)

def main_screen():
    screen.fill(background_color)
    
    font = pygame.font.SysFont(None, 48)
    text = font.render("Hello World", True, (255, 255, 255))  
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()


splash_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_screen()


pygame.quit()
sys.exit()
