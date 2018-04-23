from weapon_and_spells import Weapon
from weapon_and_spells import Spell

class Hero(Person):
    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate=2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.damage_by_weapon = 0
        self.damage_by_spell = 0
        self.max_mana = mana


    def known_as(self):
        return f"{self.name} the {self.title}"

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health <= 0:
            return 0
        return self.health

    def take_mana(self, mana_points):
        self.mana += mana_points
        if self.mana >= self.max_mana:
            return self.max_mana
        return self.mana

    def equip(self, weapon):
        if self.damage_by_weapon <= weapon.get_damage:
            self.damage_by_weapon = weapon.get_damage

    def learn(self, spell):
        if self.damage_by_spell <= spell.get_damage:
            self.damage_by_spell = spell.get_damage


    def attack(self, method):
        if method == "weapon":
            damage = self.damage_by_weapon
        elif method == "spell":
            damage = self.damage_by_spell
        return damage

