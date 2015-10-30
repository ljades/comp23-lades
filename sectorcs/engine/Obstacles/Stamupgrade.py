# Louis Ades
# Stamupgrade.py
#
# A barrier on the screen. Cannot be passed through.

import pygame, os, sys

sys.path.append("../")
sys.path.append("../Units")

from pygame.locals import *
from random import randint
from Constants import *
from Obstacle import *
from Paths import *
from Hero import Hero

class Stamupgrade(Obstacle):
    def __init__(self, init_x, init_y, canvas):
        super(Stamupgrade, self).__init__(UPGRADE_HP, UPGRADE_ARMOR, 
                                      UPGRADE_TOUCH, UPGRADE_1,
                                      UPGRADE_1, UPGRADE_1, init_x, init_y, 
                                      True, canvas)
        self.playUpgrade = pygame.mixer.Sound(GET_UPGRADE)
    def passable_collide(self, target):
        if isinstance (target, Hero):
            self.playUpgrade.play()
            if (hasattr(target, "level")):
                target.staminaMax += 50
                self.kill()

                
