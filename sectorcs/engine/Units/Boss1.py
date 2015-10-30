# Ryan Schumacher
# Boss1.py
#
# A big enemy which fires a tri-shot gun rapidly

import pygame, os, sys, Constants, math
from pygame.locals import *
from random import randint
from Constants import *
from Unit import Unit
from Turret_dumb import *
from BombDrop import *

sys.path.append("../")
sys.path.append("Weapons/")
sys.path.append("../Obstacles")
from Upgrade import Upgrade

from MissileLauncher import MissileLauncher
from MissileDrop import *
from TurretGun import *
import Paths

class Boss1(Unit):
    def __init__(self, canvas, x, y, obsGroup):
        super(Boss1, self).__init__(150, 15, 500, 500, [TurretGun], 0,
                                    Paths.BOSS_1ST, Paths.LASER_BLUE,
                                    Paths.BOSS_1ST, x, y, 0, 0, canvas)

        velocity = 2
        self.dx = velocity
        self.dy = velocity

        self.startdx = self.dx
        self.startdy = self.dy
        
        self.obsGroup = obsGroup
        self.degreeParam = 0

        gun = TurretGun(canvas)
        self.gun_cool = 0
        
    def fireWeapon(self):
        self.curWeap.fire(self.x, self.y, 10, random.randint(0,45))
        #self.curWeap.fire(self.x, self.y, 10, random.randint(45,90))
        self.curWeap.fire(self.x, self.y, 10, random.randint(90,135))
        #self.curWeap.fire(self.x, self.y, 10, random.randint(135,180))
        self.curWeap.fire(self.x, self.y, -10, random.randint(0,45))
        #self.curWeap.fire(self.x, self.y, -10, random.randint(45,90))
        self.curWeap.fire(self.x, self.y, -10, random.randint(90,135))
        #self.curWeap.fire(self.x, self.y, -10, random.randint(135,180))
        
    def update(self, hero_copy):
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
                self.gun_cool = 25
            
                
        if self.degreeParam > 180:
           self.degreeParam = 0
           self.startdy = self.startdy * -1
           
        self.gun_cool -= 1
        super(Boss1, self).update(hero_copy)

        if((self.active == False) and (self.hpCur <= 0)):
            self.obsGroup.add(MissileDrop(self.x, self.y, self.screen))
            self.kill()
            
        
        
        
        
        
        
