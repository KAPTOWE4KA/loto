import random


class Barrel:
    def __init__(self, num):
        self.number = num
        self.marked = False

    def __int__(self):
        return self.number

class LotoBag:
    def __init__(self):
        self.unmarked_barrels = [i+1 for i in range(0, 90)]
        self.marked_barrels = []
        random.shuffle(self.unmarked_barrels)

    def get_next(self):
        self.marked_barrels.append(self.unmarked_barrels.pop(0))
        return self.marked_barrels[-1]

    def reset(self):
        self.unmarked_barrels = [i+1 for i in range(0, 90)]
        self.marked_barrels = []
        random.shuffle(self.unmarked_barrels)



class LotoCard:
    def __init__(self, size=[3, 9, 5]):
        self.rows = []
        for rc in range(0,size[0]):
            self.rows.append([1 for i in range(0, size[2])]+[0 for i in range(0, size[1]-size[2])])
            random.shuffle(self.rows[rc])
        self.lots = [[i+1 for i in range(0, 90)][v] for v in range(0, size[0]*size[2])]
        random.shuffle(self.lots)


    def print(self, *marked_barrels: int):
        b_index = 0
        print("---"*len(self.rows[0]))
        lot_index = 0
        if len(marked_barrels) > 0:
            marked_nums = [b for b in marked_barrels]
        for r in self.rows:
            line = ""
            for cell in r:
                if cell == 1:
                    if self.lots[lot_index] in marked_nums:
                        line += " X "
                    else:
                        if self.lots[lot_index] < 10:
                            line += " "+self.lots[lot_index].__str__()+" "
                        else:
                            line += self.lots[lot_index].__str__() + " "
                    lot_index += 1
                else:
                    line += "   "
            print(line)
        print("---" * len(self.rows[0]))


class LotoGameVSBot:
    def __init__(self, cardsize=[3, 9, 5]):
        #3 - rows, 9 - row length, 5 - nums in row
        self.bag = LotoBag()
        self.playercard = LotoCard()
        self.botcard = LotoCard()
        self.playername = ""
        self.is_game_ended = False

    def start(self):
        self.playername = input("Введите своё имя: ")
        while not self.is_game_ended:
            current_barrel = self.bag.get_next()
            print("Новый бочонок: "+current_barrel.__str__(), end=" (")
            print("осталось "+str(len(self.bag.unmarked_barrels))+")")
            #new barrel printing here

            ###
            #cards printing here
            self.playercard.print(self.bag.marked_barrels)
            self.botcard.print(self.bag.marked_barrels)
            ###
            answer = input("Зачеркнуть число? y/n\n")
            if answer == "y" or answer == "Y":
                print("Да")
            elif answer == "n" or answer == "N":
                print("Нет")
            else:
                print("Неправильный ответ")


