import os

from fight import Fight
from hero import Hero
from enemy import Enemy


class Dungeon():

    def __init__(self, map_file):
        assert type(map_file) is str, 'map_file must be string'
        assert os.path.isfile(map_file) is True, 'map_file is not file'
        self.map_file = map_file
        self.dungeon_map = self.load_map()
        self.spawning_cordinates = self.get_all_spawning_cordinates()
        self.hero = None
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
        assert type(direction) is str, 'Direction must be string'
        "up", "down", "left" and "right"
        assert direction == 'up' or direction == 'down' \
            or direction == 'left' or direction == 'right',\
            'Direction must be up,down, left or right'

        if direction == 'up' and self.is_safe(self.x - 1, self.y):
            self.dungeon_map[self.x][self.y] = '.'
            self.dungeon_map[self.x - 1][self.y] = 'H'
            self.x -= 1
            return True

        elif direction == 'down' and self.is_safe(self.x + 1, self.y):
            self.dungeon_map[self.x][self.y] = '.'
            self.dungeon_map[self.x + 1][self.y] = 'H'
            self.x += 1
            return True

        elif direction == 'left' and self.is_safe(self.x, self.y - 1):
            self.dungeon_map[self.x][self.y] = '.'
            self.dungeon_map[self.x][self.y - 1] = 'H'
            self.y -= 1
            return True

        elif direction == 'right' and self.is_safe(self.x, self.y + 1):
            self.dungeon_map[self.x][self.y] = '.'
            self.dungeon_map[self.x][self.y + 1] = 'H'
            self.y += 1
            return True
        return False

    def is_safe(self, x, y):
        assert type(x) is int, 'x must be int'
        assert type(y) is int, 'y must be int'
        try:
            self.dungeon_map[x][y]
            if self.dungeon_map[x][y] == '#':
                return False
            return True
        except IndexError:
            return False

    def pick_treasure(self):
        t = []
        with open("loot.txt", 'r') as f:
            for i in f.readlines():
                t.append(i)
        treasure = t[randint(0,len(t))].split(",")

        if treasure[0] == "weapon":
            tmp = float(treasure[2]) if '.' in treasure[2] else int(treasure[2])
            tr = Weapon(name=treasure[1], damage=tmp)
            self.hero.equip(tr)
        elif treasure[0] == "spell":
            tmp = float(treasure[2]) if '.' in treasure[2] else int(treasure[2])
            tmp1 = float(treasure[3]) if '.' in treasure[3] else int(treasure[3])
            tr = Spell(name=treasure[1], damage=tmp, mana_cost=tmp1, cast_range=int(treasure[4]))
            self.hero.learn(tr)
        else:
            if treasure[0] == "Mana potion":
                self.hero.take_mana(int(treasure[1]))
                tr = "Mana potion"
            elif treasure[0] == "Health potion":
                self.hero.take_healing(int(treasure[1]))
                tr = "Health potion"

        return tr


    def where_are_you(self):
        if self.dungeon_map[self.x][self.y] == "T":
            return f"Found {self.pick_treasure()}!"
        elif self.dungeon_map[self.x][self.y] == "E":
            enemy = Enemy(health=100, mana=100, damage=20)
            f = Fight(self.hero, enemy)
            start_fight()
        elif self.dungeon_map[self.x][self.y] == ".":
            pass
        elif self.dungeon_map[self.x][self.y] == "S":
            pass
        elif self.dungeon_map[self.x][self.y] == "G":
            print("You have cleared the dungeon!")

    def check_for_enemy(self, ran):
        for i in range(1, ran):
                if (self.dungeon_map[self.x + i][self.y] == "E" or
                        self.dungeon_map[self.x - i][self.y] == "E" or
                        self.dungeon_map[self.x][self.y + i] == "E" or
                        self.dungeon_map[self.x][self.y - i] == "E"):
                    return True
                else:
                    return False

    def hero_attack(self, by):
        if by == "spell":
            if self.hero.spell != None:
                ran = self.hero.spell.cast_range
                if self.check_for_enemy(ran):
                    enemy = Enemy(health=100, mana=100, damage=20)
                    f = Fight(self.hero, enemy)
                    start_fight()
            else:
                print(f"You can\'t attack, because you don\'t know any spells.")
        if by == "weapon":
            if self.hero.weapon != None:
                if self.check_for_enemy(0):
                    enemy = Enemy(health=100, mana=100, damage=20)
                    f = Fight(self.hero, enemy)
                    start_fight()
            else:
                print(f"You can\'t attack, because you don\'t have a weapon.")
