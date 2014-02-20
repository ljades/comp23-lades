import pygame, os, sys
from pygame.locals import *
from random import randint

class Laser(pygame.sprite.Sprite):
        def load_image(self, image_name):
                ''' Following the proper image loading format '''
                try:
                        image = pygame.image.load(image_name)
                except pygame.error, message:
                        print "Cannot load image: " + image_name
                        raise SystemExit, message
                return image.convert_alpha()

        def __init__(self, screen, img_filename, init_x, init_y, init_x_speed, init_y_speed):
                ''' Laser-specific constructor '''
                pygame.sprite.Sprite.__init__(self)
                self.screen = screen

                self.image = self.load_image(img_filename)
                self.rect = self.image.get_rect()

                self.image_w, self.image_h = self.image.get_size()

                self.x = init_x
                self.y = init_y
                self.dx = init_x_speed
                self.dy = init_y_speed
                self.active = True

        def update(self):
                if (self.active == True):
                        ''' Reaching ends of screen detection '''
                        if ((self.x + self.image_w + self.dx) <= 0 or (self.x + self.dx) >= self.screen.get_size()[0]):
                                self.active = False
                        
                        if ((self.y + self.image_h + self.dy) <= 0 or (self.y + self.dy) >= self.screen.get_size()[1]):
                                self.active = False

                        self.x = self.x + self.dx
                        self.y = self.y + self.dy

        def draw(self):
                if (self.active == True):
                        draw_pos = self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
                        self.screen.blit(self.image, draw_pos)


if __name__ == "__main__":
	# Check if sound and font are supported
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"


        #Constants
        FPS = 50
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
        MIN_SPEED = 5
        MAX_SPEED = 12
        SPEED_X_BOUND = 5
        BACKGROUND_COLOR = (0, 0, 0)
        LASER_IMAGE = 'assets/assets/laser.gif'
        counter = 0
        
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('ALL OF THE LASERZ!!')
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 28)

        sprites = []
        
        while True:
                time_passed = clock.tick(FPS)

                # Event handling here (to quit)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

                
                screen.fill(BACKGROUND_COLOR)

                ''' Generate a new laser every so often '''
                if (counter % (FPS / 5) == 0):
                        sprites.append(Laser(screen, LASER_IMAGE, randint(1, SCREEN_WIDTH), SCREEN_HEIGHT - 1, randint(-1*SPEED_X_BOUND, SPEED_X_BOUND), -1*randint(MIN_SPEED, MAX_SPEED)))


                for sprite in sprites:
                        sprite.update()
                        sprite.draw()

                counter += 1

                pygame.display.flip()
