#Will Hickey
#Boss3.py
#
#A Teleporting boss

import pygame, os, sys, Constants, math
from pygame.locals import *
from random import randint
from Constants import *
from Unit import Unit
from Turret_dumb import *
from BombDrop import *

sys.path.append("../")
sys.path.append("Weapons/")

from TurretGun import *
import Paths

class Boss3(Unit):
    def __init__(self, canvas, x, y, obsGroup):
        super(Boss3, self).__init__(70, 70, 500, 500, [TurretGun], MISSILE_ONLY_ARMOR,
                                    Paths.BOSS_3, Paths.LASER_BLUE,
                                    Paths.BOSS_3, x, y, 0, 0, canvas)
        self.obsGroup = obsGroup
        
        
        # Give the starting weapon
        gun = TurretGun(canvas)
        
        self.gun_cool = 0
        self.teleport_cool = 200
        
        
    def fireWeapon(self):
        # The turrets fire in a random pattern
        
        self.curWeap.fire(self.x, self.y, 10, random.randint(0,45))
        self.curWeap.fire(self.x, self.y, 10, random.randint(45,90))
        self.curWeap.fire(self.x, self.y, 10, random.randint(90,135))
        self.curWeap.fire(self.x, self.y, 10, random.randint(135,180))
        self.curWeap.fire(self.x, self.y, -10, random.randint(0,45))
        self.curWeap.fire(self.x, self.y, -10, random.randint(45,90))
        self.curWeap.fire(self.x, self.y, -10, random.randint(90,135))
        self.curWeap.fire(self.x, self.y, -10, random.randint(135,180))
        
    def update(self, hero_copy):
        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            if (self.gun_cool <= 0):
                self.fireWeapon()
                self.gun_cool = 25
            
            if (self.teleport_cool <= 0):
                self.x = randint(int((hero_copy.x - 600)),int((hero_copy.x + 600)))
                self.y = randint(int(hero_copy.y - 400),int(hero_copy.x + 400))
                
                if(self.x < 0):
                    self.x = 0
                elif(self.x > 2880):
                    self.x = 2850
                if(self.y < 0):
                    self.y = 0
                elif(self.y > 1800):
                    self.y = 1750
                
                self.dx = randint(-10, 10)
                self.dy = randint(-10, 10)
                self.teleport_cool = 500
            
            self.gun_cool -= 1
            self.teleport_cool -= 1
            super(Boss3, self).update(hero_copy)
        if((self.active == False) and (self.hpCur <= 0)):
            self.obsGroup.add(BombDrop(self.x, self.y, self.screen))
            self.kill()
            
        
        
        
        
        
        
