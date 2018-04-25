from hero import Hero
from enemy import Enemy

class Fight(Hero, Enemy):
    def __init__(self, hero, enemy, dun):
        assert isinstance(hero, Hero), 'Hero must be instance of Hero class.'
        assert isinstance(enemy, Enemy), 'Enemy must be instance of Enemy class.'
        self.hero = hero
        self.enemy = enemy
        self.dungeon = dun
        self.hero_coord = (0,0)

    def check_enemy(self, ran):
        for x, y in enumerate(self.dungeon):
            for y_value in value:
                if y_value == 'H':
                    a = index
                    b = y_value
        self.hero_coord = (a, b)
        for i in range(0, ran):
                if (self.dungeon[a + i][b] == "E" or
                        self.dungeon_map[a - i][b] == "E" or
                        self.dungeon_map[a][b + i] == "E" or
                        self.dungeon_map[a][b - i] == "E"):
                    return True
        return False

    def distance(self):
        pass

    def hero_move(self):
        if self.hero.spell != None and self.hero.weapon != None:
            if not self.check_enemy(1) and self.hero.can_cast():
                self.enemy.take_damage(self.hero.attack(by="spell"))
                print(f"Hero casts {self.hero.spell.name} for {self.hero.spell.damage} damage. Enemy health is: {self.enemy.health}")
            elif not self.check_enemy(1) and not self.hero.can_cast():
                print("Noooooo. Your hero can\'t casts a spell. Looks like he is doomed!")
            elif self.check_enemy(1):
                if self.hero.spell.damage < self.hero.weapon.damage: 
                    self.enemy.take_damage(self.hero.attack(by="weapon"))
                    print(f"Hero hits with {self.hero.weapon.name} for {self.hero.weapon.damage} damage. Enemy health is: {self.enemy.health}")
                elif not self.hero.can_cast():
                    self.enemy.take_damage(self.hero.attack(by="weapon"))
                    print(f"Hero hits with {self.hero.weapon.name} for {self.hero.weapon.damage} damage. Enemy health is: {self.enemy.health}")
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
            print("Noooooo. Your hero don\'t have weapon and can\'t casts a spell. Looks like he is doomed!")

    def enemy_move(self):
        if not self.check_enemy(1):
            if self.enemy.spell == None:
                #FIND HERO MOOVE TO HIM
                pass
            elif self.enemy.spell != None and not self.check_enemy(self.enemy.spell.cast_range):
                #FIND HERO MOOVE TO HIM
                pass
            elif self.enemy.spell != None and self.check_enemy(self.enemy.spell.cast_range):
                self.hero.take_damage(self.enemy.attack(by="spell"))

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
        while self.hero.health == 0 or self.enemy.health == 0:
            self.hero_move()
            self.enemy_move()
            self.hero.take_mana(self.hero.mana_regeneration_rate)

        if self.hero.health == 0:
            print("Your hero is dead!")
        else:
            print("The enemy is dead!")