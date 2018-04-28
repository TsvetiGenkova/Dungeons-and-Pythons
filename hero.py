from weapon_and_spells import Weapon
from weapon_and_spells import Spell
from Person import Person



class Hero(Person):
    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate=2, spell=None, weapon=None):
        assert type(health) is int
        assert type(mana) is int
        assert type(mana_regeneration_rate) is int
        super().__init__(health, mana, spell, weapon)
        self.name = name
        self.title = title
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

    def get_mana_regeneration_rate(self):
        return self.mana_regeneration_rate

    def known_as(self):
        return f"{self.name} the {self.title}"

    def attack(self, by):
        assert by == 'weapon' or by == 'spell', 'by= is not spell or weapon'
        if by == 'weapon' and isinstance(self.weapon, Weapon):
            if self.weapon != None:
                damage = self.weapon.get_damage()
            else:
                damage = 0
                print(f"Your hero currently doesn\'t have any weapons.")
        elif by == "spell" and isinstance(self.spell, Spell):
            if self.can_cast():
                damage = self.spell.get_damage()
                self.mana = self.used_mana_to_cast_spell()
            else:
                damage = 0
                print(f"The hero can\'t cast spell.")

        return damage


    def __str__(self):
        return f'Hero {self.name} , {self.title}, {self.health}, {self.mana}'
