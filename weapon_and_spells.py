class Weapon():
    def __init__(self, name, damage):
        assert type(damage) is float or type(damage) is int, 'damage must be number'
        self.name = name
        self.damage = damage

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def __str__(self):
        return f' Weapon {self.name} damage = {self.damage}'


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

    def __str__(self):
        return f'Spell {self.name} damage = {self.damage} mana_cost = {self.mana_cost} range = {self.cast_range}'