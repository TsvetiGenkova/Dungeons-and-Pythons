from hero import Hero
from dungeon import Dungeon
from fight import Fight
from enemy import Enemy
from utils import check_for_stuff
from weapon_and_spells import Spell
from weapon_and_spells import Weapon

def start_screen()
    print("Welcome to Dungeon and pythons!")
    print("The goal of the game is to find the treasures hidden in the dungeon and reach the gateway \'G\'.")
    print("But beware the fierce enemys that you can meet in the dark...\n\n")
    print("First create your hero.")
    n = input("Give him/her a name: ") 
    t = input("And a title: ")
    h = Hero(name=n, title=t)
    print(f"Very well your hero is known as {str(h.known_as())}")
    print(f"and his stats are: health - {h.get_health()}, mana - {h.get_mana()}, mana regeneration rate - {h.get_mana_regeneration_rate()}")
    #print("Do you want to equip your hero with weapon or spell before the start or find them in the dungeon? (y/n)")
    m = input(f"Now pick a level: ")
    print("Your hero is \'H\' and where you see \'E\' there is an enemy. If you reach \'T\' treasure awaits you.")
    map = f"{m}.txt"
    d = Dungeon(map)
    d.spawn(h)
    w = Weapon(name="The Axe of Destiny", damage=20)
    s = Spell(name="Fireball", damage=40, mana_cost=80, cast_range=3)
    h.equip(w)
    h.learn(s)
    d.print_map()


def main():
    start_screen()

    while d.cleared == False:
        if d.hero_attack(by="spell"):
            des = input("There is an enemy in the range of your spell. You can start a fight. (y/n) ")
            if des == "y":
                ran = h.spell.get_cast_range()
                enemy = Enemy.generate_enemy()
                enemy_coords = check_for_stuff(d.dungeon_map, d.x, d.y, "E", ran)
                f = Fight(h, enemy, enemy_coords, d.dungeon_map)
                f.start_fight()
            elif des == "n":
                dir = input("Pick direction for your hero to go! ")
                d.move_hero(dir)
        elif d.hero_attack(by="weapon"):
            des = input("There is an enemy near you. You can start a fight. (y/n) ")
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
    

if __name__ == '__main__':
    main()