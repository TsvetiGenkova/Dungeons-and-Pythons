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


def main():
    print("Welcome to Dungeon and pythons!")
    print("The goal of the game is to find the treasures hidden in the dungeon and reach the gateway \'G\'.")
    print("But beware the fierce enemys that you can meet in the dark...\n\n")
    print("First create your hero.")
    n = input("Give him/her a name: ")
    t = input("And a title: ")
    h = Hero(name=n, title=t)
    print(f"Very well your hero is known as {str(h.known_as())}")
    print(f"and his stats are: health - {h.get_health()}, mana - {h.get_mana()}, mana regeneration rate - {h.get_mana_regeneration_rate()}")

    map=get_map_names()
    print(map)
    m = input(f"\n Now pick a level: ")
    while m not in get_map_names() :
        m = input(f"\n Wrong file name, pick again : ")
    map.remove(m)
    give_map = f"Maps/{m}"
    # add asserts about the map and names
    d = Dungeon(give_map)
    d.spawn(h)
    w = Weapon(name="The Axe of Destiny", damage=20)
    s = Spell(name="Fireball", damage=40, mana_cost=80, cast_range=3)
    h.equip(w)
    h.learn(s)
    d.print_map()
# d.cleared
    while True:
        if d.hero_attack(by="spell"):
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
                dir = input("Pick direction for your hero to go! ")
                d.move_hero(dir)
        elif d.hero_attack(by="weapon"):
            des = input(
                "There is an enemy near you. You can start a fight. (y/n) ")
            if des == "y":
                enemy = Enemy.generate_enemy()
                enemy_coords = check_for_stuff(d.dungeon_map, d.x, d.y, "E", 1)
                f = Fight(h, enemy, enemy_coords, d.dungeon_map)
                f.start_fight()
            elif des == "n":
                dir = input("Pick direction for your hero to go! ")
                d.move_hero(dir)

        if h.is_alive():
            dir = input("Pick direction for your hero to go! ")
            d.move_hero(dir)
        else:
            inp = input("You died do you want to respawn? (y/n) ")
            if inp == "y":
                h.health = h.max_health
                h.mana = h.max_mana
                if d.spawn(h):
                    d.print_map()
                else:
                    print("There is no spawning points.")
                    break
            elif inp == "n":
                break
        if d.cleared == True:
            print('You cleared the dungon')
            das = input('Go to next ? y/n  ')
            if das == 'y':
                hero = d.hero
                d = Dungeon('Maps/'+map[0])
                d.spawn(hero)
                map.remove(map[0])
                d.print_map()
            else:
                print('Game finished')
                break
        print(d.cleared)





if __name__ == '__main__':
    main()
