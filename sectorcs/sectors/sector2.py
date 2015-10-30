# sector2.py
# Ryan Schumacher
#
# A sector with enemies and obstacles

from sectorHeader import *

def makeSector2(hero, screen):
    sector = Sector (hero, "Sector 2", [0, 0, 0, 0], 300, 1000, SEKT_2, BOSS_1)

    # Add the enemies here via:
    #
    boss_3 = Boss3(screen, 1000, 900, sector.tempObstGroup)
    sector.addEnemy(boss_3)
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    # Add the obstacles here via:
    #
    #sector.storm_side = 1
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
