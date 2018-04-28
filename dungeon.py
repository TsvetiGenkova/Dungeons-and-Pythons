import os
from fight import Fight
from hero import Hero
from enemy import Enemy
import random
from weapon_and_spells import Spell
from weapon_and_spells import Weapon
from utils import Move
from utils import check_for_stuff

class Dungeon(Move):

    def __init__(self, map_file):
        assert type(map_file) is str, 'map_file must be string'
        assert os.path.isfile(map_file) is True, 'map_file is not file'
        self.map_file = map_file
        self.dungeon_map = self.load_map()
        self.spawning_cordinates = self.get_all_spawning_cordinates()
        self.hero = None
        self.x = None
        self.y = None
        self.cleared = False

    def get_all_spawning_cordinates(self):
        spawning_cordinates = []
        for index, value in enumerate(self.dungeon_map):
            for y_index, y_value in enumerate(value):
                if y_value == 'S':
                    spawning_cordinates.append([(index, y_index), False])
        return spawning_cordinates

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
        m = Move(self.hero)
        tmp = m.move(self.dungeon_map, self.x, self.y, direction)
        if m.cleared:
            self.cleared == True
        if tmp:
            self.x = tmp[0]
            self.y = tmp[1]
            self.print_map()
        else:
            if not self.hero.is_alive():
                des  = input("Do you want to respawn? (y/n) ")
                if des == "y":
                    self.hero.health = self.hero.max_health
                    self.hero.mana = self.hero.max_mana
                    self.spawn(self.hero)
                    self.print_map()
                else:
                    pass
            dir = input("You can\'t move that way! Pick another direction! ")
            self.move_hero(dir)


    def hero_attack(self, by):
        if by == "spell":
            if self.hero.can_cast():
                ran = self.hero.spell.get_cast_range()
                if check_for_stuff(self.dungeon_map, self.x, self.y, "E", ran):
                    return True
                else:
                    return False
            else:
                return False
                print(f"You can\'t attack, because you don\'t know any spells or don\'t have mana.")
        if by == "weapon":
            if self.hero.weapon != None:
                if check_for_stuff(self.dungeon_map, self.x, self.y, "E", 1):
                    return True
                else:
                    return False
            else:
                print(f"You can\'t attack, because you don\'t have a weapon.")
                return False
