# sector6.py
# Louis Ades
#
# A sector with the final boss

from sectorHeader import *
import math

def makeSector6(hero, screen):
    sector = Sector (hero, "Sector 6", [0, 0, 0, 0], 2600, 200, SEKT_3, BOSS_1)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    final_boss = Boss4(screen, 1200, 1200, sector.tempObstGroup)
    sector.addEnemy(final_boss)

    for i in range(0, 14):
        j = ((i * 1.0) / 7.0) * math.pi
        bossOrb = Obstacle (BOSS_ORB_HP, BOMB_ONLY_ARMOR, 0, FINALBOSS_ORB_IMG,
                            LASER_BLUE, LASER_BLUE, 1200 + 300 * math.cos(j), 
                            1200 + 300 * math.sin(j), True, screen)
        sector.addObs(bossOrb)

    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

    return sector
