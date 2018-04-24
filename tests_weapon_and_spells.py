import unittest
from weapon_and_spells import Weapon
from weapon_and_spells import Spell

class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.w1 = Weapon(name="The Axe of Destiny", damage=20)
        self.w2 = Weapon(name="The Axe", damage=20.5)
        

    def test_raise_type_error_init(self):
        with self.assertRaises(TypeError):
            self.w3 = Weapon(name="The destroyer", damage="22.5")
            
    def test_get_damage(self):
        self.assertEqual(self.w1.get_damage(), 20)
        self.assertEqual(self.w2.get_damage(), 20.5)

    def test_get_name(self):
        self.assertEqual(self.w1.get_name(), "The Axe of Destiny")
        self.assertEqual(self.w2.get_name(), "The Axe")


class TestSpell(unittest.TestCase):
    def setUp(self):
        self.s1 = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.s2 = Spell(name="Lightning", damage=30.5, mana_cost=50.5, cast_range=2)

    def test_raise_type_error_cast_range(self):
        with self.assertRaises(TypeError):
            self.s3 = Spell(name="Lightning", damage=30.5, mana_cost=50.5, cast_range=2.3)

    def test_raise_type_error_damage(self):
        with self.assertRaises(TypeError):
            self.s3 = Spell(name="Lightning", damage="jjj", mana_cost=50.5, cast_range=2)

    def test_raise_type_error_mana_cost(self):
        with self.assertRaises(TypeError):
            self.s3 = Spell(name="Lightning", damage=50, mana_cost="ss", cast_range=2)

    def test_get_name(self):
        self.assertEqual(self.s1.get_name(), "Fireball")
        self.assertEqual(self.s2.get_name(), "Lightning")
    
    def test_get_damage(self):
        self.assertEqual(self.s1.get_damage(), 30)
        self.assertEqual(self.s2.get_damage(), 30.5)

    def test_get_mana_cost(self):
        self.assertEqual(self.s1.get_mana_cost(), 50)
        self.assertEqual(self.s2.get_mana_cost(), 50.5)

    def test_get_cast_range(self):
        self.assertEqual(self.s1.get_cast_range(), 2)


if __name__ == '__main__':
    unittest.main()