# noinspection PyAttributeOutsideInit,PyMethodMayBeStatic,PyShadowingBuiltins,DuplicatedCode
class Number:

    def __init__(self):
        # 继承settings内的初始化行与列
        self.row_list = []
        self.column_list = []
        self.reset()

    def row_to_column(self):
        #  由行向列同步转换
        times = 0
        for row in self.row_list:
            timess = 0
            for column in self.column_list:
                column[times] = row[timess]
                timess += 1
            times += 1

    def column_to_row(self):
        #  由列向行同步转换
        times = 0
        for column in self.column_list:
            timess = 0
            for row in self.row_list:
                row[times] = column[timess]
                timess += 1
            times += 1

    def reset(self):
        self.row_list = [[(0, False), (0, False), (0, False), (0, False)],
                         [(0, False), (0, False), (0, False), (0, False)],
                         [(0, False), (0, False), (0, False), (0, False)],
                         [(0, False), (0, False), (0, False), (0, False)]]
        self.column_list = [[(0, False), (0, False), (0, False), (0, False)],
                            [(0, False), (0, False), (0, False), (0, False)],
                            [(0, False), (0, False), (0, False), (0, False)],
                            [(0, False), (0, False), (0, False), (0, False)]]

    def delete_zero(self, list_2048):
        none_zero_list = []
        for i in list_2048:
            if not i[0] == 0:
                none_zero_list.append(i[0])
            else:
                continue
        return none_zero_list

    def add_zero(self, list_2048, direction):
        list = list_2048
        if direction > 0:  # right
            for i in range(4 - len(list)):
                list.append((0, False))
        else:
            times = 0
            for i in range(4 - len(list)):
                list.insert(times, (0, False))
                times += 1
        return list

    def combine(self, block_list, direction, inf):
        none_zero_list = self.delete_zero(block_list)
        new_list = []
        times = 0
        while True:
            try:
                if none_zero_list[times] == none_zero_list[times + 1]:
                    new_list.append((none_zero_list[times] * 2, 'Combine'))
                    inf.score += none_zero_list[times] * 2
                    times += 2
                else:
                    new_list.append((none_zero_list[times], False))
                    times += 1
            except IndexError:
                if times == len(none_zero_list) - 1:
                    new_list.append((none_zero_list[times], False))
                break
        add_zero_list = self.add_zero(new_list, direction)
        if add_zero_list == block_list:
            same = True
        else:
            same = False
        return add_zero_list, same
