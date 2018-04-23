

from Person import Person


class Enemy(Person):

    def __init__(self, health, mana, damage):
        assert type(health) is int
        assert type(mana) is int
        assert type(damage) is int

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
