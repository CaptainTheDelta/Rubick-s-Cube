# coding: utf-8

# Pour l'ensemble des notations, se reporter aux images jointes.


#----------------------------------- Import -----------------------------------

import numpy as np
from copy import deepcopy
import os

#------------------------------------ Cube ------------------------------------

# Vue déplié du cube :

#     4
# 0 1 2 3
#     5

cube = None

def init_cube():
    """Renvoie le cube de base.

    Return
        (np.array): Cube.
    """
    face = lambda c: np.array([c] * 9,int).reshape((3,3))

    return np.array([face(c) for c in range(6)], int)

def copy_cube():
    """Renvoie un instané du cube.

    Return:
        (np.array): Cube.
    """
    return deepcopy(cube)


cube = init_cube()

#--------------------------------- Mouvements ---------------------------------

# Rotations du cube

def x():
    #   4       2
    # 0123 -> 4153
    #   5       0
    cube[[0,4,2,5]] = np.roll(cube[[0,4,2,5]], -1, axis=0)

    cube[1] = np.rot90(cube[1])
    cube[3] = np.rot90(cube[3],-1)
    return 'x'

def xp():
    cube[[0,4,2,5]] = np.roll(cube[[0,4,2,5]], 1, axis=0)

    cube[1] = np.rot90(cube[1],-1)
    cube[3] = np.rot90(cube[3])
    return 'xp'


def y():
    #   4       4
    # 0123 -> 1230
    #   5       5
    cube[:4] = np.roll(cube[:4], -1, axis=0)

    cube[5] = np.rot90(cube[5])
    cube[4] = np.rot90(cube[4],-1)
    return 'y'

def yp():
    np.roll(cube[:4],1,axis=0)

    cube[5] = np.rot90(cube[5],-1)
    cube[4] = np.rot90(cube[4])
    return 'yp'


def z():
    #   4       1
    # 0123 -> 0524
    #   5       3
    cube[[1,4,3,5]] = np.roll(cube[[1,4,3,5]], 1, axis=0)

    cube[0] = np.rot90(cube[0])
    cube[2] = np.rot90(cube[2],-1)
    return 'z'

def zp():
    cube[[1,4,3,5]] = np.roll(cube[[1,4,3,5]], -1, axis=0)

    cube[0] = np.rot90(cube[0],-1)
    cube[2] = np.rot90(cube[2])
    return 'zp'


# Rotations des milieux

def E():
    cube[:4,1] = np.roll(cube[:4,1], 1, axis=0)
    return 'E'

def Ep():
    cube[:4,1] = np.roll(cube[:4,1], -1, axis=0)
    return 'Ep'

def E2():
    cube[:4,1] = np.roll(cube[:4,1], 2, axis=0)
    return 'E2'


def M():
    cube[[0,4,2,5],:,1] = np.roll(cube[[0,4,2,5],:,1], 1, axis=0)
    return 'M'

def Mp():
    cube[[0,4,2,5],:,1] = np.roll(cube[[0,4,2,5],:,1], 1, axis=0)
    return 'Mp'

def M2():
    cube[[0,4,2,5],:,1] = np.roll(cube[[0,4,2,5],:,1], 2, axis=0)
    return 'M2'


def S():
    xp();E();x()
    return 'S'

def Sp():
    xp();Ep();x()
    return 'Sp'

def S2():
    xp();E2();x()
    return 'S2'


# Rotation des faces

def R():
    cube[[0,4,2,5],:,2] = np.roll(cube[[0,4,2,5],:,2], -1, axis=0)
    cube[3] = np.rot90(cube[3])
    return 'R'


def Rp():
    cube[[0,4,2,5],:,2] = np.roll(cube[[0,4,2,5],:,2], 1, axis=0)
    cube[3] = np.rot90(cube[3],-1)
    return 'Rp'

def R2():
    cube[[0,4,2,5],:,2] = np.roll(cube[[0,4,2,5],:,2], 2, axis=0)
    cube[3] = np.rot90(cube[3],2)
    return 'R2'


def L():
    cube[[0,4,2,5],:,0] = np.roll(cube[[0,4,2,5],:,0], -1, axis=0)
    cube[1] = np.rot90(cube[1],-1)
    return 'L'

def Lp():
    cube[[0,4,2,5],:,0] = np.roll(cube[[0,4,2,5],:,0], 1, axis=0)
    cube[1] = np.rot90(cube[1])
    return 'Lp'

def L2():
    cube[[0,4,2,5],:,0] = np.roll(cube[[0,4,2,5],:,0], 2, axis=0)
    cube[1] = np.rot90(cube[1],2)
    return 'L2'


def U():
    cube[:4,0] = np.roll(cube[:4,0], -1, axis=0)
    cube[4] = np.rot90(cube[4],-1)
    return 'U'

def Up():
    cube[:4,0] = np.roll(cube[:4,0], 1, axis=0)
    cube[4] = np.rot90(cube[4])
    return 'Up'

def U2():
    cube[:4,0] = np.roll(cube[:4,0], 2, axis=0)
    cube[4] = np.rot90(cube[4],2)
    return 'U2'


def D():
    cube[:4,2] = np.roll(cube[:4,2], 1, axis=0)
    cube[4] = np.rot90(cube[4],-1)
    return 'D'

def Dp():
    cube[:4,2] = np.roll(cube[:4,2], -1, axis=0)
    cube[4] = np.rot90(cube[4])
    return 'Dp'

def D2():
    cube[:4,2] = np.roll(cube[:4,2], 2, axis=0)
    cube[4] = np.rot90(cube[4],2)
    return 'D2'


def F():
    y();L();yp()
    return 'F'

def Fp():
    y();Lp();yp()
    return 'Fp'

def F2():
    y();L2();yp()
    return 'F2'


def B():
    y();R();yp()
    return 'B'

def Bp():
    y();Rp();yp()
    return 'Bp'

def B2():
    y();R2();yp()
    return 'B2'


def shuffle():
    """Mélange le cube."""
    pass