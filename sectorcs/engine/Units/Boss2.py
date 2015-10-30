#Louis Ades
#Boss4.py
#
#A Zig-Zag Missiles boss

import pygame, os, sys, Constants, math
from pygame.locals import *
from random import randint
from Constants import *
from Unit import Unit
from Turret_dumb import *
from BombDrop import *
from MissileLauncher import *
from Speedupgrade import Speedupgrade
from Upgrade import Upgrade

sys.path.append("../")
sys.path.append("Weapons/")

from TurretGun import *
import Paths

class Boss2(Unit):
    def __init__(self, canvas, x, y, obsGroup):
        super(Boss2, self).__init__(200, 200, 100000, 100000, [MissileLauncher], 
                                    0,
                                    Paths.FINALBOSS_IMG, Paths.LASER_BLUE,
                                    Paths.FINALBOSS_IMG, x, y, 0, 0, canvas)
        self.obsGroup = obsGroup
        
        self.moveCounter = 0
        # Give the starting weapon
        gun = MissileLauncher(canvas)
        
        self.gun_cool = 0
        
        
    def fireWeapon(self):
        # The turrets fire in a random pattern
        
        self.curWeap.fire(self.x, self.y, 10, random.randint(0,360))
        self.curWeap.fire(self.x, self.y, 10, random.randint(0,360))
        self.curWeap.fire(self.x, self.y, 10, random.randint(0,360))
        self.curWeap.fire(self.x, self.y, 10, random.randint(0,360))

        
    def update(self, hero_copy):
        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            if (self.gun_cool <= 0):
                self.fireWeapon()
                self.gun_cool = 80
            
            
            self.gun_cool -= 1
            
            self.dx = 4 * math.sin(2.0 * self.moveCounter / FRAMES_SEC)
            self.dy = 4 * math.cos(6.0 * self.moveCounter / FRAMES_SEC)
            
            self.moveCounter += 1
            super(Boss2, self).update(hero_copy)
        if((self.active == False) and (self.hpCur <= 0)):
            self.obsGroup.add(Speedupgrade(self.x, self.y, self.screen))
            self.obsGroup.add(Upgrade(self.x, self.y, self.screen))
            self.kill()
            
        
        
        
        
        
        
