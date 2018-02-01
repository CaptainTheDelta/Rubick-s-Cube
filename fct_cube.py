# coding: utf-8

# Pour l'ensemble des notations, se reporter aux images jointes.


#----------------------------------- Import -----------------------------------

import os
import numpy as np
from random import randint,choice
from copy import deepcopy

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
    cube[[0,4,2,5]] = cube[[4,2,5,0]]

    cube[0] = np.rot90(cube[0],2)
    cube[5] = np.rot90(cube[5],2)
    cube[1] = np.rot90(cube[1])
    cube[3] = np.rot90(cube[3],-1)
    return 'x'

def xp():
    x();x();x();
    return 'xp'


def y():
    #   4       4
    # 0123 -> 1230
    #   5       5
    cube[[0,1,2,3]] = cube[[1,2,3,0]]

    cube[5] = np.rot90(cube[5])
    cube[4] = np.rot90(cube[4],-1)
    return 'y'

def yp():
    y();y();y();
    return 'yp'


def z():
    #   4       1
    # 0123 -> 0524
    #   5       3
    yp();x();y()
    # cube[[1,4,3,5]] = cube[[5,1,4,3]]

    # cube[0] = np.rot90(cube[0])
    # cube[2] = np.rot90(cube[2],-1)
    return 'z'

def zp():
    yp();xp();y()
    #cube[[1,4,3,5]] = np.roll(cube[[1,4,3,5]], -1, axis=0)

    #cube[0] = np.rot90(cube[0],-1)
    #cube[2] = np.rot90(cube[2])
    return 'zp'


# Rotations des milieux

def E():
    cube[:4,1] = np.roll(cube[:4,1], 1, axis=0)
    cube[0,1] = cube[0,1][::-1]
    return 'E'

def Ep():
    E();E();E();
    return 'Ep'

def E2():
    E();E();
    return 'E2'


def M():
    zp();E();z()
    return 'M'

def Mp():
    zp();Ep();z()
    return 'Mp'

def M2():
    zp();E2();z()
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
def U():
    cube[:4,0] = np.roll(cube[:4,0], -1, axis=0)
    cube[4] = np.rot90(cube[4],-1)
    cube[5] = np.rot90(cube[5],1)
    return 'U'

def Up():
    U();U();U();
    return 'Up'

def U2():
    U();U();
    return 'U2'


def R():
    zp();U();z();
    return 'R'

def Rp():
    zp();Up();z();
    return 'Rp'

def R2():
    zp();U2();z();
    return 'R2'


def L():
    z();U();zp();
    return 'L'

def Lp():
    z();Up();zp();
    return 'Lp'

def L2():
    z();U2();zp();
    return 'L2'


def D():
    x();x();U();xp();xp();
    return 'D'

def Dp():
    x();x();Up();xp();xp();
    return 'Dp'

def D2():
    x();x();U2();xp();xp();
    return 'D2'


def F():
    x();U();xp();
    return 'F'

def Fp():
    x();Up();xp();
    return 'Fp'

def F2():
    x();U2();xp();
    return 'F2'


def B():
    xp();U();x();
    return 'B'

def Bp():
    xp();U();x();
    return 'Bp'

def B2():
    xp();U();x();
    return 'B2'


def shuffle():
    """Mélange le cube."""
    fcts = [x,xp, y,yp, z,zp,
        E,Ep,E2, M,Mp,M2, S,Sp,S2, U,Up,U2,
        R,Rp,R2, L,Lp,L2, D,Dp,D2, F,Fp,F2, B,Bp,B2]
    n = len(fcts)

    N = randint(50,100)

    print("Nombre d'actions pour mélanger le cube :",N)

    while N > 0:
        N -= 1
        choice(fcts)()


fct_inv = {
    x:xp, xp:x,
    y:yp, yp:y,
    z:zp, zp:z,
    E:Ep, Ep:E, E2:E2,
    M:Mp, Mp:M, M2:M2,
    S:Sp, Sp:S, S2:S2,
    U:Up, Up:U, U2:U2,
    R:Rp, Rp:R, R2:R2,
    L:Lp, Lp:L, L2:L2,
    D:Dp, Dp:D, D2:D2,
    F:Fp, Fp:F, F2:F2,
    B:Bp, Bp:B, B2:B2
}