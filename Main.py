import pygame
from sys import exit

# Initializes pygame
pygame.init()

# Setter størrelsesn på vinduet
screen = pygame.display.set_mode((800, 400))
# Display setter navn på vinduet
pygame.display.set_caption("BlackJack")
# time.clock gir en visualisering av tiden i vinduet som kjører
clock = pygame.time.Clock()

# While løkken venter på user input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

