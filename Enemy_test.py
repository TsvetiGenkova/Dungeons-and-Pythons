

import unittest
from Enemy import Enemy
from weapon_and_spells import Spell
from weapon_and_spells import Weapon


class Test(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy(health=50, mana=56, damage=50.0)
        self.enemy.learn(Spell(name='light', damage=52,
                               mana_cost=23, cast_range=2))
        self.enemy.equip(Weapon(name='ligh Axe', damage=66))

    def test_init(self):
        self.assertRaises(AssertionError, Enemy,
                          health=50.0, mana=50, damage='23')
        self.assertRaises(AssertionError, Enemy,
                          health=50.0, mana=50, damage=-23)
        self.assertRaises(AssertionError, Enemy,
                          health='50.0', mana=50, damage=23)
        self.assertRaises(AssertionError, Enemy, health=50,
                          mana='50.0', damage='23')
        self.assertRaises(AssertionError, Enemy, health='50',
                          mana='50.0', damage='23')

    def test_take_damage(self):
        self.assertRaises(AssertionError, self.enemy.take_damage, damage='5')
        self.assertRaises(AssertionError, self.enemy.take_damage, damage=-4)

    def test_attack(self):
        self.assertRaises(AssertionError, self.enemy.attack, by=55)
        self.assertEqual(52, self.enemy.attack(by='spell'))
        self.assertEqual(66, self.enemy.attack(by='weapon'))
        self.enemy.learn(Spell(name='light', damage=99,
                               mana_cost=150, cast_range=2))
        self.assertRaises(ValueError, self.enemy.attack, by='spell')

    def test_take_mana(self):
        self.assertRaises(AssertionError, self.enemy.take_mana, mana='5')
        self.assertRaises(AssertionError, self.enemy.take_mana, mana=-5)
        self.assertFalse(self.enemy.take_mana(23))
        self.enemy.mana = 15
        self.assertTrue(self.enemy.take_mana(10))


if __name__ == '__main__':
    unittest.main()
