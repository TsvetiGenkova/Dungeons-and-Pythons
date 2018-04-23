class Hero(Person):
    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate=2):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.damage = 0
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

    @classmethod
    def equip(cls, weapon):
        







