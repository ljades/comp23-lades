# sector0.py
# Ryan Schumacher
#
# A sector with enemies and obstacles

from sectorHeader import *
from random import randint

def makeSector0(hero, screen):
    sector = Sector (hero, "Sector 0", [0,0,0,0], 150, 150, SEKT_1, MAIN_1)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    #circle1 = CircleFlyer (screen, 1200, 1200, 3)
    #sector.addEnemy(circle1)

    #burst1 = BurstShooter (screen, 1000, 800, 1)
    #sector.addEnemy(burst1)

    sector.addObs(Rock (400, 400, screen))

    for i in range(0, 30):
        sector.addObs(Rock (randint(100, 2600), randint(400, 1600), screen))

    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
