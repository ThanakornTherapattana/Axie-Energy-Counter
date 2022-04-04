import pygame
from .constants import CLICK_SOUND


class Button:
    def __init__(self, x, y, image, scale):
        width, height = image.get_width(), image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x*scale, y*scale)
        self.clicked = False
        
    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))
        
    def check_mouse_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos) :
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                action = True
                self.clicked = True
                CLICK_SOUND.play()
                
                
        if pygame.mouse.get_pressed()[0] == 0 :
            self.clicked = False
            
        return action