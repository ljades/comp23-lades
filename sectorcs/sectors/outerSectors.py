# outerSectors.py
# Louis Ades
#
# A sector with enemies and obstacles

from sectorHeader import *

def makeSectorBound(hero, screen):
    sector = Sector (hero, "Boundaries", [0, 0, 0, 0], 1000, 800, SEKT_3, MAIN_1)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    # Add the obstacles here via:
    #
    sector.storm_side = 5
    
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
