# Will Hickey
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

class BombDeployer(Weapon):
    def __init__(self, canvas):
        Weapon.__init__(self, BOMB_DMG, BOMB_STAM, BOMB_IMG, 
                        BOMB_IMG_EXPL, BOMB_FIRE, BOMB_EXPL, BOMB_SPEED, BOMB_COOLDOWN, TYPE_B, canvas)
