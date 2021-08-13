class Settings():

    def __init__(self):
        self.number_to_picture_dict = {0: 'image/0.png', 2: 'image/2.png', 4: 'image/4.png', 8: 'image/8.png',
                                       16: './image/16.png', 32: './image/32.png', 64: './image/64.png',
                                       128: './image/128.png',
                                       256: './image/256.png', 512: './image/512.png', 1024: './image/1024.png',
                                       2048: './image/2048.png'}

        self.block_height = 70
        self.block_width = 70
        self.scoreboard_width = 245
        self.scoreboard_height = 70
        self.total_block_x = self.block_width * 4 + self.block_width * 0.6
        self.total_block_y = self.block_width * 4 + self.block_width * 1.1
        self.available_x = (400 - self.total_block_x) / 2
        self.available_y = 700 - self.total_block_y - 50

        self.row_position = [self.available_x + self.block_width * 1.2 * 0,
                             self.available_x + self.block_width * 1.2 * 1,
                             self.available_x + self.block_width * 1.2 * 2,
                             self.available_x + self.block_width * 1.2 * 3]

        self.column_position = [self.available_y + + (self.block_height + 10) * 0,
                                self.available_y + + (self.block_height + 10) * 1,
                                self.available_y + + (self.block_height + 10) * 2,
                                self.available_y + + (self.block_height + 10) * 3]

        self.tips_1 = {'color': (250, 202, 192), 'text': 'Have A Good Time'}
        self.tips_2 = {'color': (156, 111, 105), 'text': 'G a m e   O v e r'}
        self.tips_3 = [{'color': (123, 65, 64), 'text': 'Congratulations!'},
                       {'color': (123, 65, 64), 'text': 'You have finished the game 2048!'}]
