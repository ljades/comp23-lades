# sector2.py
# Will Hickey
#
# A sector with enemies and obstacles

from sectorHeader import *

def makeSector7(hero, screen):
    sector = Sector (hero, "Sector 7", [0, 0, 0, 0], 1000, 800, SEKT_3, MAIN_1)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    # Add the obstacles here via:
    #
    sector.storm_side = 4
    
    sector.addObs(maxHPupgrade (1000, 1000, screen))
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector