"""
Author: CaptainTheDelta
Creation: 23-05-17
"""
# ---------------------------------- Import -----------------------------------

import sys
import ctypes

# -------------------------------- Constantes ---------------------------------

STD_OUTPUT_HANDLE = ctypes.windll.kernel32.GetStdHandle(-11)

black   = 0x0
blue    = 0x1
green   = 0x2
aqua    = 0x3
red     = 0x4
purple  = 0x5
yellow  = 0x6
white   = 0x7

gray        = 0x8
lightBlue   = 0x9
lightGreen  = 0xa
lightAqua   = 0xb
lightRed    = 0xc
lightPurple = 0xd
lightYellow = 0xe
brightWhite = 0xf


# --------------------------------- Fonctions ---------------------------------

def setColor(fg,bg=0):
    """Fixe une couleur à la console.

    Args:
        fg (int): Valeur de la couleur du texte.
        bg (int)[0]: Valeur de la couleur de l'arrière plan.
    """
    color = fg | (bg << 4)

    ctypes.windll.kernel32.SetConsoleTextAttribute(STD_OUTPUT_HANDLE,color)


def resetColor():
    setColor(white,black)


def printClr(color,*args,**kwargs):
    """Affiche le string coloré via le couple color.

    Args:
        color (tuple): Couple fg,bg.
        string (str): Contenu à afficher.
    """
    setColor(*color)
    
    print(*args,**kwargs)
    
    resetColor()


# def clr(color,*args):
#     return " ".join(args)


def debug(*args):
    """"Affiche un debug à l'utilisateur.

    Args:
        *args (??): Valeur à afficher.
    """
    print("[DEBUG]",*args)
