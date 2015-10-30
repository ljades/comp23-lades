# Ryan Schumacher
# Obstacle.py
#
# Any inanimate, immobile object is classified as an object in Sektor CS

import pygame, os, sys, Constants, math

from pygame.locals import *
from random import randint
from Constants import *

class Obstacle(pygame.sprite.Sprite):
    ''' An inanimate object that may deal damage when touched by a unit'''

    def load_image(self, image_path):
        ''' Loads the sprite from the designated path'''
        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "Error loading image: " + image_path
            raise SystemExit, message
        return image.convert_alpha()

    def __init__(self, hpMax, armor, touchDamage, imagePath, onHit, onDeath, 
                 init_x, init_y, passable, canvas):
        ''' Creates an obstacle at coordinates x y with the given canvas'''
        pygame.sprite.Sprite.__init__(self)

        # For passable objects, ignore hpMax and hpCur
        self.hpMax = hpMax
        self.hpCur = hpMax
        self.armorClass  = armor #armorClass = an integer that dampens damage
        self.touchDamage = touchDamage # Damage dealt for touching this object

        self.x = init_x
        self.y = init_y

        self.image   = self.load_image(imagePath)
        self.image_w = self.image.get_width()
        self.image_h = self.image.get_height()
        self.onHitImage   = onHit   # Path to image of sprite getting hit
        self.onDeathImage = onDeath # Path to image of sprite dying 

        self.rect = self.image.get_rect()
        self.rect.x = self.x - (self.image_w / 2)
        self.rect.y = self.y - (self.image_h / 2)

        self.screen = canvas
        self.active = True

        self.dx = 0
        self.dy = 0

        self.hit_something = False
        self.passable = passable

    def update(self):
            self.x += self.dx
            self.y += self.dy
            #print("x: {} y: {}".format(self.dx, self.dy))
            self.rect.x += self.dx
            self.rect.y += self.dy

            if(self.hpCur <= 0):
               self.active = False


    def draw(self, relX, relY, hero_copy):
        if (self.active == True and math.fabs(self.x - hero_copy.x) < WIDTH and 
            math.fabs(self.y - hero_copy.y) < HEIGHT ):
            self.screen.blit(self.image, 
                             self.image.get_rect().move(self.x - self.image_w / 2 - relX, 
                                                        self.y - self.image_h / 2 - relY))

    def checkDeath (self):
        if self.hpCur <= 0:
            self.active = False;

    def check_collide(self, target):
        if ((target != None) and 
        (self.rect.colliderect(target.rect.inflate(-15, -15))) and 
        target.active == True and 
        self.active == True):

            if self.passable == False and target.collide_cool <= 0:

                self.hit_something = True
                target.hpCur -= self.touchDamage #Apply damage to the target.

                
                target.dy = target.dy * -1.6
                if(target.dy > target.max_speed):
                    target.dy = target.max_speed
                elif(target.dy < (-1 * target.max_speed)):
                    target.dy = (-1 * target.max_speed)
                target.dx = target.dx * -1.6
                if(target.dx > target.max_speed):
                    target.dx = target.max_speed
                elif(target.dx < (-1 * target.max_speed)):
                    target.dx = (-1 * target.max_speed)

            #TODO: Play a sound effect and push back
                target.collide_cool = 1
                return True
            else:
                self.passable_collide (target) # Abstract routine

        return False

    # Abstract routine only implemented in passable objects
    def passable_collide(self, target):
        pass

    def getHpMax(self):
        return self.hpMax

    def setHpMax(self, newhpMax):
        self.hpMax = newhpMax;

    def getHpCur(self):
        return self.hpCur

    def setHpCur(self, newHpCur):
        self.hpCur = newHpCur

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
