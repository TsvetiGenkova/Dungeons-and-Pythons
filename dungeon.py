import os
from fight import Fight
from hero import Hero
from enemy import Enemy
from random import randint
from weapon_and_spells import Spell
from weapon_and_spells import Weapon
from utils import Move
from utils import check_for_enemy


class Dungeon(Move):

    def __init__(self, map_file):
        assert type(map_file) is str, 'map_file must be string'
        assert os.path.isfile(map_file) is True, 'map_file is not file'
        self.map_file = map_file
        self.dungeon_map = self.load_map()
        self.spawning_cordinates = self.get_all_spawning_cordinates()
        self.hero = None
        self.enemyes = self.get_enemys()
        self.x = None
        self.y = None

    def spawn(self, hero):
        assert isinstance(hero, Hero), 'Hero must be instance of Hero class '
        for i in self.spawning_cordinates:
            if i[1] == False:
                self.x = i[0][0]
                self.y = i[0][1]
                self.dungeon_map[self.x][self.y] = 'H'
                i[1] = True
                self.hero = hero
                return True
        return False

    def get_all_spawning_cordinates(self):
        spawning_cordinates = []
        for index, value in enumerate(self.dungeon_map):
            for y_index, y_value in enumerate(value):
                if y_value == 'S':
                    spawning_cordinates.append([(index, y_index), False])
        return spawning_cordinates

    def get_enemys(self):
        enemyes = []
        for index, value in enumerate(self.dungeon_map):
            for y_index, y_value in enumerate(value):
                if y_value == 'E':
                    enemyes.append([(index, y_index), self.generate_enemy()])
        return enemyes

    def generate_enemy(self):
        return Enemy(health=55, mana=55, damage=55.0)

    def load_map(self):
        m = []
        with open(self.map_file, 'r') as f:
            for i in f.readlines():
                i = i.rstrip()
                m.append(list(i))
        return m

    def print_map(self):
        for i in self.dungeon_map:
            print(''.join(i))

    def move_hero(self, direction):
        changes = Dungeon.move(self.dungeon_map, self.x, self.y, direction)
        if changes == False:
            return False
        self.x = changes[0]
        self.y = changes[1]
        self.dungeon_map = changes[2]
        if (self.x,self.y) is self.get_all_trasure_cordinates():
            self.pick_treasure()
        return True

    def pick_treasure(self):
        t = []
        with open("loot.txt", 'r') as f:
            for i in f.readlines():
                t.append(i)
        treasure = t[randint(0, len(t) - 1)].split(",")
        if treasure[0] == "weapon":
            tmp = float(treasure[2]) if '.' in treasure[2] else float(
                treasure[2])
            tr = Weapon(name=treasure[1], damage=tmp)
            self.hero.equip(tr)
        elif treasure[0] == "spell":
            tmp = float(treasure[2]) if '.' in treasure[2] else float(
                treasure[2])
            tmp1 = float(treasure[3]) if '.' in treasure[3] else float(
                treasure[3])
            tr = Spell(name=treasure[1], damage=tmp,
                       mana_cost=tmp1, cast_range=int(treasure[4]))
            self.hero.learn(tr)
        else:
            if treasure[0] == "Mana potion":
                self.hero.take_mana(int(treasure[1]))
                tr = "Mana potion"
            elif treasure[0] == "Health potion":
                self.hero.take_healing(int(treasure[1]))
                tr = "Health potion"

        return tr

    def where_are_you(self, x, y):
        if self.dungeon_map[x][y] == "T":
            return f"Found {self.pick_treasure()}!"
        elif self.dungeon_map[x][y] == "E":
            dun = self.dungeon_map
            for i in self.enemyes:
                if i[0][0] == x and i[0][1] == y:
                    enemy_coords = i[0]
                    enemy = i[1]
                    break
            f = Fight(self.hero, enemy, enemy_coords, dun)
            f.start_fight()
        elif self.dungeon_map[x][y] == ".":
            pass
        elif self.dungeon_map[x][y] == "S":
            pass
        elif self.dungeon_map[x][y] == "G":
            print("You have cleared the dungeon!")

    def hero_attack(self, by):
        if by == "spell":
            if self.hero.spell != None:
                ran = self.hero.spell.cast_range
                if check_for_enemy(self.dungeon_map, self.x, self.y, ran):
                    enemy = Enemy(health=100, mana=100, damage=20)
                    f = Fight(self.hero, enemy)
                    start_fight()
            else:
                print(f"You can\'t attack, because you don\'t know any spells.")
        if by == "weapon":
            if self.hero.weapon != None:
                if self.check_for_enemy(self.dungeon_map, self.x, self.y, 1):
                    enemy = Enemy(health=100, mana=100, damage=20)
                if self.check_for_enemy(self.dungeon_map, self.x, self.y, 1):
                    enemy = Enemy(health=100, mana=100, damage=20.0)
                    f = Fight(self.hero, enemy)
                    start_fight()
            else:
                print(f"You can\'t attack, because you don\'t have a weapon.")

    def get_all_trasure_cordinates(self):
        trasures = []
        for index, value in enumerate(self.dungeon_map):
            for y_index, y_value in enumerate(value):
                if y_value == 'S':
                    trasures.append([(index, y_index), False])
        return trasures


d = Dungeon('map.txt')
d.spawn(Hero(name='ivan', title='ivanov', health=100,
             mana=100, mana_regeneration_rate=2))

d.move_hero('right')
d.move_hero('down')
d.move_hero('down')
d.print_map()
