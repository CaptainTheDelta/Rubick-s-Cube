# coding: utf-8

#----------------------------------- Import -----------------------------------

import numpy as np
import pygame
from pygame.locals import *

from fct_cube import *

#--------------------------------- Variables ----------------------------------

CASE_SIZE = 40
ESPACE = CASE_SIZE // 5
EMPTY_SPACE = CASE_SIZE // 2

colors = ['O','B','R','G','Y','W']
RGB = [(255,127,0),(0,0,255),(255,0,0),
            (0,255,0),(255,255,0),(255,255,255)]
white = RGB[5]

#---------------------------------- Fonction ----------------------------------

clear = lambda: os.system("cls") 


def afficherCube():
    """Affiche le cube."""
    lines = [[' '] * 8 + [colors[c] for c in l] for l in cube[4]]
    lines.append([''])

    for i in range(3):
        c = [colors[c] for c in cube[:4,i].ravel()]
        c.insert(-3,' ')
        c.insert(6,' ')
        c.insert(3,' ')
        lines.append(c)

    lines.append([''])
    lines += [[' '] * 8 + [colors[c] for c in l] for l in cube[5]]
    
    for l in lines:
        for c in l:
            print(' '+c,end ='')
        print()


def case(x,y):
    return (x,y,CASE_SIZE,CASE_SIZE)


def print_cube(display):
    """Affiche le cube.

    Args:
        display (pygame): Fenetre python.
    """
    global cube
    width = CASE_SIZE + ESPACE

    def print_face(X,Y,face):
        """Affiche l'une des faces du cube dans la fenêtre à la position X,Y.
    
        Args:
            X (int): Coordonnée entière.
            Y (int): Coordonnée entière.
            face (np.array): Tableau numpy 3x3 représentant une face.
        """
        for y,line in enumerate(face):
            for x,c in enumerate(line):
                pygame.draw.rect(
                    display, 
                    RGB[c],
                    case(X + x * width, Y + y * width)
                )

    l = 2 * width + CASE_SIZE + EMPTY_SPACE 

    pos = [(0,l), (l,l), (2*l,l),(3*l,l),(2*l,0),(2*l,2*l)]

    # face0 = deepcopy(cube[0])
    # face0[:,[0,2]] = np.roll(face0[:,[0,2]],1,axis=1)

    # print_face(*[p+EMPTY_SPACE for p in pos[0]],face0)

    for i in range(6):
        print_face(*[p+EMPTY_SPACE for p in pos[i]],cube[i])


def print_text(display,text):
    """Affiche le texte text en haut à droite de la fenetre .

    Args:
        display (pygame): Fenêtre pygame.
        text (str): Texte à afficher.
    """
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, False, white)
    display.blit(label, (ESPACE,ESPACE))


def print_resolving(actions):
    """Affiche le cube à chaque étape de la résolution.
    Penser à remettre le cube à la situation initiale AVANT d'appeler cette 
    fonction.

    Args:
        actions (list): Liste des fonctions à exécuter.
    """
    # Initialisation de la fenêtre pygame.
    
    pygame.init()

    width = 3 * CASE_SIZE + 2 * ESPACE + EMPTY_SPACE
    screen = pygame.display.set_mode((4*width+EMPTY_SPACE,3*width+EMPTY_SPACE))
    pygame.display.set_caption("Rubick's Cube")

    clock = pygame.time.Clock()
    fps = 60

    # Affiche la position initiale
    print_cube(screen)

    c = True
    
    while c:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c = False


        try:
            txt = actions.pop(0)()
            
            screen.fill(0)
            print_text(screen,txt)
            print_cube(screen)
        
        except:
            pass

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
