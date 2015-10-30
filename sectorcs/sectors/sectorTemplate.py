# sectorTemplate.py
# Ryan Schumacher
#
# Template for making a new sector
# Do NOT add neighbors in this file, all neighbors will be added in sectNeighbors.py

from sectorHeader import *

def makeSectorNUMBER(hero, screen):
    sector = Sector (hero, "SECTOR NAME HERE", [0,0,0,0], 
                     SPAWN_X, SPAWN_Y, 
                     SEKT_PATH_HERE, MAIN_PATH_HERE)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
