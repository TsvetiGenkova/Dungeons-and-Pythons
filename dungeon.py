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


# d = Dungion('map.txt')

# a = d.spawn(Hero(name='ivan', title='Light', health=100,
#                  mana=100, mana_regeneration_rate=2))
# print(a)

# a = d.spawn(Hero(name='ivan', title='Light', health=100,
#                  mana=100, mana_regeneration_rate=2))
# print(a)
# a = d.spawn(Hero(name='ivan', title='Light', health=100,
#                  mana=100, mana_regeneration_rate=2))
# print(a)
# d.print_map()
