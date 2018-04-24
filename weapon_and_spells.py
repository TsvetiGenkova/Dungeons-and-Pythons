class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_damage(self):
        return self.damage

    def get_name(self):
        return self.name




class Spell():
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self. damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __eq__(self, other):
        if self.name == other.name and self.damage == other.damage and self.mana_cost == other.mana_cost and self.cast_range == other.cast_range:
            return True
        return False

    def get_name(self):
        return self.name
            
    def get_damage(self):
        return self.damage

    def get_mana_cost(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range


        