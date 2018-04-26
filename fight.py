from hero import Hero
from enemy import Enemy
from utils import Move
from utils import check_for_enemy


class Fight(Hero, Enemy, Move):
    def __init__(self, hero, enemy, enemy_coords, dun):
        assert isinstance(hero, Hero), 'Hero must be instance of Hero class.'
        assert isinstance(
            enemy, Enemy), 'Enemy must be instance of Enemy class.'
        assert type(enemy_coords) is tuple, 'enemy cords must be tuple'
        assert type(dun) is list, 'dungion must be list of lists'
        self.hero = hero
        self.enemy = enemy
        self.dungeon = dun
        self.enemy_coords = enemy_coords
        self.hero_coord = (0, 0)

    def check_enemy(self, ran):
        for x, value in enumerate(self.dungeon):
            for y, y_value in enumerate(value):
                if y_value == 'H':
                    a = x
                    b = y
        self.hero_coord = (a, b)
        return check_for_enemy(self.dungeon, self.hero_coord[0], self.hero_coord[1], ran)

    def distance(self):
        return (self.hero_coord[0] - self.enemy_coords[0], self.hero_coord[1] - self.enemy_coords[1])

    def move_enemy(self):
        if self.distance()[0] == 0:
            if self.distance()[1] < 0:
                # move left
                Fight.move(
                    self.dungeon, self.enemy_coords[0], self.enemy_coords[1], "left")
                print(f"The enemy has moved one square to the left in order to get to the hero. This is his move.")
            else:
                # move right
                Fight.move(instance, self.dungeon,
                           self.enemy_coords[0], self.enemy_coords[1], "right")
                print(f"The enemy has moved one square to the right in order to get to the hero. This is his move.")
        elif self.distance()[1] == 0:
            if self.distance()[0] < 0:
                # move up
                Fight.move(instance, self.dungeon,
                           self.enemy_coords[0], self.enemy_coords[1], "up")
                print(f"The enemy has moved one square up in order to get to the hero. This is his move.")
            else:
                # move down
                Fight.move(instance, self.dungeon,
                           self.enemy_coords[0], self.enemy_coords[1], "down")
                print(f"The enemy has moved one square down in order to get to the hero. This is his move.")

        return self.dungeon

    def hero_fight(self):
        if self.hero.spell != None and self.hero.weapon != None:
            if not self.check_enemy(1) and self.hero.can_cast():
                self.enemy.take_damage(self.hero.attack(by="spell"))
                print(f"Hero casts {self.hero.spell.name} for {self.hero.spell.damage} damage. Enemy health is: {self.enemy.health}")
            elif not self.check_enemy(1) and not self.hero.can_cast():
                print(
                    "Noooooo. Your hero can\'t casts a spell. Looks like he is doomed!")
            elif self.check_enemy(1):
                if self.hero.spell.damage < self.hero.weapon.damage:
                    self.enemy.take_damage(self.hero.attack(by="weapon"))
                    print(f"Hero hits with {self.hero.weapon.name} for {self.hero.weapon.damage} damage. Enemy health is: {self.enemy.health}")
                elif not self.hero.can_cast():
                    self.enemy.take_damage(self.hero.attack(by="weapon"))
                    print(f"Hero hits with {self.hero.weapon.name} for {self.hero.weapon.damage} damage. Enemy health is: {self.enemy.health}")
                elif self.hero.spell.damage > self.hero.weapon.damage and self.hero.can_cast():
                    self.enemy.take_damage(self.hero.attack(by="spell"))
                    print(f"Hero casts {self.hero.spell.name} for {self.hero.spell.damage} damage. Enemy health is: {self.enemy.health}")
        elif self.hero.spell == None and self.hero.weapon != None:
            self.enemy.take_damage(self.hero.attack(by="weapon"))
            print(f"Hero hits with {self.hero.weapon.name} for {self.hero.weapon.damage} damage. Enemy health is: {self.enemy.health}")
        elif self.hero.spell != None and self.hero.weapon == None and self.hero.can_cast():
            self.enemy.take_damage(self.hero.attack(by="spell"))
            print(f"Hero casts {self.hero.spell.name} for {self.hero.spell.damage} damage. Enemy health is: {self.enemy.health}")
        elif self.hero.spell != None and self.hero.weapon == None and not self.hero.can_cast():
            print("Noooooo. Your hero don\'t have a weapon. Looks like he is doomed!")
        else:
            print(
                "Noooooo. Your hero don\'t have weapon and can\'t casts a spell. Looks like he is doomed!")

    def enemy_fight(self):
        if not self.check_enemy(1):
            if self.enemy.spell == None:
                self.move_enemy()
            elif self.enemy.spell != None and not self.check_enemy(self.enemy.spell.cast_range):
                self.move_enemy()
            elif self.enemy.spell != None and self.check_enemy(self.enemy.spell.cast_range) and not self.enemy.can_cast():
                self.move_enemy()
            elif self.enemy.spell != None and self.check_enemy(self.enemy.spell.cast_range) and self.enemy.can_cast():
                self.hero.take_damage(self.enemy.attack(by="spell"))
                print(f"Enemy hits hero with {self.enemy.spell.name} for {self.enemy.spell.damage} dmg. Hero health is {self.hero.health}.")

        elif self.check_enemy(1):
            if self.enemy.spell != None and self.enemy.weapon != None:
                spell_damage = self.enemy.spell.damage
                weapon_damage = self.enemy.weapon.damage
                enemy_damage = self.enemy.damage

                if not self.enemy.can_cast():
                    ls = [weapon_damage, enemy_damage]
                else:
                    ls = [spell_damage, weapon_damage, enemy_damage]
                ls.sort(reverse=True)

                if ls[0] == self.enemy.spell.damage:
                    self.hero.take_damage(self.enemy.attack(by="spell"))
                    print(f"Enemy hits hero with {self.enemy.spell.name} for {self.enemy.spell.damage} dmg. Hero health is {self.hero.health}.")
                elif ls[0] == self.enemy.weapon.damage:
                    self.hero.take_damage(self.enemy.attack(by="weapon"))
                    print(f"Enemy hits hero for {self.enemy.weapon.damage} dmg. Hero health is {self.hero.health}.")
                elif ls[0] == self.enemy.damage:
                    self.hero.take_damage(self.enemy.damage)
                    print(f"Enemy hits hero for {self.enemy.damage} dmg. Hero health is {self.hero.health}.")

            elif self.enemy.spell == None and self.enemy.weapon != None:
                if self.enemy.weapon.damage > self.enemy.damage:
                    self.hero.take_damage(self.enemy.attack(by="weapon"))
                    print(f"Enemy hits hero for {self.enemy.weapon.damage} dmg. Hero health is {self.hero.health}.")
                else:
                    self.hero.take_damage(self.enemy.damage)
                    print(f"Enemy hits hero for {self.enemy.damage} dmg. Hero health is {self.hero.health}.")

            elif self.enemy.spell == None and self.enemy.weapon == None:
                self.hero.take_damage(self.enemy.damage)
                print(f"Enemy hits hero for {self.enemy.damage} dmg. Hero health is {self.hero.health}.")

    def start_fight(self):
        print(f"A fight is started between our {self.hero} and {self.enemy}")
        while self.hero.is_alive() == True and self.enemy.is_alive() == True:
            self.hero_fight()
            self.enemy_fight()
            self.hero.take_mana(self.hero.mana_regeneration_rate)
            print('DSADAS')
        if self.hero.is_alive() == False:
            print("Your hero is dead!")
        elif self.enemy.is_alive() == False:
            print("The enemy is dead!")
