# Will Hickey
# TurretGun.py
#


import pygame, os, sys

from pygame.locals import *
from Weapon import Weapon

sys.path.append("../")
import Constants, Paths
from Constants import *
from Paths import *

class TurretGun(Weapon):
    def __init__(self, canvas):
        Weapon.__init__(self, MAINGUN_DMG, MAINGUN_STAM, LASER_GREEN, 
                        LASER_BLUE, LASER_FIRE, LASER_EXPL, MAINGUN_SPEED, 0, TYPE_L, canvas)
