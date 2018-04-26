

import unittest
from Person import Person


class Test(unittest.TestCase):

    def setUp(self):
        self.person = Person(health=50, mana=56)

    def test_init(self):
        self.assertRaises(AssertionError, Person, health=5, mana='5')
        self.assertRaises(AssertionError, Person, health='5', mana=5)
        self.assertRaises(AssertionError, Person, health='5', mana='5')

    def test_is_alive(self):
        self.assertTrue(self.person.is_alive())
        self.person.health = 0
        self.assertFalse(self.person.is_alive())

    def test_get_mana(self):
        self.assertEqual(56, self.person.get_mana())
        self.person.mana = 0
        self.assertEqual(0, self.person.get_mana())

    def test_get_health(self):
        self.assertEqual(50, self.person.get_health())
        self.person.health = 0
        self.assertEqual(0, self.person.get_health())

    def test_healing(self):
        self.assertFalse(self.person.take_healing(50))
        self.person.health = 23
        self.assertTrue(self.person.take_healing(27))
        self.person.health = 0
        self.assertFalse(self.person.take_healing(23))
        self.assertRaises(AssertionError,self.person.take_healing,healing_points= '5')
        self.assertRaises(AssertionError,self.person.take_healing,healing_points = -100)


if __name__ == '__main__':
    unittest.main()
