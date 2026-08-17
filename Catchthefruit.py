import pygame
import random

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Catch the Fruit!")
ventana = pygame.display.set_mode((800, 600))

taza_x = 350
taza_s = 420
fruta_x = 400
fruta_y = 100
fruta_s = 300
fps = 60

def dibujar():
    ventana.fill((200, 200, 200))
    pygame.draw.rect(ventana, (100, 50, 200), (taza_x, 500, 100, 50))
    pygame.draw.circle(ventana, (200, 0, 0), (fruta_x, fruta_y), 25)

while True:
    dt = clock.tick(fps) / 1000

    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
        taza_x -= taza_s * dt
    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
        taza_x += taza_s * dt
    if taza_x < -100:
        taza_x = 800
    if taza_x > 800:
        taza_x = -100
    
    fruta_y += fruta_s * dt
    if fruta_y >= 625:
        fruta_y = -25
        fruta_x = random.randint(25, 775)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    dibujar()
    pygame.display.update()