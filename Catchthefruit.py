import pygame
import random

pygame.init()
pygame.display.set_caption("Catch the Fruit!")
ventana = pygame.display.set_mode((800, 600))

taza_x = 350

def dibujar():
    ventana.fill((200, 200, 200))
    pygame.draw.rect(ventana, (100, 50, 200), (taza_x, 500, 100, 50))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    dibujar()
    pygame.display.update()