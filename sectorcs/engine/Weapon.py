# Ryan Schumacher
# Weapon.py
#
# Class for a weapon object. All weapons belong to units

import pygame, os, sys, Projectile
from Constants import *
from pygame.locals import *
from Projectile import Projectile
from Missile import Missile
from Bomb import Bomb

class Weapon:
    ''' An item that a unit (either the player or an AI unit) uses in combat '''
    def __init__(self, damage, stamUsage, projImage, projOnCollide, projFireSound,
                    projHitSound, projSpd, cooldown, weaponType, canvas):
        self.damageScore  = damage
        self.staminaUsage = stamUsage

        self.weapType = weaponType

        self.projectileImage = projImage         # Image of the projectile made
        self.projectileOnCollide = projOnCollide # Projectile collision image
        
        self.projectileFireSound = projFireSound
        self.projectileHitSound = projHitSound

        self.firedList = pygame.sprite.Group()
        self.projSpeed = projSpd

        self.cooldown = 0
        self.max_cooldown = cooldown

        self.screen = canvas

    def fire(self, x, y, velocity, rotation):
        if (self.cooldown > 0):
            return None

        if (self.weapType == TYPE_L):
            fired = Projectile (self.projectileImage,
                                self.projectileOnCollide,
                                self.projectileFireSound,
                                self.projectileHitSound, 
                                self.damageScore, velocity, x, y, rotation,
                                self.screen)
        elif (self.weapType == TYPE_M):
            fired = Missile    (self.projectileImage,
                                self.projectileOnCollide,
                                self.projectileFireSound,
                                self.projectileHitSound, 
                                self.damageScore, velocity, x, y, rotation,
                                FAST_ACCEL, M_DURABILITY,
                                self.screen)
        elif (self.weapType == TYPE_B):
            fired = Bomb (self.projectileImage,
                            self.projectileOnCollide,
                            self.projectileFireSound,
                            self.projectileHitSound, 
                            self.damageScore, x, y, BOMB_COUNTDOWN,
                            self.screen)
        self.firedList.add(fired)
        self.cooldown = self.max_cooldown
        return fired;
    
    def update(self, time_passed):
        if(self.cooldown <= 0):
            return None
        self.cooldown -= time_passed
                                        
        
