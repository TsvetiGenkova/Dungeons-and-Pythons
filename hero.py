from weapon_and_spells import Weapon
from weapon_and_spells import Spell

class Hero():
    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate=2):
        assert type(health) is int
        assert type(mana) is int
        assert type(mana_regeneration_rate) is int

        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def known_as(self):
        return f"{self.name} the {self.title}"

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health <= 0:
            return 0
        return self.health

    def take_mana(self, mana_points):
        tmp = self.mana + mana_points
        if tmp >= self.max_mana:
            return self.max_mana
        return self.mana

    def equip(self, weapon):
        if self.weapon != None:
            if self.weapon.damage <= weapon.get_damage():
                self.weapon = weapon
        else:
            self.weapon = weapon

    def used_mana_to_cast_spell(self):
        if self.spell != None:
            self.mana = self.mana - self.spell.mana_cost
            return self.mana
        else:
            return self.mana

    def can_cast(self):
        if self.mana > self.spell.mana_cost:
            return True
        return False

    def learn(self, spell):
        if self.spell != None:
            if self.spell.damage <= spell.get_damage():
                self.spell = spell
        else:
            self.spell = spell

    def attack(self, by):
        if by == "weapon":
            if self.weapon != None:
                damage = self.weapon.damage
            else:
                damage = 0
                print(f"Your hero currently doesn\'t have any weapons.")
            return damage
        elif by == "spell":
            if self.spell != None:
                if self.can_cast():
                    damage = self.spell.damage
                    self.mana = self.used_mana_to_cast_spell()
                else:
                    damage = 0
                    print(f"The hero can\'t cast {self.spell.name} spell.")
            else:
                damage = 0
                print(f"Your hero currently doesn\'t know any spells.")

            return damage
            
    def sortt(self):
        spell_damage = self.spell.damage
        weapon_damage = self.weapon.damage
        enemy_damage = 22

        ls = [spell_damage, weapon_damage, enemy_damage]
        ls.sort(reverse=True)
        print(ls)



h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w1 = Weapon(name="The Axe of Destiny", damage=80)
s1 = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
h.equip(w1)
h.learn(s1)

print(h.sortt())