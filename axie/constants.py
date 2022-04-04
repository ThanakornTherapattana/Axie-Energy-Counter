import pygame
pygame.init()

WIDTH, HEIGHT = 300, 400

WHITE = (255,255,255)
BLACK = (0,0,0)

BACKGROUND = pygame.image.load('assets/back_beta.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

ENERGY_IMG = pygame.image.load('assets/energy.png')
ENERGY_IMG = pygame.transform.scale(ENERGY_IMG, (16*5, 16*5))

RESET_BUTTON = pygame.image.load('assets/reset_button.png')
NEXT_BUTTON = pygame.image.load('assets/next_button.png')
UNDO_BUTTON = pygame.image.load('assets/undo_button.png')
PLUS_BUTTON = pygame.image.load('assets/plus_button.png')
MINUS_BUTTON = pygame.image.load('assets/minus_button.png')

ENERGY_FONT = pygame.font.Font(('assets/Minecraftia-Regular.ttf'), 40)
OTHER_ENERGY_FONT = pygame.font.Font(('assets/Minecraftia-Regular.ttf'), 20)
ENERGY_NAME_FONT = pygame.font.Font(('assets/Minecraftia-Regular.ttf'), 12)