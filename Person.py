class Person():
    def __init__(self, health, mana):
        assert type(health) is int
        assert type(mana) is int
        self.health = health
        self.mana = mana
        self.max_health = health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def get_mana(self):
        if mana >= 0:
            return self.mana
        return 0

    def get_health(self):
        if self.is_alive():
            return self.health
        return 0

    def take_healing(self, healing_points):
        if self.is_alive() and (self.health + healing_points) <= self.max_health:
            self.health += healing_points
            return True

        return False
