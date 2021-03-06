import datetime
import random


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

    def mark_next(self, count=1):
        for i in range(0, count):
            self.marked_barrels.append(self.unmarked_barrels.pop(0))

    def __str__(self):
        line = ""
        for s in self.unmarked_barrels:
            line += s+' '
        for s in self.marked_barrels:
            line += s+' '
        return line

    def __eq__(self, other):
        return sorted(self.unmarked_barrels) == sorted(other.unmarked_barrels)

    def __ne__(self, other):
        return sorted(self.unmarked_barrels) != sorted(other.unmarked_barrels)

    def __gt__(self, other):
        return len(self.unmarked_barrels) > len(other.unmarked_barrels)

    def __lt__(self, other):
        return len(self.unmarked_barrels) < len(other.unmarked_barrels)

    def __ge__(self, other):
        return len(self.unmarked_barrels) >= len(other.unmarked_barrels)

    def __le__(self, other):
        return len(self.unmarked_barrels) <= len(other.unmarked_barrels)

    def __len__(self):
        return len(self.unmarked_barrels)


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

    def __str__(self):
        line = ""
        for s in sorted(self.lots):
            line += str(s)+' '
        return line

    def __eq__(self, other):
        return sorted(self.lots) == sorted(other.lots)

    def __ne__(self, other):
        return sorted(self.lots) != sorted(other.lots)

    def __gt__(self, other):
        return len(self.lots) > len(other.lots)

    def __lt__(self, other):
        return len(self.lots) < len(other.lots)

    def __ge__(self, other):
        return len(self.lots) >= len(other.lots)

    def __le__(self, other):
        return len(self.lots) <= len(other.lots)


class LotoGameVSBot:
    def __str__(self):
        line = "Players: "
        for p in self.playernames:
            line += p+", "
        return line

    def __eq__(self, other):
        return sorted(self.playernames) == sorted(other.playernames)

    def __ne__(self, other):
        return sorted(self.playernames) != sorted(other.playernames)

    def __gt__(self, other):
        return len(self.playernames) > len(other.playernames)

    def __lt__(self, other):
        return len(self.playernames) < len(other.playernames)

    def __ge__(self, other):
        return len(self.playernames) >= len(other.playernames)

    def __le__(self, other):
        return len(self.playernames) <= len(other.playernames)

    def __init__(self, players=["bot", "player"], # "bot" = Bot, "BoT" != bot
                 cardsize=[3, 9, 5]):
        change_seed()
        # 3 - rows, 9 - row length, 5 - nums in row
        self.bag = LotoBag()
        self.playercards = [LotoCard() for player in players if player != "bot"]
        change_seed()
        self.botcards = [LotoCard() for player in players if player == "bot"]
        self.playernames = [p for p in players if p != "bot"]

    @staticmethod
    def newgame1bot(pname="player"):
        return LotoGameVSBot(players=["bot", pname])

    def start(self, muted=False):
        if len(self.playercards) == 0:
            if not muted:
                print("?? ???????? ???????????? ???????? ?????????????? 1 ??????????")
            return -1
        elif (len(self.botcards)+len(self.playercards)) < 2:
            if not muted:
                print("?? ???????? ???????????? ???????? ?????????????? 1 ?????????? ?? ???? 0 ???? 2 ??????????")
            return -1
        while True:
            current_barrel = self.bag.get_next()
            if current_barrel != 0:
                # new barrel printing here
                print("?????????? ??????????????: " + current_barrel.__str__(), end=" (")
                print("???????????????? " + str(len(self.bag.unmarked_barrels)) + ")")
                ###
                # cards printing here
                for botcard in self.botcards:
                    print("???????????????? ????????: ")
                    botcard.print(self.bag.marked_barrels)
                for player_i in range(0,len(self.playercards)):
                    print(f"???????????????? ???????????? {self.playernames[player_i]}:")
                    self.playercards[player_i].print(self.bag.marked_barrels)
                # card completing check
                is_draw = True
                for botcard in self.botcards:
                    if botcard.is_completed(self.bag.marked_barrels):
                        is_draw = True
                    else:
                        is_draw = False
                        break
                if is_draw:
                    for playercard in self.playercards:
                        if playercard.is_completed(self.bag.marked_barrels):
                            is_draw = True
                        else:
                            is_draw = False
                        break
                if is_draw:
                    print("??????????")
                    return 0

                winners = []
                losers = []

                for player_i in range(0, len(self.playercards)):
                    if self.playercards[player_i].is_completed(self.bag.marked_barrels):
                        winners.append(self.playernames[player_i])

                for botcard in self.botcards:
                    if botcard.is_completed(self.bag.marked_barrels):
                        winners.append("bot")

                if len(winners) > 0:
                    if "bot" not in winners:
                        print("?????????????? ??????????:" if len(winners) == 1 else "???????????????? ????????????:")
                        for wn in winners:
                            print(wn, end=' ')
                        return 1
                    else:
                        print("??????????????:" if len(winners) == 1 else "????????????????:")
                        for wn in winners:
                            print(wn, end=' ')
                        return 1
                else:
                    ###
                    for player_i in range(0, len(self.playernames)):
                        if player_i >= len(self.playernames):
                            break
                        print(f"??????????: {self.playernames[player_i]}")
                        while True:
                            answer = input(f"???????????????????? ?????????? {current_barrel}? y/n\n")
                            if answer == "y" or answer == "Y":
                                if current_barrel not in self.playercards[player_i].lots:
                                    print(f"???? ?????????? ???????????????? ?????? ???????????? ??????????! ?????????? {self.playernames[player_i]} ???????????????? ")
                                    if len(self.playercards) > 1:
                                        print(f"?????????? {self.playernames[player_i]} ????????????????")
                                        self.playercards.pop(player_i)
                                        self.playernames.pop(player_i)
                                        player_i = player_i - 1
                                        break
                                    else:
                                        print("?????? ??????????????")
                                        return -1
                                else:
                                    if player_i==len(self.playernames):
                                        player_i = 0
                                    else:
                                        player_i += 1
                                break
                            elif answer == "n" or answer == "N":
                                if current_barrel in self.playercards[player_i].lots:
                                    print(
                                        f"???? ?????????? ???????????????? ???????? ?????????? ??????????! ?????????? {self.playernames[player_i]} ???????????????? ")
                                    if len(self.playercards) > 1:
                                        print(f"?????????? {self.playernames[player_i]} ????????????????")
                                        self.playercards.pop(player_i)
                                        self.playernames.pop(player_i)
                                        player_i = player_i - 1
                                        break
                                    else:
                                        print("?????? ??????????????")
                                        return -1
                                else:
                                    if player_i == len(self.playernames):
                                        player_i = 0
                                    else:
                                        player_i += 1
                                break
                            else:
                                print("???????????????????????? ??????????.")

                    self.bag.mark_next()
            else:
                print("???????????? ????????. ?????????????????????? ??????????")
                break
