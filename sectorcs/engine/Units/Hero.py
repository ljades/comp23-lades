# Ryan Schumacher
# Unit.py
#
# The main unit that is controlled by the player

import pygame, os, sys, Constants

from pygame.locals import *
from Constants import *
from Unit import Unit
from Paths import *

sys.path.append("../")
sys.path.append("Weapons/")

from MainGun import MainGun
import Paths

class Hero(Unit):
    def __init__(self, canvas):
        super(Hero, self).__init__(100, 100, 100, 100, [MainGun], 0,
                                   Paths.HERO_1, 
                                   Paths.HERO_1,
                                   Paths.HERO_1, 
                                   canvas.get_width() / 2, 
                                   canvas.get_height() / 2,
                                   HERO_MAX_SPEED,
                                   HERO_ACCEL,
                                   canvas)
        self.speedSetting = HERO_MAX_SPEED
        self.collide_cool = 0

        self.Death = pygame.mixer.Sound(HERO_DEATH)

        self.rect.x = (self.rect.x - self.image_w / 2)
        self.rect.y = (self.rect.y - self.image_h / 2)

        self.level = 1

    def incrementLevel (self):
        self.level += 1
        if (self.level == 2):
            new_image = self.load_image(HERO_2)
            self.image =   pygame.transform.rotate(new_image, -90.0)
            self.rot_image = self.image

        elif (self.level == 3):
            new_image = self.load_image(HERO_3)
            self.image = pygame.transform.rotate(new_image, -90.0)
            self.rot_image = self.image

        elif (self.level >= 4):
            new_image = self.load_image(HERO_4)
            self.image = pygame.transform.rotate(new_image, -90.0)
            self.rot_image = self.image
            
            
