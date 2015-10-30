# Will Hickey
# Turret_dumb.py
#
# The main unit that is controlled by the player

import pygame, os, sys, Constants, math

from pygame.locals import *
from Constants import *
from Unit import Unit

sys.path.append("../")
sys.path.append("Weapons/")

from TurretGun import *
import Paths, random

class Turret_dumb(Unit):
    def __init__(self, canvas, x, y):
        super(Turret_dumb, self).__init__(50, 50, 30, 30, [TurretGun], 0,
                                                    Paths.TURRET_ALIVE, 
                                                    Paths.LASER_BLUE,
                                                    Paths.TURRET_ALIVE, 
                                                    x, 
                                                    y,
                                                    0,
                                                    0,
                                                    canvas)
        self.speedSetting = 0

        # Give the starting weapon
        gun = TurretGun(canvas)
        
        self.gun_cool = 0
        
        
        self.weapons.append(gun)
        self.currWeap = self.weapons[0]

        self.rect.x = (self.rect.x - self.image_w / 2)
        self.rect.y = (self.rect.y - self.image_h / 2)
               
    def fireWeapon(self):
        # The turrets fire in a random pattern
        random.seed(random.randint(0,90))
        
        self.curWeap.fire(self.x, self.y, 7, random.randint(0,180))
        self.curWeap.fire(self.x, self.y, -7, random.randint(0,180))
        self.curWeap.fire(self.x, self.y, 7, random.randint(0,180))
        self.curWeap.fire(self.x, self.y, -7, random.randint(0,180))
        
        
    def update(self, hero_copy):
        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            if (self.gun_cool <= 0):
                self.fireWeapon()
                self.gun_cool = 30
        
            self.gun_cool -= 1
        super(Turret_dumb, self).update(hero_copy)
        
