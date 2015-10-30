# Ryan Schumacher
# CircleFlyer.py
#
# A basic enemy unit that flies in a circle

import pygame, os, sys, Constants, math

from pygame.locals import *
from Constants import *
from Unit import Unit

sys.path.append("../")
sys.path.append("Weapons/")

from TurretGun import *
from Paths import *
import random

class CircleFlyer(Unit):
    def __init__(self, canvas, x, y, velocity):
        super(CircleFlyer, self).__init__(100, 100, 30, 30, [TurretGun], 0,
                                          ORB_1, 
                                          ORB_1,
                                          ORB_1, 
                                          x, 
                                          y,
                                          velocity,
                                          0,
                                          canvas)
        self.speedSetting = 0

        self.dx = velocity
        self.dy = velocity

        self.startdx = self.dx
        self.startdy = self.dy

        self.degreeParam = 0

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
        
        self.curWeap.fire(self.x, self.y, 6, random.randint(0,360))
        self.curWeap.fire(self.x, self.y, -4, random.randint(0,360))        
        
    def update(self, hero_copy):
        self.degreeParam += 1

        self.x += self.dx
        self.rect.x += self.dx

        self.y += self.dy
        self.rect.y += self.dy

        self.dx = self.startdx * math.cos(self.degreeParam / 40)
        self.dy = self.startdy * math.sin(self.degreeParam / 40)

        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            if (self.gun_cool <= 0):
                self.fireWeapon()
                self.gun_cool = 40
        
            self.gun_cool -= 1

        if self.degreeParam > 360:
            self.degreeParam = 0

        super(CircleFlyer, self).update(hero_copy)
