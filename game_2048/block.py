import pygame
from pygame.sprite import Sprite

from .settings import Settings

settings = Settings()


# noinspection PyShadowingNames
class Block(Sprite):

    def __init__(self, settings, screen, number):
        super(Block, self).__init__()
        self.number = number
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.transition = False
        self.combine_transition = False
        if self.number[1] == 'Create':
            self.transition = True
            self.combine_transition = False
        elif self.number[1] == 'Combine':
            self.transition = False
            self.combine_transition = True
        self.transition_size = 30
        self.transition_combine_size = 86

        self.image_path = self.settings.number_to_picture_dict[number[0]]
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self, image):
        self.screen.blit(image, self.rect)
