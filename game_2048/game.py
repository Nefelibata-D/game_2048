import pygame
from pygame.sprite import Group
import time
import base64
import os
import platform

from .settings import Settings
from .number import Number
from . import game_function as gf
from .scoreboard import Scoreboard
from .information import Information
from .button import Button
from .tips import Tips


# noinspection PyBroadException
def read_inf():
    try:
        local_inf = open('inf.txt', mode='r')
        base64_inf = local_inf.read().encode()
        inf = eval(base64.decodebytes(base64_inf).decode())
        local_inf.close()
    except:
        inf = {'bs': 0}
    return inf

def get_desktop():
    if platform.system().lower() == 'windows':
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        desktop = winreg.QueryValueEx(key, "Desktop")[0] + r'\game_2048\screenshot'
    elif platform.system().lower() == 'darwin':
        desktop = os.path.expanduser('~/Desktop/game_2048/screenshot')
    
    return desktop

def output():
    if platform.system().lower() == 'windows':
        os.system('cls')
    print('')
    print('')
    print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
    print('some tips:')
    print('')
    print(" - You can use ⬅  ⬆  ➡  ⬇  keys or 'AWSD' keys to remove the blocks on the screen ")
    print(" - Screenshot will be saved to ' ~/Desktop/game-2048/screenshots '")
    print(" - You can't make 4096 block when you have two 2048 blocks.")
    print("   So what you should do next is reset this game and start a new challenge.")
    print('')
    print(" That's all. Now, enjoy yourself !")
    print('')
    print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

def run_game():

    current_path = os.path.dirname(__file__)
    os.chdir(current_path)

    desktop = get_desktop()

    if not os.path.exists(desktop):
        os.makedirs(desktop)
    
    output()

    pygame.init()
    screen = pygame.display.set_mode((400, 650))
    pygame.display.set_caption('2048')
    settings = Settings()
    number = Number()
    button = Button(screen)
    blocks = Group()
    inf_read = read_inf()
    inf = Information()
    inf.best_score = inf_read['bs']
    scoreboard = Scoreboard(screen, settings, inf)
    tips = Tips(screen)
    try:
        process = inf_read['process']
        inf.score = inf_read['ns']
        number.row_list = process[0]
        number.column_list = process[1]
        inf.game_finish = inf_read['finish']
        inf.game_over = inf_read['over']
        gf.creat_block(blocks, settings, screen, number)
    except KeyError:
        gf.random_create(number)
        gf.random_create(number)
        number.row_to_column()
        gf.creat_block(blocks, settings, screen, number)

    while True:
        gf.transition(blocks)
        gf.check_events(settings, screen, number, blocks, inf, scoreboard, button, desktop)
        gf.update_screen(settings, screen, blocks, scoreboard, button, inf, tips)
        time.sleep(0.01)


run_game()
