# Sector.py
#
# A sector is what is displayed on the screen at any given time. A sector
# contains enemies, obstacles, and paths to other sectors. They are the
# building blocks of the world.

import copy, pygame, os, sys, Constants
from Constants import *
from pygame.locals import *
from random import randint
from Asteroid import Asteroid

sys.path.append("Units/")
from Turret_dumb import *

class Sector():

    def load_image(self, image_path):
        ''' Loads the sprite from the designated path'''
        try:
            image = pygame.image.load(image_path)
        except pygame.error, message:
            print "Error loading image: " + image_path
            raise SystemExit, message
        return image.convert_alpha()

    def __init__(self, mainChar, name, neighbors, spawnX, spawnY, 
                 backgroundPath, musicPath):
        ''' Initializes a sector with all of the information it holds '''
        # A sector's name MUST be unique for populating it
        self.name = name
        self.hero = mainChar
        self.neighbors = neighbors

        # A sector maintains a list of all units, obstacles, and projectiles
        self.unitGroup = pygame.sprite.Group()
        self.obstGroup = pygame.sprite.Group()
        self.projGroup = pygame.sprite.Group()

        self.tempUnitGroup = pygame.sprite.Group()
        self.tempObstGroup = pygame.sprite.Group()
        self.tempProjGroup = pygame.sprite.Group()

        self.respawnX  = spawnX
        self.respawnY  = spawnY
        
        self.storm_side = 0;

        # Grab the background image
        self.background = self.load_image(backgroundPath)
        self.width, self.height = self.background.get_size() 

        # Background music
        self.music = musicPath

    def load_music(self, sound_name):
         try:
             pygame.mixer.music.load(sound_name)
         except pygame.error, message:
             print "Cannot load sound: " + sound_name
             raise SystemExit, message

    def loadTheme(self):
         ''' Returns the loaded music file '''
         theme = self.load_music(self.music)
         return theme

    def transition(self, toSector):
        ''' Moves the hero unit, returns the sector to load '''
        if toSector.music != self.music:
            toSector.loadTheme()
            pygame.mixer.music.play()

    def checkTransition(self):
        ''' Checks if the hero unit is moving into another sector '''
        ''' If a transition is needed, calls transition() '''

        # TODO: Maintain the rotation after the ship has transitioned sectors
        x = self.hero.rect.x
        y = self.hero.rect.y

        if y <= NORTHERN_BOUNDARY and self.hero.dy <= -1 and self.neighbors[NORTH] != 0:     
            # In a north transition, the X coordinate is preserved
            self.hero.y = self.height - self.hero.image_h
            self.hero.rect.y = self.height - 3 * self.hero.image_h / 2

            for unit in self.neighbors[NORTH].tempUnitGroup:
                unit.active = True;
                unit.hpCur = unit.hpMax

            for obs in self.neighbors[NORTH].tempObstGroup:
                obs.active = True;
                obs.hpCur = obs.hpMax

            self.transition(self.neighbors[NORTH])
            return self.neighbors[NORTH]

        elif y + self.hero.image_h >= self.height - SOUTHERN_BOUNDARY and self.hero.dy >= 1 and self.neighbors[SOUTH] != 0:
            # In a south transition, the X coordinate is preserved
            self.hero.y = self.hero.image_h / 2 
            self.hero.rect.y = self.hero.image_h / 2

            for unit in self.neighbors[SOUTH].tempUnitGroup:
                unit.active = True;
                unit.hpCur = unit.hpMax

            for obs in self.neighbors[SOUTH].tempObstGroup:
                obs.active = True;
                obs.hpCur = obs.hpMax

            self.transition(self.neighbors[SOUTH])
            return self.neighbors[SOUTH]


        elif x <= WESTERN_BOUNDARY and self.hero.dx <= -1 and self.neighbors[WEST] != 0:
            # In a west transtiion, the Y coordinate is preserved
            self.hero.x = self.width - self.hero.image_w / 2
            self.hero.rect.x = self.width - 3 * self.hero.image_w / 2

            for unit in self.neighbors[WEST].tempUnitGroup:
                unit.active = True;
                unit.hpCur = unit.hpMax

            for obs in self.neighbors[WEST].tempObstGroup:
                obs.active = True;
                obs.hpCur = obs.hpMax

            self.transition(self.neighbors[WEST])
            return self.neighbors[WEST]

        elif x + self.hero.image_w >= self.width - EASTERN_BOUNDARY and self.hero.dx >= 1 and self.neighbors[EAST] != 0:
            # In an eastern transition, the Y coordinate is preserved
            self.hero.x = self.hero.image_w / 2
            self.hero.rect.x = self.hero.image_w / 2

            for unit in self.neighbors[EAST].tempUnitGroup:
                unit.active = True;
                unit.hpCur = unit.hpMax

            for obs in self.neighbors[EAST].tempObstGroup:
                obs.active = True;
                obs.hpCur = obs.hpMax

            self.transition(self.neighbors[EAST])
            return self.neighbors[EAST]

        return self

    def addNeighbor(self, sectNeighbor, direction):
        self.neighbors[direction] = sectNeighbor   

    def addEnemy (self, newEnemy):
        self.unitGroup.add(newEnemy)
        self.tempUnitGroup.add(newEnemy)

    def addObs (self, newObs):
        self.obstGroup.add(newObs)
        self.tempObstGroup.add(newObs)

    def addProj (self, newProj):
        self.projGroup.add(newProj)
        self.tempProjGroup.add(newProj)
        
    def asteroid_storm(self, relX, relY, screen):
        decider = 0
        if (self.storm_side == 1):#coming from top
            x = randint(10, self.width - 10)
            y = 0
            dx = randint(-3, 3)
            dy = randint(1, 8)
        elif(self.storm_side == 2):#coming from right
            x = self.width
            y = randint(10, self.height -10)
            dx = randint(-8, -1)
            dy = randint(-3, 3)
        elif(self.storm_side == 3): #coming from bottom
            x = randint(10, self.width - 10)
            y = self.height - 200
            dx = randint(-3, 3)
            dy = randint(-8, -1)
        elif(self.storm_side == 4):#coming from left
            x = 0
            y = randint(10, self.height -10)
            dx = randint(1, 8)
            dy = randint(-3, 3)

        elif(self.storm_side == 5): #boundary storm--massive!
            decider = randint(0, 50)
            if (decider == 0): #From the left
                x = relX
                y = relY + randint(0, HEIGHT)
                dx = randint(1, 8)
                dy = randint(-3, 3)
            if (decider == 1): #From the top
                x = relX + randint(0, WIDTH)
                y = relY
                dx = randint(-3, 3)
                dy = randint(1, 8)
            if (decider == 2): #From the right
                x = relX + WIDTH
                y = relY + randint(0, HEIGHT)
                dx = randint(-8, -1)
                dy = randint(-3, 3)
            if (decider == 3): #From the bottom
                x = relX + randint(0, WIDTH)
                y = relY + HEIGHT
                dx = randint(-3, 3)
                dy = randint(-8, -1)
            
        if (decider <= 3):
            new_astr = Asteroid(x, y, dx, dy, randint(1,3), screen)
            self.tempObstGroup.add(new_astr)
        
        
        
        
        
        
        
        
        
        
        
