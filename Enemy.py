

from Person import Person

from weapon_and_spells import Weapon
from weapon_and_spells import Spell


class Enemy(Person):

    def __init__(self, health, mana, damage):
        assert type(health) is int, 'health is not int'
        assert type(mana) is int, 'mana is not int'
        assert type(damage) is int, 'damage is not int'

        super().__init__(health, mana)
        self.damage = damage
        self.max_mana = mana
        self.spell = None
        self.weapon = None

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, by=None):
        if by == None:
            return self.damage
        assert type(by) is str, 'by is not string'
        if by == "spell" and self.spell != None:
            return spell.damage()
        if by == 'weapon' and self.weapon != None:
            return weapon.damage()
        raise ValueError

    def take_mana(self, mana):
        if (self.mana + mana) <= self.max_mana:
            self.mana += mana
            return True

        return False

    def get_mana(self):
        if self.mana >= 0:
            return mana
        return 0

    def can_cast(self):
        if self.spell != True:
            return True
        return False

    def equip(self, weapon):
        assert isinstance(
            weapon, Weapon) is True, 'Weapon is not instance of weapon'
        if self.weapon == None:
            self.weapon = weapon

        if self.weapon.get_damage() < weapon.get_damage():
            self.weapon = weapon

    def spell(self, spell):
        assert isinstance(spell, Spell), 'spell must be instace of Spell'
        if self.spell == None:
            self.spell = spell
        if self.spell.get_damage() < spell.get_damage():
            self.spell = spell
