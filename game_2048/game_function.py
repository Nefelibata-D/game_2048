import pygame
import sys
import random
import base64
import time
import os
import platform

from .block import Block


def update_screen(settings, screen, blocks, scoreboard, button, inf, tips):
    screen.fill((187, 173, 160))
    scoreboard.draw_scoreboard()
    update_tips(inf, settings, tips)
    if inf.roll_back_able:
        button.roll_back_image = pygame.image.load('image/roll_back.png')
    else:
        button.roll_back_image = pygame.image.load('image/roll_back_unable.png')
    button.draw_button()
    for block in blocks.sprites():
        if block.transition:
            size = block.transition_size
            image = pygame.transform.smoothscale(block.image, (size, size))
            block.blitme(image)
        elif block.combine_transition:
            size = block.transition_combine_size
            image = pygame.transform.smoothscale(block.image, (size, size))
            block.blitme(image)
        else:
            block.blitme(block.image)
    pygame.display.flip()


def check_events(settings, screen, number, blocks, inf, scoreboard, button, desktop):
    for event in pygame.event.get():
        transition_list = check_need_transition(blocks)
        if transition_list:
            break
        if inf.game_over and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button(settings, screen, number, blocks, inf, scoreboard, button, mouse_x, mouse_y, desktop)
        else:
            cancel_all_transition(number)  # reset transition of every block
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN and not inf.game_over:
                create_history(number, inf)
                check_keydown_event(event, settings, screen, number, blocks, inf)
                scoreboard.check_break_record()
                auto_save(inf, number)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_button(settings, screen, number, blocks, inf, scoreboard, button, mouse_x, mouse_y, desktop)


def creat_block(blocks, settings, screen, number):
    block = Block(settings, screen, (0, False))
    block_width = block.rect.width
    column_times = 0

    for row in number.row_list:
        row_times = 0
        for block_number in row:
            block = Block(settings, screen, block_number)
            if block.transition:
                extra = (block_width - block.transition_size) / 2
            elif block.combine_transition:
                extra = (block_width - block.transition_combine_size) / 2
            else:
                extra = 0
            block.x = settings.row_position[row_times] + extra
            block.rect.y = settings.column_position[column_times] + extra
            block.rect.x = block.x
            blocks.add(block)
            row_times += 1

        column_times += 1


def row_move(blocks, settings, screen, number, direction, inf):
    times = 0
    changes = []
    for row in number.row_list:
        result = number.combine(row, direction, inf)
        number.row_list[times] = result[0]
        changes.append(result[1])
        times += 1
    if False in changes:
        rest = random_create(number)
        number.row_to_column()
        if rest == 0:
            if check_game_over(number):
                inf.game_over = True
                creat_block(blocks, settings, screen, number)
                return None
        blocks.empty()
        creat_block(blocks, settings, screen, number)
        inf.roll_back_able = True


def column_move(blocks, settings, screen, number, direction, inf):
    times = 0
    changes = []
    for column in number.column_list:
        result = number.combine(column, direction, inf)
        number.column_list[times] = result[0]
        changes.append(result[1])
        times += 1
    if False in changes:
        number.column_to_row()
        rest = random_create(number)
        number.row_to_column()
        if rest == 0:
            if check_game_over(number):
                inf.game_over = True
                creat_block(blocks, settings, screen, number)
                return None
        blocks.empty()
        creat_block(blocks, settings, screen, number)
        inf.roll_back_able = True


def check_keydown_event(event, settings, screen, number, blocks, inf):
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        row_move(blocks, settings, screen, number, 1, inf)
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        row_move(blocks, settings, screen, number, -1, inf)
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        column_move(blocks, settings, screen, number, 1, inf)
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        column_move(blocks, settings, screen, number, -1, inf)


def random_create(number):
    available_list = []

    for i in number.row_list:
        if (0, False) in i:
            available_list.append(i)

    if len(available_list) != 0:
        row_list = random.choice(available_list)
        times = 0
        available_choice = []

        for i in row_list:
            if i[0] == 0:
                available_choice.append(times)
                times += 1
            else:
                times += 1
                continue

        index = random.choice(available_choice)
        row_list[index] = random.choice([(2, 'Create'), (4, 'Create')])

        return len(available_list) + len(available_choice) - 2
    else:
        return 0


