# sector2.py
# Will Hickey
#
# A sector with enemies and obstacles

from sectorHeader import *

def makeSector3(hero, screen):
    sector = Sector (hero, "Sector 3", [0, 0, 0, 0], 0, 0, SEKT_2, MAIN_1)

    # Add the enemies here via:
    #
    # *Create a new enemy*
    # sectorNUMBER.addEnemy (ENEMY_HERE)

    # Add the obstacles here via:
    #
    # *Create a new obstacle*
    # sectorNUMBER.addObs (OBSTACLE_HERE)

#asteroids are about 50 square pixels
#one "unit" is about 225 square pixels, a little less than 5 asteroids
#makes a long asteroid wall, vertically
    def makeLongVert(startx, starty):
        for i in range(0, 15):
            sector.addObs(Rock (startx, starty, screen))
            starty += 50

#makes a long asteroid wall, horizontally
    def makeLongHoriz(startx, starty):
        for i in range(0, 15):
            sector.addObs(Rock (startx, starty, screen))
            startx += 50


    def makeShortVert(startx, starty):
        for i in range(0, 5):
            sector.addObs(Rock (startx, starty, screen))
            starty += 50


    def makeShortHoriz(startx, starty):
        for i in range(0, 5):
            sector.addObs(Rock (startx, starty, screen))
            startx += 50
    #first wall/
    makeLongVert(300, 0)
    makeLongVert(300, 900)
    sector.addObs(Rock (300, 1650, screen))
    #sector.addObs(Rock (300, 1700, screen))
    #sector.addObs(Rock (300, 1750, screen))
   #/first wall

    #bottom wall/
    makeLongHoriz(350, 1650)
    makeLongHoriz(1100, 1650)
    makeLongHoriz(1850, 1650)
    #/bottom wall

    #last wall/
    makeLongVert(2600, 0)
    makeLongVert(2600, 900)
    sector.addObs(Rock (2600, 1650, screen))
    sector.addObs(Rock (2600, 1700, screen))
    sector.addObs(Rock (2600, 1750, screen))
    #/last wall

    #"upgrade walkway" (final few steps)
    makeShortHoriz(2600, 750)
    makeShortHoriz(2600, 900)
    sector.addObs(Rock(2800, 800, screen))
    sector.addObs(Rock(2800, 850, screen))

    #upgrade
    sector.addObs(maxHPupgrade (2750, 850, screen))

    #top wall/
    makeLongHoriz(350, 100)
    makeLongHoriz(1100, 100)
    makeLongHoriz(1850, 100)
    #/top wall


    #2nd walls
    makeShortVert(700, 0)
    makeShortVert(700, 250)
    makeShortHoriz(550, 500)

    makeShortHoriz(550, 700)
    makeShortHoriz(800, 700)
    makeShortVert(550, 750)

    makeShortHoriz(300, 1300)

    makeShortVert(600, 1550)
    #/2nd walls


    #3rd walls
    makeLongVert(1000, 450)
    makeShortVert(1000, 1200)

    makeShortHoriz(1000, 1300)
    makeShortVert(1250, 1350)
    makeShortHoriz(1250, 1600)
    makeShortVert(1500, 1600) #overlap
    #/3rd walls

    #4th walls
    makeLongVert(1300, 200)
    makeShortHoriz(1350, 200)
    makeShortHoriz(1600, 200)
    makeShortVert(1800, 200)
    makeShortHoriz(1550, 450)

    makeShortHoriz(1300, 700)
    makeShortHoriz(1550, 700)

    makeShortHoriz(1300, 950)
    makeShortHoriz(1550, 950)
    #/4th walls


    #5th walls
    makeShortVert(1800, 1000)
    makeShortHoriz(1800, 1250)
    makeShortHoriz(2050, 1250)

    makeShortVert(2200, 750)
    makeLongHoriz(1900, 750)

    makeShortHoriz(1950, 1000)
    #/5th walls

    return sector
