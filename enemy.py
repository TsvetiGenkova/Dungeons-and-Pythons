import random
from Person import Person
from weapon_and_spells import Weapon
from weapon_and_spells import Spell


class Enemy(Person):

    def __init__(self, health, mana, damage, spell=None, weapon=None):
        assert type(health) is int, 'health is not int'
        assert type(mana) is int, 'mana is not int'
        assert type(damage) is float or type(
            damage) is int, 'damage is not float'
        assert damage > 0, 'damage must be positeve'
        super().__init__(health, mana, spell, weapon)
        self.damage = damage
        self.max_mana = mana
        self.spell = None
        self.weapon = None

    @classmethod
    def generate_enemy(self):
        ran = randint(0, 100)
        enemy = Enemy(health=random.randint(80, 100), mana=random.randint(
            50, 80), damage=random.randint(20, 40))
        if ran > 50:
            enemy.equip(Weapon(name='Base Sword', damage=randint(40, 60)))
        else:
            enemy.learn(Spell(name='Dark Magic', damage=randint(
                40, 60), mana_cost=randint(10, 20), cast_range=2))
        return enemy

    def attack(self, by=None):
        if by == None:
            damage = self.damage
        assert type(by) is str, 'by is not string'

        assert by == 'weapon' or by == 'spell', 'by= is not spell or weapon'
        if by == "spell" and isinstance(self.spell, Spell):
            if self.can_cast():
                damage = self.spell.get_damage()
                self.mana = self.used_mana_to_cast_spell()
            else:
                damage = 0
                print(f"The enemy can\'t cast spell.")
        if by == 'weapon' and isinstance(self.weapon, Weapon):
            if self.weapon != None:
                damage = self.weapon.get_damage()
            else:
                damage = 0
                print(f"The enemy currently doesn\'t have any weapons.")
        return damage

    def __str__(self):
        return f'Enemy (health = {self.health} , mana = {self.mana}))'
