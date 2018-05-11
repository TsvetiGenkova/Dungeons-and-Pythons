from hero import Hero
from dungeon import Dungeon
from fight import Fight
from enemy import Enemy
from utils import check_for_stuff
from weapon_and_spells import Spell
from weapon_and_spells import Weapon
import os


def get_map_names():
    list_of_maps = []
    for i in os.listdir('Maps'):
        if i.endswith('.txt'):
            list_of_maps.append(i)
    return list_of_maps

def map_exists(map_name):
    return os.path.exists(map_name)

def print_map_names(names):
    for i in names:
        print(i.replace('.txt', ''))

def get_right_direction():
    directions = ['up', 'right', 'left', 'down']
    direction = input("Pick direction for your hero to go! ")
    if direction in directions:
        return direction
    else:
        while direction not in directions:
            direction = input('Not direction, type again ')
        return direction

def start_screen():
    print("Welcome to Dungeon and pythons!")
    print("The goal of the game is to find the treasures hidden in the dungeon and reach the gateway \'G\'.")
    print("But beware the fierce enemys that you can meet in the dark...\n\n")
    print("First create your hero.")
    n = input("Give him/her a name: ")
    t = input("And a title: ")
    global h
    h = Hero(name=n, title=t)
    print(f"Very well your hero is known as {str(h.known_as())}")
    print(f"and his stats are: health - {h.get_health()}, mana - {h.get_mana()}, mana regeneration rate - {h.get_mana_regeneration_rate()}")

def do_you_wanna_start_a_fight():
    if d.hero_attack(by="spell") is True:
        des = input(
            "There is an enemy in the range of your spell. You can start a fight. (y/n) ")
        if des == "y":
            ran = h.spell.get_cast_range()
            enemy = Enemy.generate_enemy()
            enemy_coords = check_for_stuff(
                d.dungeon_map, d.x, d.y, "E", ran)
            f = Fight(h, enemy, enemy_coords, d.dungeon_map)
            f.start_fight()
        elif des == "n":
            dir = get_right_direction()
            d.move_hero(dir)
    elif d.hero_attack(by="weapon") is True:
        des = input(
            "There is an enemy near you. You can start a fight. (y/n) ")
        if des == "y":
            enemy = Enemy.generate_enemy()
            enemy_coords = check_for_stuff(d.dungeon_map, d.x, d.y, "E", 1)
            f = Fight(h, enemy, enemy_coords, d.dungeon_map)
            f.start_fight()
        elif des == "n":
            dir = get_right_direction()
            d.move_hero(dir)


def main():
    start_screen()
    
    map = get_map_names()
    map.reverse()
    print_map_names(map)
    m = input(f"Now pick a level: ")
    m = f'{m}.txt'
    while m not in get_map_names():
        m = input(f"Wrong file name, pick again : ")
        m = f'{m}.txt'
    give_map = f"Maps/{m}"
    map.remove(m)
    global d
    d = Dungeon(give_map)
    d.spawn(h)
    print("Your hero is \'H\' and where you see \'E\' there is an enemy. If you reach \'T\' treasure awaits you.")
    w = Weapon(name="The Axe of Destiny", damage=20)
    s = Spell(name="Fireball", damage=40, mana_cost=80, cast_range=3)
    h.equip(w)
    h.learn(s)
    d.print_map()
    
    while True:
        if d.cleared == True:
            das = input('Go to next ? y/n  ')
            if len(map) == 0:
                println('You won the game')
            elif das == 'y':
                hero = d.hero
                d = Dungeon('Maps/' + map[0])
                d.spawn(hero)
                map.remove(map[0])
                d.print_map()
            else:
                print('Game finished')
                break

        do_you_wanna_start_a_fight()

        if h.is_alive():
            dir = get_right_direction()
            d.move_hero(dir)
        else:
            h.health = h.max_health
            h.mana = h.max_mana
            if d.spawn(h):
                inp = input("You died do you want to respawn? (y/n) ")
                if inp == "y":
                    d.print_map()
                elif inp == "n":
                    break
            else:
                print("You lost the game  Q_Q")
                break


if __name__ == '__main__':
    main()