def check_need_transition(blocks):
    transition_list = []
    for block in blocks.sprites():
        if block.transition or block.combine_transition:
            transition_list.append(block)
    return transition_list


def cancel_all_transition(number):
    for row in number.row_list:
        times = 0
        for n in row:
            row[times] = (n[0], False)
            times += 1


def transition(blocks):
    transition_list = check_need_transition(blocks)
    if transition_list:
        for block in transition_list:
            if block.transition:
                block.transition_size += 4
                block.rect.x -= 2
                block.rect.y -= 2
                if block.transition_size == 70:
                    block.transition = False
            else:
                block.transition_combine_size -= 4
                block.rect.x += 2
                block.rect.y += 2
                if block.transition_combine_size == 70:
                    block.combine_transition = False
                    block.transition_combine_size = 86


def auto_save(inf, number):
    local_inf = open('inf.txt', mode='w+')
    local_inf.seek(0)
    local_inf.truncate()
    process = [number.row_list, number.column_list]
    save_inf = {'ns': inf.score, 'bs': inf.best_score, 'process': process, 'finish': inf.game_finish, 'over': inf.game_over}
    base64_inf = base64.encodebytes(str(save_inf).encode('utf8'))
    local_inf.write(base64_inf.decode())
    local_inf.close()


def roll_back(number, inf, scoreboard):
    if inf.roll_back_able:
        local_history = open('history.txt', mode='r')
        history = eval(local_history.read())
        number.row_list = history['row']
        number.column_list = history['column']
        inf.score = history['ns']
        inf.best_score = history['bs']
        if inf.score < inf.best_score:
            scoreboard.text_color = (30, 30, 30)
        local_history.close()
        inf.roll_back_able = False


def check_button(settings, screen, number, blocks, inf, scoreboard, button, mouse_x, mouse_y, desktop):
    if button.roll_back_rect.collidepoint(mouse_x, mouse_y):
        roll_back(number, inf, scoreboard)
        creat_block(blocks, settings, screen, number)
        auto_save(inf, number)
    if button.screen_shot_rect.collidepoint(mouse_x, mouse_y):
        t = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())
        if platform.system().lower() == 'windows':
            pygame.image.save(screen, desktop + '\{}.png'.format(t))
        else:
            pygame.image.save(screen, desktop + '/{}.png'.format(t))
    if button.reset_rect.collidepoint(mouse_x, mouse_y):
        number.reset()
        blocks.empty()
        inf.reset()
        scoreboard.text_color = (30, 30, 30)
        random_create(number)
        random_create(number)
        number.row_to_column()
        creat_block(blocks, settings, screen, number)
    if button.exit_rect.collidepoint(mouse_x, mouse_y):
        quit_game()


def quit_game():
    local_history = open('history.txt', mode='w+')
    local_history.seek(0)
    local_history.truncate()
    local_history.close()
    os.remove('history.txt')
    if platform.system().lower() == 'windows':
        os.system('cls')
    sys.exit()


def check_game_over(number):

    for row in number.row_list:
        for i in range(0, 3):
            if row[i][0] == row[i + 1][0]:
                return False

    for column in number.column_list:
        for i in range(0, 3):
            if column[i][0] == column[i + 1][0]:
                return False

    return True


def create_history(number, inf):
    local_history = open('history.txt', mode='w+')
    history = {'row': number.row_list, 'column': number.column_list, 'ns': inf.score, 'bs': inf.best_score}
    local_history.seek(0)
    local_history.write(str(history))
    local_history.close()


def update_tips(inf, settings, tips):
    if inf.game_over:
        tips.draw_tips(settings.tips_2)
    elif inf.game_finish:
        tips.draw_tips(settings.tips_3)
    else:
        tips.draw_tips(settings.tips_1)
