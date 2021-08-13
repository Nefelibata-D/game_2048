import pygame


# noinspection PyRedundantParentheses
class Button():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.bg_image = pygame.image.load('image/bt_bg.png')
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.left = 35
        self.bg_rect.top = 130

        self.screen_shot_image = pygame.image.load('image/screen_shot.png')
        self.screen_shot_rect = self.screen_shot_image.get_rect()
        self.screen_shot_rect.left = self.bg_rect.left + 10
        self.screen_shot_rect.top = self.bg_rect.top + 12

        self.exit_image = pygame.image.load('image/exit.png')
        self.exit_rect = self.exit_image.get_rect()
        self.exit_rect.right = self.bg_rect.right - 10
        self.exit_rect.top = self.bg_rect.top + 12

        self.roll_back_image = pygame.image.load('image/roll_back.png')
        self.roll_back_rect = self.roll_back_image.get_rect()
        self.roll_back_rect.left = self.bg_rect.left + 10
        self.roll_back_rect.bottom = self.bg_rect.bottom - 12

        self.reset_image = pygame.image.load('image/reset.png')
        self.reset_rect = self.reset_image.get_rect()
        self.reset_rect.right = self.bg_rect.right - 10
        self.reset_rect.bottom = self.bg_rect.bottom - 12

    def draw_button(self):
        self.screen.blit(self.bg_image, self.bg_rect)
        self.screen.blit(self.screen_shot_image, self.screen_shot_rect)
        self.screen.blit(self.exit_image, self.exit_rect)
        self.screen.blit(self.roll_back_image, self.roll_back_rect)
        self.screen.blit(self.reset_image, self.reset_rect)
