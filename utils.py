from Person import Person
from hero import Hero
from enemy import Enemy
from random import randint
from weapon_and_spells import Spell
from weapon_and_spells import Weapon


def check_for_stuff(dungeon_map, x, y, stuff, ran):
    assert type(x) is int and x >=0, 'X must be integer and positive'
    assert type(y) is int and y >= 0, 'Y must be integer and positive'
    assert type(ran) is int, 'ran must be integer'
    assert ran > 0, 'ran must be positive'
    assert type(stuff) is str, 'Stuff must be string'
    assert stuff == 'H' or stuff == 'E', 'Stuff must be H or E'
    assert type(dungeon_map) is list, 'dungeon_map must be list'
    for i in range(1, ran + 1):
        try:
            dungeon_map[x + i][y]
            if dungeon_map[x + i][y] == stuff:
                return (x + i, y)
            tmp = False
        except IndexError:
            tmp = False
        try:
            dungeon_map[x - i][y]
            if dungeon_map[x - i][y] == stuff and x - i >= 0:
                return (x - i, y)
            tmp = False
        except IndexError:
            tmp = False
        try:
            dungeon_map[x][y + i]
            if dungeon_map[x][y + i] == stuff:
                return (x, y + i)
            tmp = False
        except IndexError:
            tmp = False
        try:
            dungeon_map[x][y - i]
            if dungeon_map[x][y - i] == stuff and y - i >= 0:
                return (x, y - i)
            tmp = False
        except IndexError:
            tmp = False
    return tmp


class Move():

    def __init__(self, inst):
        assert isinstance(inst, Person), 'Must be instance of Person class.'
        self.inst = inst
        self.cleared = False

    def pick_treasure(self):
        t = []
        with open("loot.txt", 'r') as f:
            for i in f.readlines():
                t.append(i)
        treasure = t[randint(0, len(t) - 1)].split(",")
        if treasure[0] == "weapon":
            tmp = float(treasure[2]) if '.' in treasure[2] else int(
                treasure[2])
            tr = Weapon(name=treasure[1], damage=tmp)
            self.inst.equip(tr)
        elif treasure[0] == "spell":
            tmp = float(treasure[2]) if '.' in treasure[2] else int(
                treasure[2])
            tmp1 = float(treasure[3]) if '.' in treasure[3] else int(
                treasure[3])
            tr = Spell(name=treasure[1], damage=tmp,
                       mana_cost=tmp1, cast_range=int(treasure[4]))
            self.inst.learn(tr)
        else:
            if isinstance(self.inst, Hero):
                if treasure[0] == "Mana potion":
                    self.inst.take_mana(int(treasure[1]))
                    tr = f"Mana potion = {int(treasure[1])} mana"
                elif treasure[0] == "Health potion":
                    self.inst.take_healing(int(treasure[1]))
                    tr = f"Health potion {int(treasure[1])} health"
            elif isinstance(self.inst, Enemy):
                print("The enemy can heal themself.")
                tr = 0

        return tr

    def is_safe(self, oposite_abrv, dungeon_map, x, y):
        assert type(x) is int, 'x must be int'
        assert type(y) is int, 'y must be int'
        try:
            dungeon_map[x][y]
            if dungeon_map[x][y] == '#' or dungeon_map[x][y] == oposite_abrv:
                return False
            return True
        except IndexError:
            return False

    def move_util(self, abrv, dungeon_map, curr_x, curr_y, x, y):
        
        if dungeon_map[curr_x + x][curr_y + y] == ".":
            pass
        elif dungeon_map[curr_x + x][curr_y + y] == "S":
            pass
        elif dungeon_map[curr_x + x][curr_y + y] == "G":
            print("You have cleared the dungeon!")
            self.cleared = True
        elif dungeon_map[curr_x + x][curr_y + y] == "T":
            print(f"Found {self.pick_treasure()}!")
        elif dungeon_map[curr_x + x][curr_y + y] == "E":
            des = input(
                "There is an enemy in the direction you wish to go. Do you want to start a fight. (y/n) ")
            if des == "y":
                enemy = Enemy.generate_enemy()
                enemy_coords = check_for_stuff(
                    self.dungeon_map, curr_x, curr_y, "E", 1)
                f = Fight(self.hero, enemy, enemy_coords, self.dungeon_map)
                f.start_fight()
            elif des == "n":
                pass
        dungeon_map[curr_x][curr_y] = '.'
        dungeon_map[curr_x + x][curr_y + y] = abrv
        curr_y += y
        curr_x += x
        return (curr_x, curr_y, dungeon_map)

    def move(self, dungeon_map, curr_x, curr_y, direction):
        assert type(direction) is str, 'Direction must be string'
        "up", "down", "left" and "right"
        assert direction == 'up' or direction == 'down' \
            or direction == 'left' or direction == 'right',\
            'Direction must be up,down, left or right'
        assert type(curr_x) is int and type(
            curr_y) is int, 'curr_x and curr_y must be integers'
        assert curr_x > 0 and curr_y > 0, 'curr_x and curr_y must be positive'
        if isinstance(self.inst, Hero):
            abrv = "H"
            oposite_abrv = "E"
        elif isinstance(self.inst, Enemy):
            abrv = "E"
            oposite_abrv = "H"

        if direction == 'up' and self.is_safe(oposite_abrv, dungeon_map, curr_x - 1, curr_y):
            return self.move_util(abrv, dungeon_map, curr_x, curr_y, -1, 0)

        elif direction == 'down' and self.is_safe(oposite_abrv, dungeon_map, curr_x + 1, curr_y):
            return self.move_util(abrv, dungeon_map, curr_x, curr_y, 1, 0)

        elif direction == 'left' and self.is_safe(oposite_abrv, dungeon_map, curr_x, curr_y - 1):
            return self.move_util(abrv, dungeon_map, curr_x, curr_y, 0, -1)

        elif direction == 'right' and self.is_safe(oposite_abrv, dungeon_map, curr_x, curr_y + 1):
            return self.move_util(abrv, dungeon_map, curr_x, curr_y, 0, 1)

        return False
