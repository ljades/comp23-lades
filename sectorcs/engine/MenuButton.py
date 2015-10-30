import pygame, os, sys
from pygame.locals import *

class MenuButton(pygame.sprite.Sprite):
    """Class for the menu buttons"""
    
    def load_image(self, image_name):
        """The proper way to load an image"""
        try:
            image = pygame.image.load(image_name)
        except pygame.error, message:
            print "Cannot load image: " + image_name
            raise SystemExit, message
        return image.convert_alpha()
        
    def __init__(self, screen, img_filename, pressed_filename, x, y):
        """initaializes the button with its placement"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        
        #loads in the button image
        self.image = self.load_image(img_filename)
        self.image = pygame.transform.scale(self.image, (200, 75))
        self.rect = self.image.get_rect()
        
        #loads in the pressed button image
        self.press = self.load_image(pressed_filename)
        self.press = pygame.transform.scale(self.press, (200, 75))
        
        #set the image that is drawn
        self.draw_image = self.image
        
        # Get the image's width and height
        self.image_w, self.image_h = self.image.get_size()
			
        # Create a moving collision box
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Set the (x, y)
        self.x = x
        self.y = y
        
        #Set the flag for click
        self.clicked = False
        
    def update(self, m_pos, m_status):
        """This will check to see if the mouse is on the button"""
        self.draw_image = self.image
        self.clicked = False
        
        if ((self.rect.collidepoint(m_pos[0], m_pos[1]))):
            self.draw_image = self.press
            
            if(m_status[0] == True):
                self.clicked = True
        
    def draw(self):
        """draws the button with the correct state"""
        self.screen.blit(self.draw_image, (self.x, self.y))
            

        
        
        
        
        
        
        
        
