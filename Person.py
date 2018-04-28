from weapon_and_spells import Weapon
from weapon_and_spells import Spell

class Person():
    def __init__(self, health, mana, spell, weapon):
        assert type(health) is int
        assert type(mana) is int
        self.health = health
        self.mana = mana
        self.max_health = health
        self.spell = None
        self.weapon = None

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def get_mana(self):
        if self.mana >= 0:
            return self.mana
        return 0

    def get_health(self):
        if self.is_alive():
            return self.health
        return 0

    def can_cast(self):
        if self.spell != None and self.mana > self.spell.get_mana_cost():
            return True
        return False

    def used_mana_to_cast_spell(self):
        if self.spell != None:
            self.mana = self.mana - self.spell.mana_cost
            return self.mana
        else:
            return self.mana

    def take_damage(self, damage):
        assert type(damage) is float or type(damage) is int, 'damage must be number'
        assert damage > 0, 'damege must positive'
        self.health -= damage

    def take_mana(self, mana_points):
        assert type(mana_points) is int, 'mana_points must be integer'
        assert mana_points > 0, 'mana must be positive'
        tmp = self.mana + mana_points
        if tmp <= self.max_mana:
            self.mana += mana_points
            return True
        elif tmp > self.max_mana:
            self.mana = self.max_mana
            return True
        return False

    def take_healing(self, healing_points):
        assert type(healing_points) is int,'healing_points is not int'
        assert healing_points > 0,'healing_points must be positive'
        tmp = self.health + healing_points
        if self.is_alive():
            if tmp <= self.max_health:
                self.health += healing_points
            elif tmp > self.max_health:
                self.health = self.max_health
            return True
        return False

    def equip(self, weapon):
        assert isinstance(weapon, Weapon), 'Weapon is not instance of weapon'
        if self.weapon is None:
            self.weapon = weapon
        if self.weapon.get_damage() < weapon.get_damage():
            self.weapon = weapon
        return True

    def learn(self, spell):
        assert isinstance(spell, Spell), 'spell must be instace of Spell'
        if self.spell is None:
            self.spell = spell
        if self.spell.get_damage() < spell.get_damage():
            self.spell = spell
        return True