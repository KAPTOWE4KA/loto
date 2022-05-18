import unittest
from loto_classes import LotoBag, LotoCard, LotoGameVSBot


class TestLotoBag(unittest.TestCase):
    def setUp(self):
        self.lotobag = LotoBag()

    def test_marking(self):
        barrell = self.lotobag.get_next()
        self.lotobag.mark_next()
        self.assertNotIn(barrell, self.lotobag.unmarked_barrels)
        self.assertIn(barrell, self.lotobag.marked_barrels)

    def test_bool_operations(self):
        temp_lotobag = LotoBag()
        self.assertTrue(self.lotobag == temp_lotobag)
        temp_lotobag.mark_next(count=50)
        self.assertTrue(self.lotobag > temp_lotobag)
        self.assertFalse(self.lotobag <= temp_lotobag)
        self.assertFalse(self.lotobag < temp_lotobag)
        self.assertTrue(self.lotobag >= temp_lotobag)


class TestLotoCard(unittest.TestCase):
    def setUp(self):
        self.lotocard = LotoCard()
        self.lotobag = LotoBag()

    def test__init__(self):
        for lot in self.lotocard.lots:
            self.assertIn(lot, self.lotobag.unmarked_barrels)

    def test_is_completed(self):
        self.lotobag.mark_next(count=90)
        self.assertTrue(self.lotocard.is_completed(self.lotobag.marked_barrels))

    def test_str(self):
        self.assertIsInstance(self.lotocard.__str__(), str)

    def test_bool_operations(self):
        temp_lotocard = LotoCard(size=[3, 12, 10])
        self.assertTrue(self.lotocard != temp_lotocard)
        self.assertTrue(self.lotocard < temp_lotocard)
        self.assertFalse(self.lotocard >= temp_lotocard)
        self.assertFalse(self.lotocard > temp_lotocard)
        self.assertTrue(self.lotocard <= temp_lotocard)


class TestLotoVSGame(unittest.TestCase):
    def setUp(self):
        self.game = LotoGameVSBot(players=[])

    def test_exception(self):
        self.assertEqual(self.game.start(muted=True), -1)
        self.game = LotoGameVSBot(players=["bot"])
        self.assertEqual(self.game.start(muted=True), -1)

    def test_str(self):
        self.assertIsInstance(self.game.__str__(), str)
        self.game = LotoGameVSBot(players=["1", "2", "bot"])
        self.assertTrue(self.game.__str__() == "Players: 1, 2, ")

    def test_bool_operations(self):
        temp_game = LotoGameVSBot(players=["1", "2"])
        self.assertTrue(self.game != temp_game)
        self.assertTrue(self.game < temp_game)
        self.assertFalse(self.game >= temp_game)
        self.assertFalse(self.game > temp_game)
        self.assertTrue(self.game <= temp_game)

    def test_newgame1bot(self):
        self.assertEqual(LotoGameVSBot.newgame1bot(), LotoGameVSBot(players=["bot", "player"]))
#test coverage маленький так как есть 114 строк в LotoGameVSBot.start(), необязательных для теста