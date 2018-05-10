from hero import Hero
from enemy import Enemy
from utils import Move
from utils import check_for_stuff


class Fight(Hero, Enemy):
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
        self.hero_coord = self.find_hero()

    def print_dungeon(self):
        for i in self.dungeon:
            print(''.join(i))

    def find_hero(self):
        for x, value in enumerate(self.dungeon):
            for y, y_value in enumerate(value):
                if y_value == 'H':
                    a = x
                    b = y
        self.hero_coord = (a, b)
        return self.hero_coord

    def distance_to_enemy(self):
        return (self.hero_coord[0] - self.enemy_coords[0], self.hero_coord[1] - self.enemy_coords[1])

    def distance_to_hero(self):
        return (self.enemy_coords[0] - self.hero_coord[0], self.enemy_coords[1] - self.hero_coord[1])

    def move_towards(self, who):
        m = Move(who)
        if isinstance(who, Enemy):
            x_coord = self.enemy_coords[0]
            y_coord = self.enemy_coords[1]
            distance = self.distance_to_enemy()
        elif isinstance(who, Hero):
            x_coord = self.hero_coord[0]
            y_coord = self.hero_coord[1]
            distance = self.distance_to_hero()
        
        if distance[0] == 0:
            if distance[1] < 0:
                tmp = m.move(self.dungeon, x_coord, y_coord, "left")
                x_coord = tmp[0]
                y_coord = tmp[1]
                self.dungeon = tmp[2]               
            else:
                tmp = m.move(self.dungeon, x_coord, y_coord, "right")
                x_coord = tmp[0]
                y_coord = tmp[1]
                self.dungeon = tmp[2]
        elif distance[1] == 0:
            if distance[0] < 0:
                tmp = m.move(self.dungeon, x_coord, y_coord, "up")
                x_coord = tmp[0]
                y_coord = tmp[1]
                self.dungeon = tmp[2]
            else:
                tmp = m.move(self.dungeon, x_coord, y_coord, "down")
                x_coord = tmp[0]
                y_coord = tmp[1]
                self.dungeon = tmp[2]

        if isinstance(who, Enemy):
            self.enemy_coords = (tmp[0], tmp[1])
            print(f"The enemy has moved one square in order to get to the hero. This is his move.")
        elif isinstance(who, Hero):
            self.hero_coord = (tmp[0], tmp[1])
            print(f"The hero has moved one square in order to get to the enemy. This is his move.")

        self.print_dungeon()
        return self.dungeon

    def hero_fight(self):
        if not check_for_stuff(self.dungeon, self.hero_coord[0], self.hero_coord[1], "E", 1):
            if self.hero.can_cast():
                self.enemy.take_damage(self.hero.attack(by="spell"))
                print(f"Hero casts \"{self.hero.spell.name}\" for {self.hero.spell.damage} damage. Enemy health is: {self.enemy.get_health()}")
            elif not self.hero.can_cast():
                self.move_towards(self.hero)

        elif check_for_stuff(self.dungeon, self.hero_coord[0], self.hero_coord[1], "E", 1):
            if self.hero.can_cast() and self.hero.weapon != None:
                if self.hero.spell.get_damage() < self.hero.weapon.get_damage():
                    self.enemy.take_damage(self.hero.attack(by="weapon"))
                    print(f"Hero hits with \"{self.hero.weapon.name}\" for {self.hero.weapon.damage} damage. Enemy health is: {self.enemy.get_health()}")
                elif self.hero.spell.get_damage() > self.hero.weapon.get_damage():
                    self.enemy.take_damage(self.hero.attack(by="spell"))
                    print(f"Hero casts \"{self.hero.spell.name}\" for {self.hero.spell.damage} damage. Enemy health is: {self.enemy.get_health()}")      
            elif not self.hero.can_cast() and self.hero.weapon != None:
                self.enemy.take_damage(self.hero.attack(by="weapon"))
                print(f"Hero hits with \"{self.hero.weapon.name}\" for {self.hero.weapon.damage} damage. Enemy health is: {self.enemy.get_health()}")        
            elif self.hero.can_cast() and self.hero.weapon == None:
                self.enemy.take_damage(self.hero.attack(by="spell"))
                print(f"Hero casts \"{self.hero.spell.name}\" for {self.hero.spell.damage} damage. Enemy health is: {self.enemy.get_health()}")        

    def enemy_fight(self):
        if not check_for_stuff(self.dungeon, self.enemy_coords[0], self.enemy_coords[1], "H", 1):
            if not self.enemy.can_cast():
                self.move_towards(self.enemy)
            elif self.enemy.can_cast() and not check_for_stuff(self.dungeon, self.enemy_coords[0], self.enemy_coords[1], "H", self.enemy.spell.cast_range):
                self.move_towards(self.enemy)
            elif self.enemy.can_cast() and check_for_stuff(self.dungeon, self.enemy_coords[0], self.enemy_coords[1], "H", self.enemy.spell.cast_range) and self.enemy.can_cast():
                self.hero.take_damage(self.enemy.attack(by="spell"))
                print(f"Enemy hits hero with \"{self.enemy.spell.name}\" for {self.enemy.spell.damage} dmg. Hero health is: {self.hero.get_health()}.")

        elif check_for_stuff(self.dungeon, self.enemy_coords[0], self.enemy_coords[1], "H", 1):          
            if not self.enemy.can_cast():
                if self.enemy.weapon != None:
                    ls = [self.enemy.weapon.damage, self.enemy.damage]
                else:
                    ls = [self.enemy.damage]
            else:
                if self.enemy.weapon != None:
                    ls = [self.enemy.spell.damage, self.enemy.weapon.damage, self.enemy.damage]
                else:
                    ls = [self.enemy.spell.damage, self.enemy.damage]
            ls.sort(reverse=True)

            if ls[0] == self.enemy.damage:
                self.hero.take_damage(self.enemy.damage)
                print(f"Enemy hits hero for {self.enemy.damage} dmg. Hero health is: {self.hero.get_health()}.")         
            elif self.enemy.weapon != None and ls[0] == self.enemy.weapon.damage:
                self.hero.take_damage(self.enemy.attack(by="weapon"))
                print(f"Enemy hits hero with \"{self.enemy.weapon.name}\" for {self.enemy.weapon.damage} dmg. Hero health is: {self.hero.get_health()}.")
            elif ls[0] == self.enemy.spell.damage:
                self.hero.take_damage(self.enemy.attack(by="spell"))
                print(f"Enemy hits hero with \"{self.enemy.spell.name}\" for {self.enemy.spell.damage} dmg. Hero health is: {self.hero.get_health()}.")

    def start_fight(self):
        print(f"A fight is started between our {self.hero} and {self.enemy}")
        while self.hero.is_alive() != False or self.enemy.is_alive() != False:
            self.hero_fight()
            if self.enemy.is_alive() == False:
                self.dungeon[self.enemy_coords[0]][self.enemy_coords[1]] = '.'
                self.print_dungeon()
                print("The enemy is dead!")
                break
            self.enemy_fight()
            if self.hero.is_alive() == False:
                self.dungeon[self.hero_coord[0]][self.hero_coord[1]] = '.'
                self.print_dungeon()
                print("Your hero is dead!")
                break
            self.hero.take_mana(self.hero.mana_regeneration_rate)