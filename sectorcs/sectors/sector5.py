# sector2.py
# Will Hickey
#
# A sector with enemies and obstacles

from sectorHeader import *
from Stamupgrade import Stamupgrade

def makeSector5(hero, screen):
    sector = Sector (hero, "Sector 5", [0, 0, 0, 0], 0, 0, SEKT_1, MAIN_1)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    for i in range(0, 12):
        j = ((i * 1.0) / 6.0) * math.pi
        dumber = Turret_dumb(screen, 1200 + 300 * math.cos(j), 900 + 300 * math.sin(j))
        sector.addEnemy(dumber)
    for i in range(0, 30):
        j = ((i * 1.0) / 15.0) * math.pi
        sector.addObs(Rock (1200 + 400 * math.cos(j), 900 + 400 * math.sin(j), screen))



    sector.addObs(Stamupgrade (1200, 900, screen))
    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
