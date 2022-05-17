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


class TestLotoVSGame(unittest.TestCase):
    def setUp(self):
        self.game = LotoGameVSBot(players=[])

    def test_exception(self):
        self.assertEqual(self.game.start(muted=True), -1)
        self.game = LotoGameVSBot(players=["bot"])
        self.assertEqual(self.game.start(muted=True), -1)


#test coverage маленький так как есть 105 строк в LotoGameVSBot.start(), необязательных для теста