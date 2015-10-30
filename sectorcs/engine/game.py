# Louis Ades, Will Hickey, Ryan Schumacher, Adam Zakaria
# Game.py
#
# The main game loop & menu screen.


import pygame, os, sys, Constants, Paths
from Constants import *
from Paths import *

sys.path.append("Units/")
sys.path.append("../sectors")

from Hero import Hero
from Turret_dumb import Turret_dumb
from pygame.locals import *
import random
from Sector import Sector
from MenuButton import MenuButton
from Asteroid import Asteroid

# Import all sectors
from sector0 import *
from sector1 import *
from sector2 import *
from sector3 import *
from sector4 import *
from sector5 import *
from sector6 import *
from sector7 import *
from sector8 import *
from outerSectors import *

from sectorNeighbors import *

# Runtime parameters
FPS = FRAMES_SEC
SCREEN_WIDTH  = WIDTH
SCREEN_HEIGHT = HEIGHT
BACKGROUND_COLOR = BACKGROUND


def get_js_pos( axis_pos):
    if(axis_pos > 0.1):
        return (100 * axis_pos)
    elif(axis_pos < -0.1):
        return (100 * axis_pos)
    else:
        return 0

def pause_game(time_out):
    '''PAUSE'''
    game_pause = True
    while game_pause == True:
        time_elapsed = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_pause = False
                elif event.key == K_p:
                    game_pause = False
            if ((joystick != None) and (joystick.get_init)):
                if(joystick.get_button(9)):
                    game_pause = False
        if(time_out == 0):
            game_pause = False
        time_out -= 1
        

