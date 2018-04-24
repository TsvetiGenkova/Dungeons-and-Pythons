import os


from hero import Hero


class Dungion():

    def __init__(self, map_file):
        assert type(map_file) is str, 'map_file must be string'
        assert os.path.isfile(map_file) is True, 'map_file is not file'
        self.map_file = map_file
        self.dungeon_map = self.load_map()
        self.spawning_cordinates = self.get_all_spawning_cordinates()
        self.hero = None
        self.x = None
        self.y = None
        self.fild_type=None

    def spawn(self, hero):
        assert isinstance(hero, Hero), 'Hero must be instance of Hero class '
        for i in self.spawning_cordinates:
            if i[1] == False:
                self.x = i[0][0]
                self.y = i[0][1]
                self.dungeon_map[self.x][self.y] = 'H'
                i[1] = True
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
            self.fild_type=self.dungeon_map[self.x - 1][self.y]
            self.dungeon_map[self.x][self.y] = '.'
            self.dungeon_map[self.x - 1][self.y] = 'H'
            self.x -= 1
            return True

        elif direction == 'down' and self.is_safe(self.x + 1, self.y):
            self.field_type = self.dungeon_map[self.x + 1][self.y]
            self.dungeon_map[self.x][self.y] = '.'
            self.dungeon_map[self.x + 1][self.y] = 'H'
            self.x += 1
            return True

        elif direction == 'left' and self.is_safe(self.x, self.y - 1):
            self.field_type = self.dungeon_map[self.x][self.y - 1]
            self.dungeon_map[self.x][self.y] = '.'
            self.dungeon_map[self.x][self.y - 1] = 'H'
            self.y -= 1
            return True

        elif direction == 'right' and self.is_safe(self.x, self.y + 1):
            self.field_type = self.dungeon_map[self.x][self.y + 1]
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
        tresure = t[randint(0, len(t))].split(",")

        if tresure[0] == "weapon":
            tmp = float(tresure[2]) if '.' in tresure[2] else int(tresure[2])
            tr = Weapon(name=tresure[1], damage=tmp)
            self.hero.equip(tr)
        elif tresure[0] == "spell":
            tmp = float(tresure[2]) if '.' in tresure[2] else int(tresure[2])
            tmp1 = float(tresure[3]) if '.' in tresure[3] else int(tresure[3])
            tr = Spell(name=tresure[1], damage=tmp,
                       mana_cost=tmp1, cast_range=int(tresure[4]))
            self.hero.learn(tr)
        else:
            if tresure[0] == "Mana potion":
                self.hero.take_mana(int(tresure[1]))
                tr = "Mana potion"
            elif tresure[0] == "Health potion":
                self.hero.take_healing(int(tresure[1]))
                tr = "Health potion"

        return tr

    def where_are_you(self):
        if self.dungeon_map[self.x][self.y] == "T":
            return f"Found {self.pick_treasure()}!"
        elif self.dungeon_map[self.x][self.y] == "E":
            pass
            #start_fight(self.hero, enemy)
        elif self.dungeon_map[self.x][self.y] == ".":
            pass
        elif self.dungeon_map[self.x][self.y] == "S":
            pass
        elif self.dungeon_map[self.x][self.y] == "G":
            print("You have cleared the dungeon!")

    def check_for_enemy(self, ran):
        for i in range(1, ran):
            if self.dungeon_map[self.x + i][self.y] == "E":
                print("There is enemy in range, you can start a fight!")
            elif self.dungeon_map[self.x + i][self.y + i] == "E":
                print("There is enemy in range, you can start a fight!")
            elif self.dungeon_map[self.x + i][self.y - i] == "E":
                print("There is enemy in range, you can start a fight!")
            elif self.dungeon_map[self.x - i][self.y - i] == "E":
                print("There is enemy in range, you can start a fight!")
            elif self.dungeon_map[self.x - i][self.y + i] == "E":
                print("There is enemy in range, you can start a fight!")
            elif self.dungeon_map[self.x - i][self.y] == "E":
                print("There is enemy in range, you can start a fight!")
            elif self.dungeon_map[self.x][self.y + i] == "E":
                print("There is enemy in range, you can start a fight!")
            elif self.dungeon_map[self.x][self.y - i] == "E":
                print("There is enemy in range, you can start a fight!")
            else:
                print("There is no enemy in range!")
                return False
            return True

    def hero_attack(self, by):
        if by == "spell":
            ran = self.hero.spell.cast_range
            if self.check_for_enemy(ran):
                pass
                #start_fight(self.hero, enemy)
        if by == "weapon":
            if self.check_for_enemy(1):
                pass
                #start_fight(self.hero, enemy)


d = Dungion('map.txt')
a = d.spawn(Hero(name='ivan', title='Light', health=100,
                 mana=100, mana_regeneration_rate=2))
d.print_map()

d.move_hero('right')

