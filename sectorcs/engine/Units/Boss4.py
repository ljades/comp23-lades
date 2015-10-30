#Louis Ades
#Boss4.py
#
#A Teleporting boss

import pygame, os, sys, Constants, math
from pygame.locals import *
from random import randint
from Constants import *
from Unit import Unit
from Turret_dumb import *
from BombDrop import *
from MissileLauncher import *

sys.path.append("../")
sys.path.append("Weapons/")

from TurretGun import *
import Paths

class Boss4(Unit):
    def __init__(self, canvas, x, y, obsGroup):
        super(Boss4, self).__init__(200, 200, 1000000, 1000000, [MissileLauncher], 
                                    BOMB_ONLY_ARMOR,
                                    Paths.FINALBOSS_IMG, Paths.LASER_BLUE,
                                    Paths.FINALBOSS_IMG, x, y, 0, 0, canvas)
        self.obsGroup = obsGroup
        
        
        # Give the starting weapon
        gun = MissileLauncher(canvas)
        
        self.gun_cool = 0
        
        
    def fireWeapon(self, hero_direction):
        # The turrets fire in a random pattern
        
        self.curWeap.fire(self.x, self.y, 10, hero_direction)

        
    def update(self, hero_copy):
        x_diff = hero_copy.x - self.x
        y_diff = hero_copy.y - self.y
        if (self.active == True and math.fabs(x_diff) < WIDTH and 
            math.fabs(y_diff) < HEIGHT):
            if (self.gun_cool <= 0):
                direction = 0
                if (y_diff == 0):
                    if (x_diff > 0):
                        direction = 0.0
                    else:
                        direction = 180.0
                elif (x_diff == 0):
                    if (y_diff < 90.0):
                        direction = 90.0
                    else:
                        direction = -90.0
                else:
                    direction = (180.0 / math.pi) * math.atan( -1 * y_diff 
                                                                / x_diff )
                    if ( x_diff < 0 ):
                        direction += 180.0

                self.fireWeapon(direction)
                self.gun_cool = 40
            
            
            self.gun_cool -= 1
            
            self.armorClass = 0
            for orb in self.obsGroup:
                if orb.active == True:
                    self.armorClass += 10

            super(Boss4, self).update(hero_copy)
        if((self.active == False) and (self.hpCur <= 0)):
            self.obsGroup.add(Upgrade(self.x, self.y, self.screen))
            self.kill()
            
        
        
        
        
        
        
