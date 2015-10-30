# Constants.py
# Universal constants for Sektor CS

# Constants pertaining to display
FRAMES_SEC = 50
WIDTH      = 800
HEIGHT     = 600
BACKGROUND = (0,0,0)

NORTH = 0
SOUTH = 1
EAST  = 2
WEST  = 3

NORTHERN_BOUNDARY = 2
SOUTHERN_BOUNDARY = 2
EASTERN_BOUNDARY  = 2
WESTERN_BOUNDARY  = 2


#Weapon Types
TYPE_L = 0
TYPE_M = 1
TYPE_B = 2

# Stats for main weapon
MAINGUN_DMG  = 10
MAINGUN_STAM = 0
MAINGUN_SPEED = 10
MAINGUN_COOLDOWN = 0.5

# Stats for bomb weapon
BOMB_DMG  = 60
BOMB_STAM = 100
BOMB_SPEED = 10
BOMB_COOLDOWN = 0.5
BOMB_COUNTDOWN = 2

# Stats for hero
HERO_MAX_SPEED = 8
HERO_ACCEL = 1
HERO_STAMINA_RECOVERY_RATE = 3 #HOW MANY TICKS TO RESTORE 1 STAMINA
HERO_DEATH_WAIT = 100 #number of ticks to pause the game after death

#Stats for Projectiles
PROJ_DEATH_TIME = 9 #How many ticks the collide image for a projectile will be displayed

#For missiles:
FAST_ACCEL = 1
SLOW_ACCEL = 0.5
VSLOW_ACCEL = 0.25
MAX_LOCK_DISTANCE = 400
M_DURABILITY = 4.0
MISSILE_DMG = 30
MISSILE_SPEED = 4
MISSILE_STAM = 40
MISSILE_COOLDOWN = 0.2


#For rock units:
ROCK_HP = 10
ROCK_ARMOR = 2
ROCK_TOUCH = 0 # No touch damage from basic rocks

# For upgrade packs:
UPGRADE_HP = 1000   # Placeholder value
UPGRADE_ARMOR = 0 # Placeholder value
UPGRADE_TOUCH = 0

#For Alien:
STRAFE_TIME = 100

#FINALBOSS Stuff
BOSSF_HP = 300
BOSS_ORB_HP = 50

#ARMOR CONSTANTS
BOMB_ONLY_ARMOR = BOMB_DMG - 10
MISSILE_ONLY_ARMOR = MISSILE_DMG - 10
