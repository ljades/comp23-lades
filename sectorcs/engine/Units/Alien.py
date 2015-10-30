# Ryan Schumacher
# Alien.py
#
# A basic alien unit

import pygame, os, sys, Constants, math

from pygame.locals import *
from Constants import *
from Unit import Unit

sys.path.append("../")
sys.path.append("Weapons/")

from TurretGun import *
from Paths import *
import random

class Alien(Unit):
    def __init__(self, canvas, x, y, init_dx, init_dy):
        super(Alien, self).__init__(100, 100, 30, 30, [TurretGun], 0,
                                                    Paths.ALIEN_1, 
                                                    Paths.ALIEN_1,
                                                    Paths.ALIEN_1, 
                                                    x, 
                                                    y,
                                                    0,
                                                    0,
                                                    canvas)
        self.speedSetting = 0

        self.dx = init_dx
        self.dy = init_dy

        self.startdx = self.dx
        self.startdy = self.dy

        self.changeTicker = STRAFE_TIME

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
        
        self.curWeap.fire(self.x, self.y, 5, random.randint(0,180))
        self.curWeap.fire(self.x, self.y, -5, random.randint(0,180))        
        
    def update(self, hero_copy):
        self.changeTicker -= 1

        self.x += self.dx
        self.rect.x += self.dx

        self.y += self.dy
        self.rect.y += self.dy

        if (self.changeTicker <= 0):
            self.dx = self.startdx * -1
            self.dy = self.startdy * -1

            if (self.changeTicker <= -1 * STRAFE_TIME):
                self.changeTicker = STRAFE_TIME
        else:
            self.dx = self.startdx
            self.dy = self.startdy

        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            if (self.gun_cool <= 0):
                self.fireWeapon()
                self.gun_cool = 20
        
            self.gun_cool -= 1
        super(Alien, self).update(hero_copy)
