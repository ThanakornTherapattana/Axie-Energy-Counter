import pygame
from axie.constants import WIDTH, HEIGHT
from axie.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Axie Energy Counter')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
         
        game.update()
          
    pygame.quit()
     
if __name__ == '__main__' :
    main()