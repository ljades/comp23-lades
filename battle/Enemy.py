import pygame, os, sys, Laser
from pygame.locals import *
from random import randint

class Enemy(pygame.sprite.Sprite):
        def load_image(self, image_name):
                ''' Following the proper image loading format '''
                try:
                        image = pygame.image.load(image_name)
                except pygame.error, message:
                        print "Cannot load image: " + image_name
                        raise SystemExit, message
                return image.convert_alpha()

        def __init__(self, screen, enemy_filename, explosion_filename, init_x, init_y, init_dx, init_dy):
                ''' Enemy-specific constructor '''
                pygame.sprite.Sprite.__init__(self)
                self.screen = screen

		self.enemy_image = self.load_image(enemy_filename)
                self.explosion_image = self.load_image(explosion_filename)
                self.rect = self.enemy_image.get_rect()

                self.image_w, self.image_h = self.enemy_image.get_size()
		self.image_w2, self.image_h2 = self.explosion_image.get_size()

                self.x = init_x
                self.y = init_y
                self.dx = init_dx
                self.dy = init_dy
                self.active = True
		self.exploding = False
		self.explode_countdown = 1.0

	def explode(self):
		self.exploding = True
		self.dx = 0
		self.dy = 0


        def update(self, FPS):
                if ((self.active == True) and (self.exploding == False)):
                        ''' Reaching ends of screen detection '''
                        if ((self.x + self.dx) <= 0 or (self.x + self.dx) >= self.screen.get_size()[0]):
                                self.dx = -1 * self.dx
                        
                        if ((self.y + self.dy) <= 0 or (self.y + self.dy) >= self.screen.get_size()[1]):
                                self.dy = -1 * self.dy


			self.x = self.x + self.dx
			self.y = self.y + self.dy

		elif (self.active == True and self.exploding == True):
			if self.explode_countdown <= 0.0:
				self.active = False
			else:
				self.explode_countdown -= 2/FPS


        def draw(self):
                if (self.active == True and self.exploding == False):
                        draw_pos = self.enemy_image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
                        self.screen.blit(self.enemy_image, draw_pos)
		elif (self.active == True and self.exploding == True):
			draw_pos = self.explosion_image.get_rect().move(self.x - self.image_w2 / 2, self.y - self.image_h2 / 2)


if __name__ == "__main__":
	# Check if sound and font are supported
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"


        #Constants
	if (len(sys.argv) == 2):
		try:
			NUM_ENEMIES = int(sys.argv[1])
		except:
			NUM_ENEMIES = 10
	else:
		NUM_ENEMIES = 10
	MAX_SPEED_X = 10
	MAX_SPEED_Y = 10
        FPS = 50
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
        BACKGROUND_COLOR = (255, 255, 255)
        ENEMY_IMAGE = "assets/assets/mutalisk.gif"
	EXPLODE_IMAGE = "assets/assets/laser_explosion.gif"
        
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Battlecruiser, Reporting!')
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 28)

	sprites = []

	for i in range(0, NUM_ENEMIES):
		sprites.append(Enemy(screen, ENEMY_IMAGE, EXPLODE_IMAGE, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, randint(-1*MAX_SPEED_X, MAX_SPEED_X), randint(-1*MAX_SPEED_Y, MAX_SPEED_Y)))
        
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

		for sprite in sprites:
			sprite.update(FPS)
			sprite.draw()

                pygame.display.flip()
