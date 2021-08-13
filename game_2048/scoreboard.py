import pygame


# noinspection PyShadowingNames,PyTypeChecker,PyAttributeOutsideInit,PyRedundantParentheses
class Scoreboard():

    def __init__(self, screen, settings, inf):
        self.settings = settings
        self.inf = inf
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.bs_board_image = pygame.image.load('image/best_score.png')
        self.ns_board_image = pygame.image.load('image/now_score.png')
        self.bs_board_rect = self.bs_board_image.get_rect()
        self.ns_board_rect = self.ns_board_image.get_rect()

        self.bs_board_rect.right = self.screen_rect.right - 35
        self.ns_board_rect.right = self.screen_rect.right - 35
        self.bs_board_rect.top = 130
        self.ns_board_rect.top = self.bs_board_rect.bottom + 20

        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font('fonts/AmericanTypewriter.TTF', 32)

    def prep_score(self):
        now_score = str(self.inf.score)
        best_score = str(self.inf.best_score)
        self.ns_image = self.font.render(now_score, True, self.text_color, (238, 228, 218))
        self.bs_image = self.font.render(best_score, True, self.text_color, (238, 228, 218))

        self.ns_rect = self.ns_image.get_rect()
        self.bs_rect = self.bs_image.get_rect()

        self.ns_rect.centerx = self.ns_board_rect.centerx + 20
        self.ns_rect.centery = self.ns_board_rect.centery

        self.bs_rect.centerx = self.bs_board_rect.centerx + 20
        self.bs_rect.centery = self.bs_board_rect.centery

    def draw_scoreboard(self):
        self.prep_score()
        self.screen.blit(self.bs_board_image, self.bs_board_rect)
        self.screen.blit(self.ns_board_image, self.ns_board_rect)
        self.screen.blit(self.ns_image, self.ns_rect)
        self.screen.blit(self.bs_image, self.bs_rect)

    def check_break_record(self):
        if self.inf.score > self.inf.best_score:
            self.inf.best_score = self.inf.score
            self.text_color = (235, 80, 70)