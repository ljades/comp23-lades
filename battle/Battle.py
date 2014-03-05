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

    font = pygame.font.Font(None, 40)
    giantfont = pygame.font.Font(None, 40)
    SCORE_LOCATION = (10, 10)
    GOVER_LOCATION = (30, 30)

    try:
        background_music = pygame.mixer.Sound(BACKGROUND_MUSIC)
        explosion_sound = pygame.mixer.Sound(EXPLOSION_SOUND)
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
    game_over = False
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
        
        #update stuff
        enemy_index = 0
        for enemy in enemies:
            if enemy.active == False:
                enemies.pop(enemy_index)
            else:
                enemy.update(FPS)
                enemy.draw()
            enemy_index += 1
            

        player.update(FPS)
        player.draw()

        counter += 1
        y_pos_on_scroll += 1

        ''' collision detection '''
        for enemy in enemies:
            for laser in player.lasers:
                if (pygame.sprite.collide_rect(laser, enemy) and enemy.exploding == False):
                    score += 100
                    enemy.explode()
                    break
        #check if player lost
        for enemy in enemies:
            if (pygame.sprite.collide_rect(player, enemy) == True):
                game_over = True
                break

        score_text = font.render("Score: " + str(score), 1, (60, 255, 30))
        screen.blit(score_text, SCORE_LOCATION)

        pygame.display.flip()

        if (game_over == True):
            explosion_sound.play()
            game_over = False
            score = 0
            counter = 0
            y_pos_on_scroll = -1*background_image.get_size()[1] + SCREEN_HEIGHT
            enemies = []
            gover_text = giantfont.render("GAME OVER! PRESS ENTER TO PLAY AGAIN", 1, (60, 255, 30))
            
            screen.blit(gover_text, GOVER_LOCATION)
            pygame.display.flip()
            while (1):
                #print something

                play_again = False
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        if event.key == K_RETURN:
                            play_again = True
                if play_again:
                    break
                
