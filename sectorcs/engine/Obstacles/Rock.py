# Ryan Schumacher
# Rock.py
#
# A barrier on the screen. Cannot be passed through.

import pygame, os, sys

sys.path.append("../")

from pygame.locals import *
from random import randint
from Constants import *
from Obstacle import *
from Paths import *

class Rock(Obstacle):
    def __init__(self, init_x, init_y, canvas):
        super(Rock, self).__init__(ROCK_HP, ROCK_ARMOR, ROCK_TOUCH, ROCK_1,
                                   ROCK_1, ROCK_1, init_x, init_y, 
                                   False, canvas)

    
