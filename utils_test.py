from utils import Move
from utils import check_for_stuff
from hero import Hero
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.m = []
        with open('test_map.txt', 'r') as f:
            for i in f.readlines():
                i = i.rstrip()
                self.m.append(list(i))

        self.hero = Hero(name='ivan', title='Dragon Slayer', health=100,
                         mana=100, mana_regeneration_rate=2, spell=None, weapon=None)
        self.mover = Move(self.hero)

    def test_check_for_sttuff(self):
        self.assertRaises(AssertionError, check_for_stuff, '1', 1, 1, 'H', 1)
        self.assertRaises(AssertionError, check_for_stuff,
                          self.m, '1', 1, 'H', 1)
        self.assertRaises(AssertionError, check_for_stuff,
                          self.m, 1, '1', 'H', 1)
        self.assertRaises(AssertionError, check_for_stuff, self.m, 1, 1, 1, 1)
        self.assertRaises(AssertionError, check_for_stuff,
                          self.m, 1, 1, 'B', 1)
        self.assertRaises(AssertionError, check_for_stuff,
                          self.m, 1, 1, 'H', '1')

    def test_move(self):
        self.assertRaises(AssertionError, self.mover.move,
                          self.m, 3, 1, 'wrong')
        self.assertRaises(AssertionError, self.mover.move,
                          self.m, 3, '1', 'up')
        self.assertRaises(AssertionError, self.mover.move,
                          self.m, '3', 1, 'wrong')
        self.assertRaises(AssertionError, self.mover.move,
                          'self.m', 3, 1, 'wrong')

        self.assertFalse(self.mover.move(self.m,3,1,'down'))

    def test_is_safe(self):
        


if __name__ == '__main__':
    unittest.main()
