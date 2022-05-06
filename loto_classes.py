import random


class LotoException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"LotoException, {self.message}"
        else:
            return "LotoException has been raised"


class Barrell:
    def __init__(self, new_number):
        self.marked = False
        if isinstance(new_number, int):
            self.number = new_number
        else:
            raise TypeError("Barrel number is not class<int>")

    def set_number(self, new_number):
        if isinstance(new_number, int):
            self.number = new_number
        else:
            raise TypeError("Barrel number is not class<int>")

    def mark(self):
        if self.marked:
            raise LotoException("Barrel already marked")
        else:
            self.marked = True


class LotoBag:
    def __init__(self, barrel_max=90):
        self.barrel_index = 0
        self.barrel_count=barrel_max
        nums = [i+1 for i in range(0, self.barrel_count)]
        random.shuffle(nums)
        self.barrels = [Barrell(i) for i in nums]
        #print([b.number for b in self.barrels])

    def get_next_barrel(self):
        self.barrel_index += 1
        self.barrels[self.barrel_index].mark()
        return self.barrels[self.barrel_index - 1].number

    def get_marked_barrels(self):
        return [b.number for b in self.barrels if b.marked]

    def shuffle_remaining_barrels(self):
        marked_barrels = [self.barrels[i] for i in range(0, self.barrel_index)]
        unmarked_barrels = [self.barrels[i] for i in range(self.barrel_index, len(self.barrels))]
        random.shuffle(unmarked_barrels)
        self.barrels = marked_barrels + unmarked_barrels

    def debug_mark_many(self, start=1, end=10):
        for i in range(start-1, end+1):
            self.barrels[i].mark()

    def debug_print_all(self):
        for b in self.barrels:
            if isinstance(b, Barrell):
                print(b.number, end=", ")
            else:
                raise LotoException("Object type expected: class<Barrel>.  Found: "+str(type(b)))
        print('\n')

    def debug_print_remains(self):
        for b in self.barrels:
            if isinstance(b, Barrell):
                if b.marked:
                    print("XX" if b.number > 9 else "X", end=", ")
                else:
                    print(b.number, end=", ")
            else:
                raise LotoException("Object type expected: class<Barrel>.  Found: "+str(type(b)))
        print('\n')


class LotoCard:
    def __init__(self, lbag: LotoBag, playername, rl=9, rc=3, fc=5):
        self.rows_length = rl
        self.player = playername
        self.rows_count = rc
        self.free_cells_count = fc
        self.lots = [[b for b in lbag.barrels][v] for v in range(0, self.free_cells_count*self.rows_count)]
        self.rows = []
        for c in range(0, self.rows_count):
            self.rows.append(self.lots[c:self.free_cells_count+c]+[0 for i in range(0, self.rows_length-self.free_cells_count)])
            random.shuffle(self.rows[c])
        #print(self.lots)
        #print(self.rows)

    def print(self):
        print("Карточка игрока: "+self.player)
        print("---"*self.rows_length)
        for row in self.rows:
            line = ""
            for cell in row:
                if isinstance(cell, Barrell):
                    if cell.marked:
                        line += " X"
                    else:
                        cell = cell.number
                        if cell < 10:
                            line += " "+str(cell)
                        else:
                            line += str(cell)
                else:
                    line += "  "
                line += " "
            print(line)
        print("---" * self.rows_length)


class LotoPlayer:
    def __init__(self, name, c_count=1):
        self.cards_count = c_count
        self.score = 0
        self.name = name


#class LotoGame:
