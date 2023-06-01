import pygame
from sys import exit

# Initializes pygame
pygame.init()

# Setter størrelsesn på vinduet
screen = pygame.display.set_mode((800, 400))
# display setter navn på vinduet
pygame.display.set_caption("BlackJack")

clock = pygame.time.Clock()
# Henter bilde til bakgrunn
table_surface = pygame.image.load(r"C:\Users\Boers\PycharmProjects\FirstPyGame\bilder\card_table.png")
card_ace = pygame.image.load(r"C:\Users\Boers\PycharmProjects\FirstPyGame\bilder\ace.png")

# While løkken venter på user input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(table_surface, (0, 0))
    screen.blit(card_ace, (150, 125))

    pygame.display.update()
    clock.tick(60)



