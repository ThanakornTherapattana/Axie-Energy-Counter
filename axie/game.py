import pygame
from .button import Button
from .constants import (WHITE, BACKGROUND, RESET_BUTTON, NEXT_BUTTON, UNDO_BUTTON, ENERGY_NAME_FONT, 
                        PLUS_BUTTON, MINUS_BUTTON, ENERGY_FONT, WIDTH, BLACK, OTHER_ENERGY_FONT)




class Game:
    def __init__(self,win):
        self.win = win
        self.reset_button = Button(1, 1 , RESET_BUTTON, 5)
        self.next_button = Button(31, 67, NEXT_BUTTON, 5)
        self.undo_button = Button(11, 67, UNDO_BUTTON, 5)
        
        self.plus1 = Button(39, 26, PLUS_BUTTON, 5)
        self.plus2 = Button(39, 40, PLUS_BUTTON, 5)
        self.plus3 = Button(39, 54, PLUS_BUTTON, 5)
        
        self.minus1 = Button(11, 26, MINUS_BUTTON, 5)
        self.minus2 = Button(11, 40, MINUS_BUTTON, 5)
        self.minus3 = Button(11, 54, MINUS_BUTTON, 5)
        self._init()
        
        
    def _init(self):
        self.energy = 3
        self.energy_history = []
        self.round = 1
        self.gained = 0
        self.used = 0
        self.destroyed = 0
            
    def reset(self):
        if self.reset_button.check_mouse_click() :
            self._init()
            print('reset')

        
    def draw_text(self):
        #total energy
        energy_text = ENERGY_FONT.render(f"{self.energy}", 1, BLACK)
        self.win.blit(energy_text,(WIDTH//2 - energy_text.get_width()//2, 45))
        
        #round
        round_text = ENERGY_NAME_FONT.render('ROUND ' + f"{self.round}", 1, WHITE)
        self.win.blit(round_text,(WIDTH//2 - round_text.get_width()//2, 10))
        
        #energy number
        used_energy_text = OTHER_ENERGY_FONT.render(f"{self.used}", 1, WHITE)
        gained_energy_text = OTHER_ENERGY_FONT.render(f"{self.gained}", 1, WHITE)
        destroyed_energy_text = OTHER_ENERGY_FONT.render(f"{self.destroyed}", 1, WHITE)
        
        self.win.blit(used_energy_text,(WIDTH//2 - used_energy_text.get_width()//2, 30*5))
        self.win.blit(gained_energy_text,(WIDTH//2 - gained_energy_text.get_width()//2, 44*5))
        self.win.blit(destroyed_energy_text,(WIDTH//2 - destroyed_energy_text.get_width()//2, 58*5))
        
        #energy name
        used_energy_text_n = ENERGY_NAME_FONT.render("USED", 1, WHITE)
        gained_energy_text_n = ENERGY_NAME_FONT.render("GAINED", 1, WHITE)
        destroyed_energy_text_n = ENERGY_NAME_FONT.render("DESTROYED", 1, WHITE)
        
        self.win.blit(used_energy_text_n,(WIDTH//2 - used_energy_text_n.get_width()//2, 26*5))
        self.win.blit(gained_energy_text_n,(WIDTH//2 - gained_energy_text_n.get_width()//2, 40*5))
        self.win.blit(destroyed_energy_text_n,(WIDTH//2 - destroyed_energy_text_n.get_width()//2, 54*5))
        
    def draw_button(self):
        
        self.reset_button.draw(self.win)
        
        
        self.next_button.draw(self.win) 
        self.undo_button.draw(self.win)
        
        
        self.plus1.draw(self.win)       
        self.plus2.draw(self.win)
        self.plus3.draw(self.win)

        
        self.minus1.draw(self.win)
        self.minus2.draw(self.win)
        self.minus3.draw(self.win)
    
    def plus_minus(self):
        if self.energy > 0 :
            if self.plus1.check_mouse_click() and self.used < 10:
                self.used += 1
                self.energy -= 1
            if self.plus3.check_mouse_click() and self.destroyed < 10:
                self.destroyed += 1
                self.energy -= 1
            if self.minus2.check_mouse_click() and self.gained > 0:
                self.gained -= 1
                self.energy -= 1
        
        if self.energy < 10 :         
            if self.plus2.check_mouse_click() and self.gained < 10:
                self.gained += 1
                self.energy += 1
            if self.minus1.check_mouse_click() and self.used > 0:
                self.used -= 1
                self.energy += 1
            if self.minus3.check_mouse_click() and self.destroyed > 0:
                self.destroyed -= 1
                self.energy += 1
    
    def next_previous_round(self):
        if self.round == 1 :
            self.last_energy = 3
            
        #press next button
        if self.next_button.check_mouse_click():
            self.round += 1
            self.energy += 2
            
            if self.energy > 10 :
                self.energy = 10
            
            self.energy_history.append(self.last_energy)
            self.last_energy = self.energy
            
            self.gained = 0
            self.used = 0
            self.destroyed = 0
            print(self.energy_history)
        
        #press undo button 
        if self.undo_button.check_mouse_click() and self.round > 1 :
            self.round -= 1
            self.energy = self.energy_history.pop()
            self.last_energy = self.energy
             
            self.gained = 0
            self.used = 0
            self.destroyed = 0
            print(self.energy_history)
                    
    def update(self):
        self.win.blit(BACKGROUND, (0,0))
        self.draw_button()
        self.draw_text()
        
        self.plus_minus()
        self.next_previous_round()
        self.reset()
        
        pygame.display.update()