# coding: utf-8

# Pour l'ensemble des notations, se reporter aux images jointes.


#----------------------------------- Import -----------------------------------

import numpy as np
import os

#------------------------------------ Cube ------------------------------------

# Vue déplié du cube :

#     4
# 0 1 2 3
#     5

face = lambda c: np.array([c] * 9,int).reshape((3,3))

cube = np.array([face(c) for c in range(6)], int)


#--------------------------------- Mouvements ---------------------------------

# Rotations du cube

def x():
    #   4       2
    # 0123 -> 4153
    #   5       0
    cube[[0,4,2,5]] = np.roll(cube[[0,4,2,5]], -1, axis=0)

    cube[1] = np.rot90(cube[1])
    cube[3] = np.rot90(cube[3],-1)

def xp():
    cube[[0,4,2,5]] = np.roll(cube[[0,4,2,5]], -1, axis=0)

    cube[1] = np.rot90(cube[1],-1)
    cube[3] = np.rot90(cube[3])


def y():
    #   4       4
    # 0123 -> 1230
    #   5       5
    cube[:4] = np.roll(cube[:4], -1, axis=0)

    cube[5] = np.rot90(cube[5])
    cube[4] = np.rot90(cube[4],-1)

def yp():
    np.roll(cube[:4],1,axis=0)

    cube[5] = np.rot90(cube[5],-1)
    cube[4] = np.rot90(cube[4])


def z():
    #   4       1
    # 0123 -> 0524
    #   5       3
    cube[[1,4,3,5]] = np.roll(cube[[1,4,3,5]], 1, axis=0)

    cube[0] = np.rot90(cube[0])
    cube[2] = np.rot90(cube[2],-1)

def zp():
    cube[[1,4,3,5]] = np.roll(cube[[1,4,3,5]], -1, axis=0)

    cube[0] = np.rot90(cube[0],-1)
    cube[2] = np.rot90(cube[2])


# Rotations des milieux

def E():
    cube[:4,1] = np.roll(cube[:4,1], 1, axis=0)

def Ep():
    cube[:4,1] = np.roll(cube[:4,1], -1, axis=0)

def E2():
    cube[:4,1] = np.roll(cube[:4,1], 2, axis=0)


def M():
    cube[[0,4,2,5],:,1] = np.roll(cube[[0,4,2,5],:,1], 1, axis=0)

def Mp():
    cube[[0,4,2,5],:,1] = np.roll(cube[[0,4,2,5],:,1], 1, axis=0)

def M2():
    cube[[0,4,2,5],:,1] = np.roll(cube[[0,4,2,5],:,1], 2, axis=0)


def S():
    xp();E();x()

def Sp():
    xp();Ep();x()

def S2():
    xp();E2();x()


# Rotation des faces

def R():
    cube[[0,4,2,5],:,2] = np.roll(cube[[0,4,2,5],:,2], 1, axis=0)
    cube[3] = np.rot90(cube[3],-1)


def Rp():
    cube[[0,4,2,5],:,2] = np.roll(cube[[0,4,2,5],:,2], -1, axis=0)
    cube[3] = np.rot90(cube[3])

def R2():
    cube[[0,4,2,5],:,2] = np.roll(cube[[0,4,2,5],:,2], 2, axis=0)
    cube[3] = np.rot90(cube[3],2)


def L():
    cube[[0,4,2,5],:,0] = np.roll(cube[[0,4,2,5],:,0], -1, axis=0)
    cube[1] = np.rot90(cube[1],-1)

def Lp():
    cube[[0,4,2,5],:,0] = np.roll(cube[[0,4,2,5],:,0], 1, axis=0)
    cube[1] = np.rot90(cube[1])

def L2():
    cube[[0,4,2,5],:,0] = np.roll(cube[[0,4,2,5],:,0], 2, axis=0)
    cube[1] = np.rot90(cube[1],2)


def U():
    cube[:4,0] = np.roll(cube[:4,0], -1, axis=0)
    cube[4] = np.rot90(cube[4],-1)

def Up():
    cube[:4,0] = np.roll(cube[:4,0], 1, axis=0)
    cube[4] = np.rot90(cube[4])

def U2():
    cube[:4,0] = np.roll(cube[:4,0], 2, axis=0)
    cube[4] = np.rot90(cube[4],2)


def D():
    cube[:4,2] = np.roll(cube[:4,2], 1, axis=0)
    cube[4] = np.rot90(cube[4],-1)

def Dp():
    cube[:4,2] = np.roll(cube[:4,2], -1, axis=0)
    cube[4] = np.rot90(cube[4])

def D2():
    cube[:4,2] = np.roll(cube[:4,2], 2, axis=0)
    cube[4] = np.rot90(cube[4],2)


def F():
    y();L();yp()

def Fp():
    y();Lp();yp()

def F2():
    y();L2();yp()


def B():
    y();R();yp()

def Bp():
    y();Rp();yp()

def B2():
    y();R2();yp()


#--------------------------------- Affichage ----------------------------------
clear = lambda: os.system("cls") 
couleurs = ['O','B','R','G','Y','W']

def afficherCube():
    """Affiche le cube."""
    clear()

    lines = [[' '] * 8 + [couleurs[c] for c in l] for l in cube[4]]
    lines.append([''])

    for i in range(3):
        c = [couleurs[c] for c in cube[:4,i].ravel()]
        c.insert(-3,' ')
        c.insert(6,' ')
        c.insert(3,' ')
        lines.append(c)

    lines.append([''])
    lines += [[' '] * 8 + [couleurs[c] for c in l] for l in cube[5]]
    
    for l in lines:
        for c in l:
            print(' '+c,end ='')
        print()