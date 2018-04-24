import unittest
from hero import Hero
from weapon_and_spells import Weapon
from weapon_and_spells import Spell


class TestHero(unittest.TestCase):
    def setUp(self):
        self.h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

    def test_known_as(self):
        self.assertEqual(self.h.known_as(), "Bron the Dragonslayer")

    def test_take_damage(self):
        self.h.take_damage(20.5)
        self.assertEqual(self.h.health, 79.5)

    def test_take_mana(self):
        self.h.take_mana(20)
        self.assertEqual(self.h.mana, 100)

    def test_can_cast(self):
        s = Spell(name="s", damage=40, mana_cost=120, cast_range=2)
        self.h.learn(s)
        self.assertFalse(self.h.can_cast())
        s1 = Spell(name="s1", damage=40, mana_cost=20, cast_range=2)
        self.h.learn(s1)
        self.assertTrue(self.h.can_cast())

    def test_equip(self):
        self.assertEqual(self.h.weapon, None)
        w = Weapon(name="w", damage=20)
        self.h.equip(w)
        self.assertEqual(self.h.weapon.damage, 20)
        self.assertEqual(self.h.weapon.name, "w")
        w1 = Weapon(name="w1", damage=30)
        self.h.equip(w1)
        self.assertEqual(self.h.weapon.damage, 30)
        self.assertEqual(self.h.weapon.name, "w1")
        w2 = Weapon(name="w2", damage=10)
        self.h.equip(w2)
        self.assertEqual(self.h.weapon.damage, 30)
        self.assertEqual(self.h.weapon.name, "w1")

    def test_learn(self):
        self.assertEqual(self.h.weapon, None)
        s = Spell(name="s", damage=30, mana_cost=50, cast_range=2)
        self.h.learn(s)
        self.assertEqual(self.h.spell.damage, 30)
        self.assertEqual(self.h.spell.name, "s")
        s1 = Spell(name="s1", damage=40, mana_cost=50, cast_range=2)
        self.h.learn(s1)
        self.assertEqual(self.h.spell.damage, 40)
        self.assertEqual(self.h.spell.name, "s1")
        s2 = Spell(name="s1", damage=20, mana_cost=50, cast_range=2)
        self.h.learn(s2)
        self.assertEqual(self.h.spell.damage, 40)
        self.assertEqual(self.h.spell.name, "s1")

    def test_attack(self):       
        self.assertEqual(self.h.attack(by="weapon"), 0)
        self.assertEqual(self.h.attack(by="spell"), 0)
        w = Weapon(name="w", damage=20)
        self.h.equip(w)
        self.assertEqual(self.h.attack(by="weapon"), 20)
        s = Spell(name="s", damage=30, mana_cost=10, cast_range=2)
        self.h.learn(s)
        self.assertEqual(self.h.attack(by="spell"), 30)
        self.assertEqual(self.h.mana, 90)
        s1 = Spell(name="s1", damage=30, mana_cost=110, cast_range=2)
        self.h.learn(s1)
        self.assertEqual(self.h.attack(by="spell"), 0)
        self.assertEqual(self.h.mana, 90)

if __name__ == '__main__':
    unittest.main()