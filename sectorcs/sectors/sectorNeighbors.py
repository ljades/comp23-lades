# sectorNeighbors.py
# Ryan Schumacher
#
# Make the neighbors for each group of sectors
#
# Dev note:
#     To make the connections between sectors, you need to know which sector has
#     which number. Check game.py for this if need be.

import sectorHeader

import sys
sys.path.append("../engine/")
from Constants import *

def makeNeighbors (sectors):
    ''' sectors is a list of sectors '''
    sectors[0].addNeighbor(sectors[1], NORTH) 
    sectors[0].addNeighbor(sectors[3], EAST)
    sectors[0].addNeighbor(sectors[5], SOUTH)
    sectors[0].addNeighbor(sectors[7], WEST)
    
    sectors[1].addNeighbor(sectors[0], SOUTH) 
    sectors[1].addNeighbor(sectors[10], NORTH) 
    sectors[1].addNeighbor(sectors[2], EAST)
    sectors[1].addNeighbor(sectors[8], WEST)
    
    sectors[2].addNeighbor(sectors[3], SOUTH) 
    sectors[2].addNeighbor(sectors[11], NORTH) 
    sectors[2].addNeighbor(sectors[13], EAST)
    sectors[2].addNeighbor(sectors[1], WEST)
    
    sectors[3].addNeighbor(sectors[4], SOUTH) 
    sectors[3].addNeighbor(sectors[2], NORTH) 
    sectors[3].addNeighbor(sectors[14], EAST)
    sectors[3].addNeighbor(sectors[0], WEST)
    
    sectors[4].addNeighbor(sectors[17], SOUTH) 
    sectors[4].addNeighbor(sectors[3], NORTH) 
    sectors[4].addNeighbor(sectors[15], EAST)
    sectors[4].addNeighbor(sectors[5], WEST)
    
    sectors[5].addNeighbor(sectors[18], SOUTH) 
    sectors[5].addNeighbor(sectors[0], NORTH) 
    sectors[5].addNeighbor(sectors[4], EAST)
    sectors[5].addNeighbor(sectors[6], WEST)
    
    sectors[6].addNeighbor(sectors[19], SOUTH) 
    sectors[6].addNeighbor(sectors[7], NORTH) 
    sectors[6].addNeighbor(sectors[5], EAST)
    sectors[6].addNeighbor(sectors[21], WEST)
    
    sectors[7].addNeighbor(sectors[6], SOUTH) 
    sectors[7].addNeighbor(sectors[8], NORTH) 
    sectors[7].addNeighbor(sectors[0], EAST)
    sectors[7].addNeighbor(sectors[22], WEST)
    
    sectors[8].addNeighbor(sectors[7], SOUTH) 
    sectors[8].addNeighbor(sectors[9], NORTH) 
    sectors[8].addNeighbor(sectors[1], EAST)
    sectors[8].addNeighbor(sectors[23], WEST)

    #sectors[9].addNeighbor(sectors[1], NORTH) 
    sectors[9].addNeighbor(sectors[10], EAST)
    sectors[9].addNeighbor(sectors[8], SOUTH)
    sectors[9].addNeighbor(sectors[24], WEST)
    
    sectors[10].addNeighbor(sectors[1], SOUTH) 
    #sectors[10].addNeighbor(sectors[10], NORTH) 
    sectors[10].addNeighbor(sectors[11], EAST)
    sectors[10].addNeighbor(sectors[9], WEST)
    
    sectors[11].addNeighbor(sectors[2], SOUTH) 
    #sectors[11].addNeighbor(sectors[11], NORTH) 
    sectors[11].addNeighbor(sectors[12], EAST)
    sectors[11].addNeighbor(sectors[10], WEST)
    
    sectors[12].addNeighbor(sectors[13], SOUTH) 
    #sectors[12].addNeighbor(sectors[2], NORTH) 
    #sectors[12].addNeighbor(sectors[14], EAST)
    sectors[12].addNeighbor(sectors[11], WEST)
    
    sectors[13].addNeighbor(sectors[14], SOUTH) 
    sectors[13].addNeighbor(sectors[12], NORTH) 
    #sectors[13].addNeighbor(sectors[15], EAST)
    sectors[13].addNeighbor(sectors[2], WEST)
    
    sectors[14].addNeighbor(sectors[15], SOUTH) 
    sectors[14].addNeighbor(sectors[13], NORTH) 
    #sectors[14].addNeighbor(sectors[4], EAST)
    sectors[14].addNeighbor(sectors[3], WEST)
    
    sectors[15].addNeighbor(sectors[16], SOUTH) 
    sectors[15].addNeighbor(sectors[14], NORTH) 
    #sectors[15].addNeighbor(sectors[5], EAST)
    sectors[15].addNeighbor(sectors[4], WEST)
    
    #sectors[16].addNeighbor(sectors[6], SOUTH) 
    sectors[16].addNeighbor(sectors[15], NORTH) 
    #sectors[16].addNeighbor(sectors[0], EAST)
    sectors[16].addNeighbor(sectors[17], WEST)
    
    #sectors[17].addNeighbor(sectors[7], SOUTH) 
    sectors[17].addNeighbor(sectors[4], NORTH) 
    sectors[17].addNeighbor(sectors[16], EAST)
    sectors[17].addNeighbor(sectors[18], WEST)
    
    sectors[18].addNeighbor(sectors[5], NORTH) 
    sectors[18].addNeighbor(sectors[17], EAST)
    #sectors[18].addNeighbor(sectors[5], SOUTH)
    sectors[18].addNeighbor(sectors[19], WEST)
    
    #sectors[19].addNeighbor(sectors[0], SOUTH) 
    sectors[19].addNeighbor(sectors[6], NORTH) 
    sectors[19].addNeighbor(sectors[18], EAST)
    sectors[19].addNeighbor(sectors[20], WEST)

    #sectors[20].addNeighbor(sectors[0], SOUTH) 
    sectors[20].addNeighbor(sectors[21], NORTH) 
    sectors[20].addNeighbor(sectors[19], EAST)
    #sectors[20].addNeighbor(sectors[8], WEST)
    
    sectors[21].addNeighbor(sectors[20], SOUTH) 
    sectors[21].addNeighbor(sectors[22], NORTH) 
    sectors[21].addNeighbor(sectors[6], EAST)
    #sectors[21].addNeighbor(sectors[1], WEST)
    
    sectors[22].addNeighbor(sectors[21], SOUTH) 
    sectors[22].addNeighbor(sectors[23], NORTH) 
    sectors[22].addNeighbor(sectors[7], EAST)
    #sectors[22].addNeighbor(sectors[0], WEST)
    
    sectors[23].addNeighbor(sectors[22], SOUTH) 
    sectors[23].addNeighbor(sectors[24], NORTH) 
    sectors[23].addNeighbor(sectors[8], EAST)
    #sectors[23].addNeighbor(sectors[5], WEST)
    
    sectors[24].addNeighbor(sectors[23], SOUTH) 
    #sectors[24].addNeighbor(sectors[0], NORTH) 
    sectors[24].addNeighbor(sectors[9], EAST)
    #sectors[24].addNeighbor(sectors[6], WEST)
    
