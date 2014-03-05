import pygame, os, sys, Laser
from pygame.locals import *
from Laser import Laser
from random import randint

class Battlecruiser(pygame.sprite.Sprite):
        def load_image(self, image_name):
                ''' Following the proper image loading format '''
                try:
                        image = pygame.image.load(image_name)
                except pygame.error, message:
                        print "Cannot load image: " + image_name
                        raise SystemExit, message
                return image.convert_alpha()

        def __init__(self, screen, bc_filename, laser_filename, init_x, init_y, max_speed, laser_speed, horiz_accel, vert_accel, laser_sound):
                ''' Battlecruiser-specific constructor '''
                pygame.sprite.Sprite.__init__(self)
                self.screen = screen

		self.bc_image = self.load_image(bc_filename)
                self.l_filename = laser_filename
                self.rect = self.bc_image.get_rect()

                self.image_w, self.image_h = self.bc_image.get_size()
		try:
			temp_thing = pygame.mixer.Sound(laser_sound)
		except pygame.error, message:
                        print "Cannot load sound: " + laser_sound
                        raise SystemExit, message
		
		self.laser_sound = temp_thing
                self.x = init_x
                self.y = init_y
		self.init_xy = [init_x, init_y]
                self.dx = 0
                self.dy = 0
		self.max_speed = max_speed
                self.active = True
		if (horiz_accel >= 0):
			self.horiz_accel = horiz_accel
		else:
			self.horiz_accel = -1*horiz_accel
		if(vert_accel >= 0):
			self.vert_accel = vert_accel
		else:
			self.vert_accel = -1*vert_accel

		self.laser_speed = laser_speed
		self.lasers = []
		self.cooldown = 0
		self.on_the_edge = 0

		self.was_key_pressed = 0


	def fire_laser(self):
		if (self.cooldown <= 0):
			self.lasers.append(Laser(self.screen, self.l_filename, self.x + (self.bc_image.get_size()[0] / 2), self.y, 0, -1*self.laser_speed))
			self.lasers.append(Laser(self.screen, self.l_filename, self.x - (self.bc_image.get_size()[0] / 2), self.y, 0, -1*self.laser_speed))
			self.cooldown = 0.5
			self.laser_sound.play()
			if (len(self.lasers) > 6):
				self.lasers.pop(0)
	def reset_position(self):
		self.x, self.y = self.init_xy
		self.dx = 0
		self.dy = 0

	def accel_right(self):
		if (self.dx + self.horiz_accel >= self.max_speed):
			self.dx = self.max_speed
		else:
			self.dx += self.horiz_accel
		self.was_key_pressed = 1

	def accel_left(self):
		if (self.dx - self.horiz_accel <= -1*self.max_speed):
			self.dx = -1*self.max_speed
		else:
			self.dx -= self.horiz_accel
		self.was_key_pressed = 1

	def accel_down(self):
		if (self.dy + self.vert_accel >= self.max_speed):
			self.dy = self.max_speed
		else:
			self.dy += self.vert_accel
		self.was_key_pressed = 1

	def accel_up(self):
		if (self.dy - self.vert_accel <= -1*self.max_speed):
			self.dy = -1*self.max_speed
		else:
			self.dy -= self.vert_accel
		self.was_key_pressed = 1

        def update(self, FPS):
                if (self.active == True):
                        ''' Reaching ends of screen detection '''
                        if ((self.x + self.dx) <= 0 or (self.x + self.dx) >= self.screen.get_size()[0]):
                                self.on_the_edge = 1
                        
                        if ((self.y + self.dy) <= 0 or (self.y + self.dy) >= self.screen.get_size()[1]):
                                self.on_the_edge = 1



			if (self.on_the_edge == 1):
				self.on_the_edge = 0
			else:
				self.x = self.x + self.dx
				self.y = self.y + self.dy



			if (self.cooldown > 0):
				self.cooldown -= 1.0/FPS


			if (self.was_key_pressed == 0):
				self.dx -= 0.1*(self.dx)
				self.dy -= 0.1*(self.dy)
			else:
				self.was_key_pressed = 0

			for laser in self.lasers:
				laser.update()
				laser.draw()
		self.rect.move(self.x - self.image_w/2, self.y - self.image_h/2)
		self.rect.topleft = (self.x - self.image_w/2, self.y - self.image_h/2)
		self.rect.bottomright = (self.x + self.image_w/2, self.y + self.image_h/2)

        def draw(self):
                if (self.active == True):
                        draw_pos = self.bc_image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h / 2)
                        self.screen.blit(self.bc_image, draw_pos)


if __name__ == "__main__":
	# Check if sound and font are supported
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"


        #Constants
        FPS = 50
        SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	MAX_SPEED = 8
	LASER_SPEED = 12
	HORIZ_ACCEL = 5
	VERT_ACCEL = 8
        BACKGROUND_COLOR = (0, 0, 0)
        LASER_IMAGE = 'assets/assets/laser.gif'
	BC_IMAGE = 'assets/assets/battlecruiser.gif'
	LASER_SOUND = 'assets/assets/laser.wav'
        
        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Battlecruiser, Reporting!')
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 28)

	player = Battlecruiser(screen, BC_IMAGE, LASER_IMAGE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, MAX_SPEED, LASER_SPEED, HORIZ_ACCEL, VERT_ACCEL)
        
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

		player.update(FPS)
		player.draw()

                pygame.display.flip()