def game_play():
    ''' After selecting "Play", this new game loop runs '''

    # Make the hero unit & grid of sectors
    hero = Hero(screen)

    # Create ALL sectors in the game
    sect0 = makeSector0(hero, screen)
    sect1 = makeSector1(hero, screen)
    sect2 = makeSector2(hero, screen)
    sect3 = makeSector3(hero, screen)
    sect4 = makeSector4(hero, screen)
    sect5 = makeSector5(hero, screen)
    sect6 = makeSector6(hero, screen)
    sect7 = makeSector7(hero, screen)
    sect8 = makeSector8(hero, screen)
    sect9 = makeSectorBound(hero, screen)
    sect10 = makeSectorBound(hero, screen)
    sect11 = makeSectorBound(hero, screen)
    sect12 = makeSectorBound(hero, screen)
    sect13 = makeSectorBound(hero, screen)
    sect14 = makeSectorBound(hero, screen)    
    sect15 = makeSectorBound(hero, screen)
    sect16 = makeSectorBound(hero, screen)    
    sect17 = makeSectorBound(hero, screen)    
    sect18 = makeSectorBound(hero, screen)    
    sect19 = makeSectorBound(hero, screen)    
    sect20 = makeSectorBound(hero, screen)    
    sect21 = makeSectorBound(hero, screen)    
    sect22 = makeSectorBound(hero, screen)    
    sect23 = makeSectorBound(hero, screen)    
    sect24 = makeSectorBound(hero, screen)

    # Establish the positional relationships between sectors
    makeNeighbors([sect0, sect1, sect2, sect3, sect4, sect5, sect6, sect7, 
                   sect8, sect9, sect10, sect11, sect12, sect13, sect14, 
                   sect15, sect16, sect17, sect18, sect19, sect20, sect21, 
                   sect22, sect23, sect24])

    background = sect1.background
    background_rect = background.get_rect()

    curSect = sect0
    curSect.loadTheme()
    pygame.mixer.music.play(-1)

    game_done = False

    ticks_elapsed = 0
    
    font = pygame.font.Font(None, 90)
    font.set_bold(True)
    pauseText = font.render("GAME PAUSED", 1, (51, 217, 34))
    
    heroGroup = pygame.sprite.Group()
    heroGroup.add(hero)
    # Game loop
    while (not game_done):
        time_elapsed = clock.tick(FPS)

        # TODO: Implement joystick controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_done = True
                elif event.key == K_DOWN:
                        hero.setDY(hero.speedSetting)
                elif event.key == K_LEFT:
                        hero.setDX(-1 * hero.speedSetting)
                elif event.key == K_RIGHT:
                        hero.setDX(hero.speedSetting)
                elif event.key == K_UP:
                        hero.setDY(-1 * hero.speedSetting)
                elif event.key == K_c:
                        hero.cycleWeapons()
                elif event.key == K_p:
                        screen.blit (pauseText, ((SCREEN_WIDTH / 2) - 200, (SCREEN_HEIGHT / 2) - 20))
                        pygame.display.update()
                        pause_game(-1)
                elif event.key == K_SPACE:
                    #TODO: Change these velocities according to rotation
                        newLaser = hero.fireWeapon(hero.x, hero.y, 14)
                        if (newLaser != None):
                            curSect.tempProjGroup.add(newLaser)
                            
            if ((joystick != None) and (joystick.get_init)):
                    if(joystick.get_button(6)):
                        newLaser = hero.fireWeapon(hero.x, hero.y, 14)
                        if (newLaser != None):
                            curSect.tempProjGroup.add(newLaser)
                    if(joystick.get_button(8)):
                        hero.cycleWeapons()
                    if(joystick.get_button(9)):
                        screen.blit (pauseText, ((SCREEN_WIDTH / 2) - 200, (SCREEN_HEIGHT / 2) - 20))
                        pygame.display.update()
                        pause_game(-1)
            

        # New event handling for mouse control
        # Start by getting the relative screen corner position:
        relScreenX = hero.x - (0.5 * SCREEN_WIDTH)
        relScreenY = hero.y - (0.5 * SCREEN_HEIGHT)

        (x_relative, y_relative) = pygame.mouse.get_pos()
        x_relative = x_relative - hero.x + relScreenX
        y_relative = y_relative - hero.y + relScreenY
        
        #js controls 
        if ((joystick != None) and (joystick.get_init)):
            x_relative = get_js_pos( joystick.get_axis(0))
            y_relative = get_js_pos( joystick.get_axis(1))
            hero.vector_path(x_relative, y_relative, 1)
            #print("x_rel: {} y_rel: {}".format(x_relative, y_relative))
        
        if (pygame.mouse.get_pressed()[0]):
            (x_relative, y_relative) = pygame.mouse.get_pos()
            x_relative = x_relative - hero.x + relScreenX
            y_relative = y_relative - hero.y + relScreenY
            hero.vector_path(x_relative, y_relative, 1)
            #print("x_rel: {} y_rel: {}".format(x_relative, y_relative))
        else:
            hero.vector_path(x_relative, y_relative, 0)
        if (pygame.mouse.get_pressed()[2]):
            newLaser = hero.fireWeapon(hero.x, hero.y, 14)
            if (newLaser != None):
                curSect.tempProjGroup.add(newLaser)
                

        curSect = curSect.checkTransition()
        background = curSect.background
        background_rect = background.get_rect()

        # Draw background, update sprites, redraw sprites

        #Then do the rest
        screen.fill(BACKGROUND_COLOR)
        screen.blit(background, background_rect.move(-relScreenX, -relScreenY))

        hero.update(hero)
        hero.draw(relScreenX, relScreenY, hero)

        # Check if hero is OOB:
        if (hero.x <=  10 and curSect.neighbors[WEST] == 0):
            hero.dx = hero.dx * -1.65

        if (hero.x >= curSect. width - 10 and curSect.neighbors[EAST] == 0):
            hero.dx = hero.dx * -1.65

        if (hero.y <= 10 and curSect.neighbors[NORTH] == 0):
            hero.dy = hero.dy * -1.65

        if (hero.y >= curSect.height - 10 and curSect.neighbors[SOUTH] == 0):
            hero.dy = hero.dy * -1.65

        

        if hero.level >= 5:
            victoryText = font.render("Earth is freed! Feel free to explore!", 
                                      1, (100, 200, 100))
            screen.blit (victoryText, (425, 40 + (7 * SCREEN_HEIGHT / 8)))

        # Update and draw everything in the sector....
        curSect.tempUnitGroup.update(hero)
        curSect.tempProjGroup.update(None, hero.x + (0.5 * SCREEN_WIDTH), hero.y + (0.5 * SCREEN_HEIGHT), hero, curSect.tempUnitGroup)
        #curSect.tempObstGroup.update()
        
        if((curSect.storm_side != 0) and (len(curSect.tempObstGroup) <= 25)):
            curSect.asteroid_storm(relScreenX, relScreenY, screen)
        
        #update for objects made this way for asteroid storm
        for obs in curSect.tempObstGroup:
            hit_flag = 0
            if(isinstance(obs, Asteroid)):
                for target in curSect.tempObstGroup:
                    obs.check_coll(target)
                    if(obs.hit_something == True):
                        obs.update(target, curSect.tempObstGroup)
                        hit_flag = 1
                        break
                if(hit_flag != 1):
                    obs.update(None, curSect.tempObstGroup)
            else:
                obs.update()

        # Manage the enemy projectiles:
        for unit in curSect.tempUnitGroup:

            # Moves the projectile
            unit.curWeap.firedList.update(hero,hero.x + (0.5 * SCREEN_WIDTH), hero.y + (0.5 * SCREEN_HEIGHT), hero, heroGroup)

            if not isinstance(unit, Hero):
                if unit.x <= WESTERN_BOUNDARY:
                    unit.x = random.randint (0, curSect.width)
                    unit.dx = unit.dx * -1
                if unit.x >= curSect.width - EASTERN_BOUNDARY:
                    unit.x = random.randint (0, curSect.width)
                    unit.dx = unit.dx * -1
                if unit.y <= 0:
                    unit.y = random.randint (0, curSect.width)
                    unit.dy = unit.dy * -1
                if unit.y >= curSect.height - SOUTHERN_BOUNDARY:
                    unit.y = random.randint (0, curSect.width)
                    unit.dy = unit.dy * -5
            
            # Hero's projectile hit this unit
            for laser in curSect.tempProjGroup:
                if(laser.hit_something == False):
                    if (laser.check_collide(unit) == True):
                        if (unit.active == False):
                            hero.hpCur = hero.hpCur + 5 # Killing enemies restores health
            
            for laser in unit.curWeap.firedList:
                laser.draw(relScreenX, relScreenY, hero)
            unit.draw(relScreenX, relScreenY, hero)
 
        # Draw the hero's projectile
        for proj in curSect.tempProjGroup:
            proj.draw(relScreenX, relScreenY, hero)

            for obst in curSect.tempObstGroup:
                if (proj.check_collide(obst) == True):
                    pass #TODO: Projectile repeatedly hits obst. Fix this

        for unit in curSect.tempObstGroup:
            unit.draw(relScreenX, relScreenY, hero)
            if (unit.check_collide(hero) == True):
                pass
 
        # Update health and stamina display
        font = pygame.font.Font(None, 30)
        hpText   = font.render("Health: " + str(hero.getHpCur()), 
                               1, (150, 200, 150))
        stamText = font.render("Stamina: " + str(hero.getStaminaCur()), 
                               1, (100, 200, 100))
        screen.blit (hpText, (SCREEN_WIDTH / 50, 7 * SCREEN_HEIGHT / 8))
        screen.blit (stamText, (SCREEN_WIDTH / 50, 
                                40 + (7 * SCREEN_HEIGHT / 8)))
        
        

        pygame.display.update()
        
        # Hero death --> Respawns at the coordinates stored in the sector
        if(hero.hpCur <= 0):

            # TODO: Death sound needs to be more pronounced
            hero.Death.play()
            font = pygame.font.Font(None, 90)
            font.set_bold(True)
            deathText = font.render("YOU DIED", 1, (51, 34, 217))
                        
            screen.blit (deathText, ((SCREEN_WIDTH / 2) - 200, (SCREEN_HEIGHT / 2) - 20))
            pygame.display.update()
            
            pause_game(HERO_DEATH_WAIT)

            # Respawn in the first sector
            hero.hpCur = hero.hpMax
            curSect = sect0
            hero.x = curSect.respawnX
            hero.y = curSect.respawnY

            # Reset the hitbox
            hero.rect.x = curSect.respawnX
            hero.rect.y = curSect.respawnY

            hero.rect.x = hero.rect.x - hero.image_w / 2
            hero.rect.y = hero.rect.y - hero.image_h / 2
            hero.active = True

        # Regenerate hero's stamina
        if ((ticks_elapsed % HERO_STAMINA_RECOVERY_RATE == 0) and (hero.staminaMax > hero.staminaCur)):
            hero.staminaCur += 1
            
        # Loop the music
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(curSect.music)
            pygame.mixer.music.play()

        ticks_elapsed += 1

    pygame.mixer.music.stop()

