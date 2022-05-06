import datetime
import random
import time


class Barrel:
    def __init__(self, num):
        self.number = num
        self.marked = False

    def __int__(self):
        return self.number


class LotoBag:
    def __init__(self):
        self.unmarked_barrels = [i + 1 for i in range(0, 90)]
        self.marked_barrels = []
        random.shuffle(self.unmarked_barrels)

    def get_next(self):
        if len(self.unmarked_barrels) > 0:
            return self.unmarked_barrels[0]
        else:
            return 0

    def mark_next(self):
        self.marked_barrels.append(self.unmarked_barrels.pop(0))

    def reset(self):
        self.unmarked_barrels = [i + 1 for i in range(0, 90)]
        self.marked_barrels = []
        random.shuffle(self.unmarked_barrels)


def change_seed():
    random.seed(datetime.datetime.now().microsecond.__int__() - random.randint(0, 999))


class LotoCard:
    def __init__(self, size=[3, 9, 5]):
        self.rows = []
        for rc in range(0, size[0]):
            self.rows.append([1 for i in range(0, size[2])] + [0 for i in range(0, size[1] - size[2])])

            random.shuffle(self.rows[rc])
        nums = [i + 1 for i in range(0, 90)]
        random.shuffle(nums)
        self.lots = [nums[v] for v in range(0, size[0] * size[2])]
        random.shuffle(self.lots)

    def is_completed(self, marked_barrels):
        for lot in self.lots:
            if lot not in marked_barrels:
                return False
        return True

    def print(self, marked_barrels):
        b_index = 0
        print("---" * len(self.rows[0]))
        lot_index = 0
        for r in self.rows:
            line = ""
            for cell in r:
                if cell == 1:
                    if self.lots[lot_index] in marked_barrels:
                        line += " X "
                    else:
                        if self.lots[lot_index] < 10:
                            line += " " + self.lots[lot_index].__str__() + " "
                        else:
                            line += self.lots[lot_index].__str__() + " "
                    lot_index += 1
                else:
                    line += "   "
            print(line)
        print("---" * len(self.rows[0]))


class LotoGameVSBot:
    def __init__(self, cardsize=[3, 9, 5]):
        change_seed()
        # 3 - rows, 9 - row length, 5 - nums in row
        self.bag = LotoBag()
        self.playercard = LotoCard()
        change_seed()
        self.botcard = LotoCard()
        self.playername = ""

    def start(self):
        self.playername = input("Введите своё имя: ")
        while True:
            current_barrel = self.bag.get_next()
            if current_barrel != 0:
                # new barrel printing here
                print("Новый бочонок: " + current_barrel.__str__(), end=" (")
                print("осталось " + str(len(self.bag.unmarked_barrels)) + ")")
                ###
                # cards printing here
                print("Карточка бота:")
                self.botcard.print(self.bag.marked_barrels)
                print(f"Карточка игрока {self.playername}:")
                self.playercard.print(self.bag.marked_barrels)
                if self.playercard.is_completed(self.bag.marked_barrels) and self.botcard.is_completed(self.bag.marked_barrels):
                    print("Ничья")
                    return 0
                elif self.playercard.is_completed(self.bag.marked_barrels):
                    print(f"Игрок {self.playername} выиграл")
                    return 1
                elif self.botcard.is_completed(self.bag.marked_barrels):
                    print("Бот выиграл")
                    return -1
                else:
                    ###
                    while True:
                        answer = input(f"Зачеркнуть число {current_barrel}? y/n\n")
                        if answer == "y" or answer == "Y":
                            if current_barrel not in self.playercard.lots:
                                print("На вашей карточке нет такого числа! Вы проиграли")
                                print("Бот выиграл")
                                return -1
                            break
                        elif answer == "n" or answer == "N":
                            if current_barrel in self.playercard.lots:
                                print("На вашей карточке есть такое число! Вы проиграли")
                                print("Бот выиграл")
                                return -1
                            break
                        else:
                            print("Неправильный ответ.")
                    self.bag.mark_next()
            else:
                print("Ошибка игры. Неожиданный исход")
                break
