# sector2.py
# Will Hickey
#
# A sector with enemies and obstacles

from sectorHeader import *

def makeSector4(hero, screen):
    sector = Sector (hero, "Sector 4", [0, 0, 0, 0], 0, 0, SEKT_2, MAIN_2)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    boss2 = Boss2(screen, 1100, 600, sector.tempObstGroup)
    sector.addEnemy(boss2)

    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
