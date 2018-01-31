# coding: utf-8

#----------------------------------- Import -----------------------------------

import pygame
from pygame.locals import *

from fct_cube import *
from fct_aff import *


#--------------------------------- Main Loop ----------------------------------

pygame.init()
DISPLAY = pygame.display.set_mode((730, 550))
pygame.display.set_caption("Rubick's Cube")
clock = pygame.time.Clock()
fps = 30

c = True

while c:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c = False

    # Code à ajouter ici :
    # 
    # Résolution du cube étape par étape.
    # 
    # 


    printcube(DISPLAY)
    pygame.display.update()
    clock.tick(fps)


pygame.quit()