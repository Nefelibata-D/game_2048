import pygame


# noinspection PyAttributeOutsideInit,PyRedundantParentheses
class Tips():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

    def prep_score(self, tips):
        if type(tips) == list:
            self.text_color = tips[0]['color']

            self.font_1 = pygame.font.Font('fonts/STXINGKA.TTF', 50)
            self.tips = (tips[0]['text'], tips[1]['text'])
            self.tips_image_1 = self.font_1.render(self.tips[0], True, self.text_color, (187, 173, 160))
            self.tips_rect_1 = self.tips_image_1.get_rect()
            self.tips_rect_1.centerx = self.screen_rect.centerx
            self.tips_rect_1.top = 10

            self.font_2 = pygame.font.Font('fonts/STXINGKA.TTF', 34)
            self.tips_image_2 = self.font_2.render(self.tips[1], True, self.text_color, (187, 173, 160))
            self.tips_rect_2 = self.tips_image_2.get_rect()
            self.tips_rect_2.centerx = self.screen_rect.centerx
            self.tips_rect_2.top = self.tips_rect_1.bottom + 8
        else:
            self.font = pygame.font.Font('fonts/STXINGKA.TTF', 52)
            self.text_color = tips['color']
            self.tips = tips['text']
            self.tips_image = self.font.render(self.tips, True, self.text_color, (187, 173, 160))
            self.tips_rect = self.tips_image.get_rect()
            self.tips_rect.centerx = self.screen_rect.centerx
            self.tips_rect.top = 40

    def draw_tips(self, tips):
        self.prep_score(tips)
        if type(tips) == list:
            self.screen.blit(self.tips_image_1, self.tips_rect_1)
            self.screen.blit(self.tips_image_2, self.tips_rect_2)
        else:
            self.screen.blit(self.tips_image, self.tips_rect)
