# sector1.py
# Ryan Schumacher
#
# A sector with enemies and obstacles

from sectorHeader import *

def makeSector1 (hero, screen):
    sector = Sector (hero, "Sector 1", [0,0,0,0], 300, 300, SEKT_1, MAIN_1)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sector.addEnemy (ENEMY_HERE)

    for i in range(0, 20):
        sector.addObs(Rock (randint(800, 2000), randint(100, 1300), screen))

    turret_1 = Turret_dumb(screen, 100, 250)
    turret_2 = Turret_dumb(screen, 700, 200)

    alien_1 = Alien (screen, 600, 600, 2.0, 0)
    sector.addEnemy(Alien (screen, 2100, 1300, 0, 2.0))

    sector.addEnemy(turret_1)
    sector.addEnemy(turret_2)
    sector.addEnemy(alien_1)

    sector.addEnemy (Turret_dumb(screen, 500, 400))

    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sector.addObs (OBSTACLE_HERE)

    return sector
