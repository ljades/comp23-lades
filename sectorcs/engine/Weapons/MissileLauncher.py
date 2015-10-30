# Louis Ades
# BombDeployer.py
#
# The standard gun controlled by the hero unit

import pygame, os, sys

from pygame.locals import *
from Weapon import Weapon

sys.path.append("../")
import Constants, Paths
from Constants import *
from Paths import *

class MissileLauncher(Weapon):
    def __init__(self, canvas):
        Weapon.__init__(self, MISSILE_DMG, MISSILE_STAM, MISSILE_IMG, 
                        MISSILE_IMG_EXPL, MISSILE_FIRE, MISSILE_EXPL, MISSILE_SPEED, MISSILE_COOLDOWN, TYPE_M, canvas)
