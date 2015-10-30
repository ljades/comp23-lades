# Louis Ades
# Bomb.py
# An object that gets deployed and explodes after a certain period of time. 
# All projectiles are fired from the Unit class.

import pygame, os, sys, math
from pygame.locals import *
from random import randint
import Paths, Constants 
from Paths import *
from Constants import *

class Bomb(pygame.sprite.Sprite):
    ''' A flying sprite '''

    def load_image(self, image_path):
        ''' Loads the sprite from the designated path'''
        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "Error loading image: " + image_path
            raise SystemExit, message
        return image.convert_alpha()

    def __init__(self, image, onExplode, FireSound, HitSound, damage, 
                 init_x, init_y, countdown, canvas):
        ''' Creates an obstacle at coordinates x y with the given canvas'''
        pygame.sprite.Sprite.__init__(self)

        self.image   = self.load_image(image)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()
        
        self.img_expl = self.load_image(onExplode)
        self.expl_w = self.img_expl.get_width()
        self.expl_h = self.img_expl.get_height()

        self.rect   = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = init_y
        self.countdown = countdown

        
        self.onFireSound    = FireSound   # Path to Fire Sound
        self.PlayFire = pygame.mixer.Sound(FireSound) #Fire Sound to be played
        self.PlayFire.play()
        self.onHitSound     = HitSound    # Path to Hit Sound
        self.PlayHit = pygame.mixer.Sound(HitSound) #Hit Sound to be played
        
        self.hit_something = False
        self.damageScore = damage
        
        #display the collideImage for x ticks
        self.Collide_Tick = PROJ_DEATH_TIME
        
        self.x = init_x
        self.y = init_y
        self.screen = canvas
        self.active = True

    def update(self, target, relx, rely, hero_copy, bait_group):
        '''Updates the sprite's position and active status'''
        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            if(self.hit_something == False):

                # TODO: Test for moving off screen
                if ((self.x <= 0) or (self.y <= 0) or (self.x > relx) or (self.y > rely)):
                    self.active = False
            
            
                self.countdown -= 1.0/FRAMES_SEC
                if (self.countdown <= 0):
                    self.image   = self.img_expl
                    self.image_w = self.expl_w
                    self.image_h = self.expl_h

                    self.rect   = self.image.get_rect()
                    self.rect.x = relx
                    self.rect.y = rely
                    self.Collide_Tick -=1

                #Check to see if it hit target
                if(target != None):
                    self.check_collide(target)


            #decrement the collision image counter before disappearing
            elif (self.hit_something == True):
                self.Collide_Tick -= 1
                
            if (self.Collide_Tick <= 0):
                self.PlayHit.play()
                self.active = False
                
        #take out of the sprite projectile group        
        if (self.active == False):
            self.kill()
                
    def draw(self, relX, relY, hero_copy):
        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT):
            self.screen.blit(self.image, 
                         self.image.get_rect().move(self.x - (self.image_w / 2)
                                                    - relX, self.y - (self.image_h / 2) - relY))

                         
    def check_collide(self, target):
        if ((target != None) and (self.rect.colliderect(target.rect.inflate(-15, -15))) and target.active == True):
            self.hit_something = True
            if (target.armorClass < self.damageScore):
                target.hpCur -= (self.damageScore - target.armorClass) #Apply damage to the target.target.hpCur -= self.damageScore #Apply damage to the target.
                self.PlayHit.play()
                self.image = self.img_expl

            if target.hpCur <= 0:
                target.active = False

            #self.image = pygame.transform.rotate(self.load_image(self.onCollideImage), self.rotation - 90.0)

            return True
        return False
                         
    def getDamageScore(self):
        return self.damageScore

    def setDamageScore(self, newDamageScore):
        self.damageScore = newDamageScore

    def getX(self):
        return self.x

    def setX(self, newX):
        self.x = newX

    def getY(self):
        return self.y

    def setY(self, newY):
        self.y = newY

    def getDX(self):
        return self.dx

    def setDX(self, newDX):
        self.dx = newDX

    def getDY(self):
        return self.dy

    def setDY(self, newDY):
        self.dy = newDY

    def setImage(self, newImgPath):
        self.image = self.load_image(newImgPath)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()

    def getRect(self):
        return self.rect

    def getScreen(self):
        return self.screen

    def setScreen(self, newScreen):
        self.screen = newScreen

    def getActive(self):
        return self.active

    def setActive(self, newActive):
        self.active = newActive
