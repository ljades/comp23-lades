# Asteroid.py
#
# This an obstacle called asteroid. It interacts with other units and does damage
# when collided with. It also breaks apart if it hits something with a bigger mass

import pygame, os, sys, Constants, Paths
from pygame.locals import *
from random import randint
from Constants import *
from Paths import *
from Obstacle import Obstacle

class Asteroid(Obstacle):
    '''This is an asteroid that will break apart given mass and collision'''
    
    def load_image(self, image_path):
        ''' Loads the sprite from the designated path'''
        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "Error loading image: " + image_path
            raise SystemExit, message
        return image.convert_alpha()
        
    def __init__(self, x, y, dx, dy, mass, canvas):
        
        if(mass == 3):
            image_path = Paths.ASTRO_BIG_1
        elif(mass == 2):
            image_path = Paths.ASTRO_MED_1
        elif(mass == 1):
            image_path = Paths.ASTRO_SMALL_1
        
        super(Asteroid, self).__init__(10000, 10000, (5 * mass), image_path, image_path, image_path,
                x, y, False, canvas)
        self.mass = mass
        self.dx = dx
        self.dy = dy
        
        self.PlayHit = pygame.mixer.Sound(ASTRO_HIT)
        
        self.hit_something = False
        self.break_apart = False
        
        self.safe_time = 200
        
        
        
    def update(self, target, ObstGroup):
        '''This updates the position and collision'''
        
        if(self.active == False):
            self.kill()
            self.rect.x = -5000
        else:
            super(Asteroid, self).update()
            self.safe_time -= 1

        if ((self.x < 0) or (self.y < 0) or 
            (self.x > 2880) or 
            (self.y > 1800)):
            self.active = False
            self.kill()
        
        if( self.break_apart == True):
            if(self.mass != 1):
                new_ast1 = Asteroid(self.x, self.y,
                                     (-1 * self.dx),
                                     (-1 * self.dy), 
                                     (self.mass - 1), 
                                     self.screen)
                new_ast2 = Asteroid(self.x, self.y,
                                     self.dx,
                                     (-1 * self.dy), 
                                     (self.mass - 1), 
                                     self.screen)
                new_ast3 = Asteroid(self.x, self.y,
                                     (-1 * self.dx),
                                      self.dy, 
                                     (self.mass - 1), 
                                     self.screen)
                                     
                ObstGroup.add(new_ast1)
                ObstGroup.add(new_ast2)
                ObstGroup.add(new_ast3)
            self.active = False
            self.kill()
            
        elif(self.safe_time <= 0):
            #super(Asteroid, self).update()
        
            if((self.hit_something == True) and (hasattr(target,"mass"))):
                if(self.mass > target.mass):
                    target.break_apart = True
                elif(self.mass < target.mass):
                    self.break_apart = True
                elif(self.mass == target.mass):
                    self.break_apart = True
                    target.break_apart = True
                self.hit_something = False
            
                
                
                
                
    def check_coll(self, target):
        if ((target != None) and 
            (self.rect.colliderect(target.rect.inflate(-15, -15))) and 
            (target.active == True)):
            
            self.hit_something = True
            target.hpCur -= self.touchDamage #Apply damage to the target.
            #self.image = pygame.transform.rotate(self.load_image(self.onCollideImage), self.rotation - 90.0)
            self.PlayHit.play()
                    
            