def load_image(image_name):
        """The proper way to load an image"""
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()        

# Main menu leads into the main game
if __name__ == "__main__":
    ''' Bring up the main menu, begin the game upon user's selection '''

    if not pygame.font:
        print "Warning, fonts disabled"
    if not pygame.mixer:
        print "Warning, sound disabled"

    # Pygame Initialization
    pygame.mixer.pre_init(44100, -16, 2, 2048)# setup mixer to avoid sound lag
    pygame.init()
    pygame.display.set_caption('Sektor CS')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock  = pygame.time.Clock()    
    
    # Initialize the joysticks
    joystick = None
    for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print("WE HAVE A JOYSTICK!")
    
    
    
    # Load main menu and music
    background_image = load_image(Paths.MAIN_BG)
    background_image = pygame.transform.scale(background_image, 
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))
                                              
    background_ctrl = load_image(Paths.SEKT_3)
    background_ctrl = pygame.transform.scale(background_ctrl, 
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.mixer.music.load(Paths.MAIN_MUSIC)
    pygame.mixer.music.play()

    # Create the buttons
    play_button = MenuButton(screen, Paths.MAIN_PLAY, Paths.MAIN_PLAY_P, 100, 225)
    ctrl_button = MenuButton(screen, Paths.MAIN_CTRL, Paths.MAIN_CTRL_P, 100, 350)
    exit_button = MenuButton(screen, Paths.MAIN_EXIT, Paths.MAIN_EXIT_P, 100, 475)
    back_button = MenuButton(screen, Paths.MAIN_BACK, Paths.MAIN_BACK_P, 100, 475)
    
    ctrl_flag = False
    chill = 0
    
    # Background = sect1.background
    background_rect = background_image.get_rect()

    while True:

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(Paths.MAIN_MUSIC)
            pygame.mixer.music.play()

        time_elapsed = clock.tick(FPS)
        
        play_button.clicked = False
        ctrl_button.clicked = False
        exit_button.clicked = False
        back_button.clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        #joystick test
        #axes = joystick.get_numaxes()
        #for i in range( axes ):
        #    axis = joystick.get_axis( i )
        #    print( "Axis {} value: {:>6.3f}".format(i, axis) )
        
        # Process mouse selection
        m_pos    = pygame.mouse.get_pos()
        m_status = pygame.mouse.get_pressed()

        # Update the button status
        if(ctrl_flag == False):
        
            # Draw background, update sprites, redraw sprites
            screen.fill(BACKGROUND_COLOR)
            screen.blit(background_image, background_rect)
        
            play_button.update(m_pos, m_status)
            ctrl_button.update(m_pos, m_status)
            exit_button.update(m_pos, m_status)
            
            play_button.draw()
            ctrl_button.draw()
            exit_button.draw()
            chill -= 1
        if(ctrl_flag == True):
        
            # Draw background, 
            screen.fill(BACKGROUND_COLOR)
            screen.blit(background_ctrl, background_rect)
        
            font = pygame.font.Font(None, 30)
            story1 = font.render("Earth has been captured by an alien race! You must find a" , 1, (255, 255, 255))
            story2 = font.render("way to turn off the force field that is suffocating Earth." , 1, (255, 255, 255))
            story3 = font.render("Figures that today you were assigned to a mining mission" , 1, (255, 255, 255))
            story4 = font.render("in this POS mining rig... If only you hadn't pulled that" , 1, (255, 255, 255))
            story5 = font.render("prank on your commanding officer, you would not be in this" , 1, (255, 255, 255))
            story6 = font.render("mess. You look around the cockpit to take stock of your" , 1, (255, 255, 255))
            story7 = font.render("weapons...NOTHING!" , 1, (255, 255, 255))
            story8 = font.render("As you ponder your now assured depressingly short future, you" , 1, (255, 255, 255))
            story9 = font.render("absent mindedly read the control panel of this hunk of junk:" , 1, (255, 255, 255))
            story10 = font.render("Mouse = Direction faced" , 1, (255, 255, 255))
            story11 = font.render("Left click = Move forward" , 1, (255, 255, 255))
            story12 = font.render("Right click = Fire current weapon" , 1, (255, 255, 255))
            story13 = font.render("When using a Joystick" , 1, (255, 255, 255))
            story14 = font.render("joystick = Direction and Move" , 1, (255, 255, 255))
            story15 = font.render("A = Fire current weapon" , 1, (255, 255, 255))
            
            
            screen.blit(story1, (100, 50))
            screen.blit(story2, (100, 75))
            screen.blit(story3, (100, 100))
            screen.blit(story4, (100, 125))
            screen.blit(story5, (100, 150))
            screen.blit(story6, (100, 175))
            screen.blit(story7, (100, 200))
            screen.blit(story8, (100, 225))
            screen.blit(story9, (100, 250))
            screen.blit(story10, (100, 275))
            screen.blit(story11, (100, 300))
            screen.blit(story12, (100, 325))
            screen.blit(story13, (100, 375))
            screen.blit(story14, (100, 400))
            screen.blit(story15, (100, 425))
            
            
            back_button.update(m_pos, m_status)
            back_button.draw()
        
        if(ctrl_button.clicked == True):
            ctrl_flag = True
        if(back_button.clicked == True):
            ctrl_flag = False
            chill = 10
        if(play_button.clicked == True):
            pygame.mixer.music.stop()
            game_play()
        if(exit_button.clicked == True and chill <= 0):
            pygame.quit()
            sys.exit()

        pygame.display.update()
