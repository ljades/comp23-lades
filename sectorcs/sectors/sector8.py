# sector2.py
# Will Hickey
#
# A sector with enemies and obstacles

from sectorHeader import *

def makeSector8(hero, screen):
    sector = Sector (hero, "Sector 8", [0, 0, 0, 0], 0, 0, SEKT_3, MAIN_2)

    for i in range(0, 25):
        sector.addObs(Rock (randint(800, 2000), randint(800, 1500), screen))

    for i in range (0, 15):
        sector.addObs (Rock (randint(2000, 2500), randint(100, 1500), screen))

    sector.addEnemy (Boss1 (screen, 300, 300, sector.tempObstGroup)) 

    sector.addEnemy (Turret_dumb(screen, 950, 450))
    sector.addEnemy (Turret_dumb(screen, 1050, 600))


    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
