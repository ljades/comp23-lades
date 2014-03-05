import pygame, os, sys, Laser
from pygame.locals import *
from Laser import Laser
from Enemy import Enemy
from Battlecruiser import Battlecruiser
from random import randint

if __name__ == "__main__":
    # Check if sound and font are supported
    if not pygame.font:
        print "Warning, fonts disabled"
    if not pygame.mixer:
        print "Warning, sound disabled"

    #Constants
    FPS = 50
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BC_MAX_SPEED = 8
    LASER_SPEED = 12
    BC_X_ACCEL = 5
    BC_Y_ACCEL = 8
    BACKGROUND_COLOR = (0, 0, 0)
    LASER_IMAGE = 'assets/assets/laser.gif'
    BC_IMAGE = 'assets/assets/battlecruiser.gif'
    ENEMY_IMAGE = 'assets/assets/mutalisk.gif'
    EXPLODE_IMAGE = 'assets/assets/laser_explosion.gif'
    LASER_SOUND = 'assets/assets/laser.wav'
    BACKGROUND_IMAGE = 'assets/assets/ram_aras.png'
    BACKGROUND_MUSIC = 'assets/assets/main_theme.wav'
    EXPLOSION_SOUND = 'assets/assets/death_explode.wav'
    ENEMY_MAX_SPEED = 4

    pygame.init()

    try:
        background_music = pygame.mixer.Sound(BACKGROUND_MUSIC)
    except:
        print "Sound not working."

    background_music.play(-1)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Battlecruiser, Reporting!')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 28)

    background_image = pygame.image.load(BACKGROUND_IMAGE)
    background_image = background_image.convert_alpha()
    y_pos_on_scroll = -1*background_image.get_size()[1] + SCREEN_HEIGHT 

    enemies = []

    player = Battlecruiser(screen, BC_IMAGE, LASER_IMAGE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BC_MAX_SPEED, LASER_SPEED, BC_X_ACCEL, BC_Y_ACCEL, LASER_SOUND)

    score = 0
    counter = 0
    while True:
        time_passed = clock.tick(FPS)

        #Event handling here (to quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT:
                    player.accel_left()
                if event.key == K_RIGHT:
                    player.accel_right()
                if event.key == K_UP:
                    player.accel_up()
                if event.key == K_DOWN:
                    player.accel_down()
                if event.key == K_SPACE:
                    player.fire_laser()

        screen.fill(BACKGROUND_COLOR)
        screen.blit(background_image, background_image.get_rect().move(0, y_pos_on_scroll))
        if (y_pos_on_scroll == SCREEN_HEIGHT):
                y_pos_on_scroll = -1*background_image.get_size()[1] + SCREEN_HEIGHT
        elif (y_pos_on_scroll >= 0):
            screen.blit(background_image, background_image.get_rect().move(0, y_pos_on_scroll - background_image.get_size()[1] ))

        ''' Generate a new enemy every so often '''
        if (len(enemies) <= 10 and counter % (FPS * 2) == 0):
            enemies.append(Enemy(screen, ENEMY_IMAGE, EXPLODE_IMAGE, randint(0, SCREEN_WIDTH), 1, randint(-1*ENEMY_MAX_SPEED, ENEMY_MAX_SPEED), ENEMY_MAX_SPEED, ))


        #collision detection
        
        #update stuff
        for enemy in enemies:
            enemy.update(FPS)
            enemy.draw()

        player.update(FPS)
        player.draw()

        counter += 1
        y_pos_on_scroll += 1

        pygame.display.flip()
