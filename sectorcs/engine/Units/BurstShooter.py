# Ryan Schumacher
# BurstShooter.py
#
# A basic enemy unit that moves slowly and fires huge barrages at the 
# hero unit. Moves in an arc

import pygame, os, sys, Constants, math

from pygame.locals import *
from Constants import *
from Unit import Unit

sys.path.append("../")
sys.path.append("Weapons/")

from TurretGun import *
from Paths import *
import random

class BurstShooter(Unit):
    def __init__(self, canvas, x, y, velocity):
        super(BurstShooter, self).__init__(80, 80, 30, 30, [TurretGun], 0,
                                          BURST_1, 
                                          BURST_1,
                                          BURST_1, 
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

        self.heroCopy = None
               
    def fireWeapon(self):
        # The turrets fire a burst
        random.seed(random.randint(0,180))

        angle = random.randint(0,360)

        if (random.randint (0, 3) >= 2):        
            self.curWeap.fire(self.x, self.y, 3, angle,)

        if (random.randint (0, 3) >= 2):
            self.curWeap.fire(self.x, self.y, 3, angle - 5)

        if (random.randint (0, 3) >= 2):
            self.curWeap.fire(self.x, self.y, 3, angle - 10)

        if (random.randint (0, 3) >= 2):
            self.curWeap.fire(self.x, self.y, 3, angle - 15)

        if (random.randint (0, 3) >= 2):
            self.curWeap.fire(self.x, self.y, 3, angle - 20)

        if (random.randint (0, 3) >= 2):
            self.curWeap.fire(self.x, self.y, 3, angle - 25)

        if (random.randint (0, 3) >= 2):
            self.curWeap.fire(self.x, self.y, 3, angle - 30)
        
    def update(self, hero_copy):
        self.heroCopy = hero_copy
        self.degreeParam += 1

        if (random.randint (0, 3) >= 2):
            self.x += self.dx
            self.rect.x += self.dx

            self.y += self.dy
            self.rect.y += self.dy

        self.dx = self.startdx * math.cos(self.degreeParam / 40)
        self.dy = self.startdy

        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            if (self.gun_cool <= 0):
                self.fireWeapon()
                self.gun_cool = 60
        
            self.gun_cool -= 1

        if self.degreeParam > 180:
            self.degreeParam = 0
            self.startdy = self.startdy * -1

        super(BurstShooter, self).update(hero_copy)
