# Will Hickey
# BombWeapon.py
#
# Class for a weapon object. All weapons belong to units

import pygame, os, sys, Projectile
from pygame.locals import *
from Bomb import Bomb

sys.path.append("../")
import Constants, Paths
from Constants import *
from Paths import *

class BombWeapon:
    ''' An item that a unit (either the player or an AI unit) uses in combat '''
    def __init__(self, damage, stamUsage, projImage, projOnCollide, projFireSound,
                    projHitSound, projSpd, cooldown, canvas):
        self.damageScore  = damage
        self.staminaUsage = stamUsage

        self.projectileImage = projImage         # Image of the projectile made
        self.projectileOnCollide = projOnCollide # Projectile collision image
        
        self.projectileFireSound = projFireSound
        self.projectileHitSound = projHitSound

        self.firedList = pygame.sprite.Group()
        self.projSpeed = projSpd

        self.cooldown = 0
        self.max_cooldown = cooldown
        
        self.countdown = BOMB_COUNTDOWN

        self.screen = canvas

    def fire(self, x, y, velocity, rotation):
        if (self.cooldown > 0):
            return None

        fired = Bomb (self.projectileImage,
                            self.projectileOnCollide,
                            self.projectileFireSound,
                            self.projectileHitSound, 
                            self.damageScore, x, y, self.countdown,
                            self.screen)
        self.firedList.add(fired)
        self.cooldown = self.max_cooldown
        return fired;
    
    def update(self, time_passed):
        if(self.cooldown <= 0):
            return None
        self.cooldown -= time_passed
                                        
        
