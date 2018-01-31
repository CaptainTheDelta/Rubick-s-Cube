# coding: utf-8

#----------------------------------- Import -----------------------------------

import numpy as np
import pygame
from pygame.locals import *

from fct_cube import *


#---------------------------------- Fonction ----------------------------------
RGB = [(255,165,0),(0,0,255),(255,0,0),
            (0,255,0),(255,255,0),(255,255,255)]

square_size = 50
espace = 10

def case(x,y):
    return (x,y,square_size,square_size)


def printcube(display):
    """Affiche le cube.

    Args:
        display (pygame): Fenetre python.
    """
    global cube

    def printface(X,Y,face):
        """Affiche l'une des faces du cube dans la fenêtre à la position X,Y.
    
        Args:
            X (int): Coordonées entières.
            Y (int): Coordonées entières.
            face (np.array): Tableau numpy 3x3 représentant une face.
        """
        for x,line in enumerate(face):
            for y,c in enumerate(line):
                pygame.draw.rect(
                    display, 
                    RGB[c],
                    case(
                        X + x * (square_size+espace),
                        Y + y * (square_size+espace)
                    )
                )

    l = 3 * (square_size + espace)

    pos = [(0,l), (l,l), (2*l,l),(3*l,l),(2*l,0),(2*l,2*l)]

    printface(*[p+espace for p in pos[0]],np.rot90(cube[0],2))

    for i in range(1,6):
        printface(*[p+espace for p in pos[i]],cube[i])