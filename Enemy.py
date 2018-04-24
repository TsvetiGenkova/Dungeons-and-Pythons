

from Person import Person

from weapon_and_spells import Weapon
from weapon_and_spells import Spell


class Enemy(Person):

    def __init__(self, health, mana, damage):
        assert type(health) is int, 'health is not int'
        assert type(mana) is int, 'mana is not int'
        assert type(damage) is float, 'damage is not float'
        assert damage > 0, 'damage must be positeve'

        super().__init__(health, mana)
        self.damage = damage
        self.max_mana = mana
        self.spell = None
        self.weapon = None

    def take_damage(self, damage):
        assert type(damage) is float, 'damage must be float'
        assert damage > 0, 'damege must positeve'
        self.health -= damage

    def attack(self, by=None):
        if by == None:
            return self.damage
        assert type(by) is str, 'by is not string'

        assert by == 'weapon' or by == 'spell', 'by= is not spell or weapon'
        if by == "spell" and isinstance(self.spell, Spell):
            if (self.mana - self.spell.get_mana_cost()) <= 0:
                raise ValueError('not enough mana')
            return self.spell.get_damage()
        if by == 'weapon' and isinstance(self.weapon, Weapon):
            return self.weapon.get_damage()

    def take_mana(self, mana):
        assert type(mana) is int, 'mana must be integer'
        assert mana > 0, 'mana must be positive'
        if (self.mana + mana) <= self.max_mana:
            self.mana += mana
            return True

        return False

    def get_mana(self):
        if self.mana >= 0:
            return mana
        return 0

    def can_cast(self):
        if self.spell is not None:
            return True
        return False

    def equip(self, weapon):
        assert isinstance(
            weapon, Weapon) is True, 'Weapon is not instance of weapon'
        if self.weapon is None:
            self.weapon = weapon

        if self.weapon.get_damage() < weapon.get_damage():
            self.weapon = weapon

    def learn(self, spell):
        assert isinstance(spell, Spell), 'spell must be instace of Spell'
        if self.spell is None:
            self.spell = spell
        if self.spell.get_damage() < spell.get_damage():
            self.spell = spell

    def can_cast(self, spell):
        assert isinstance(spell, Spell), 'spell must be instace of Spell'
        if self.spell != None and self.spell == spell:
            return True
        return False


# enemy = Enemy(health=50, mana=56, damage=50)
# enemy.learn(Spell(name='light', damage=52,
#                   mana_cost=23, cast_range=2))

# print(enemy.attack(by='spell'))
