class Weapon():
    def __init__(self, name, damage):
        assert type(damage) is float, 'damage must be float'
        self.name = name
        self.damage = damage

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage


class Spell():
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self. damage = float(damage)
        self.mana_cost = mana_cost
        self.cast_range = cast_range

        if type(cast_range) is not int:
            raise TypeError("The cast range should be int!")

        if type(damage) is int or type(damage) is float:
            pass
        else:
            raise TypeError("The damage should be a number!")

        if type(mana_cost) is int or type(mana_cost) is float:
            pass
        else:
            raise TypeError("The mana cost should be a number!")

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def get_mana_cost(self):
        return self.mana_cost

    def get_cast_range(self):
        return self.cast_range
