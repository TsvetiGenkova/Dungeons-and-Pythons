def check_for_enemy(dungeon_map, x, y, ran):
    for i in range(1, ran):
        if (dungeon_map[x + i][y] == "E" or
                dungeon_map[x - i][y] == "E" or
                dungeon_map[x][y + i] == "E" or
                dungeon_map[x][y - i] == "E"):
            return True
    return False



class Move():

    def is_safe(dungeon_map, x, y):
        assert type(x) is int, 'x must be int'
        assert type(y) is int, 'y must be int'
        try:
            dungeon_map[x][y]
            if dungeon_map[x][y] == '#':
                return False
            return True
        except IndexError:
            return False


    def move_util(abrv, dungeon_map, curr_x, curr_y, x, y):
        #self.where_are_you(curr_x + x, curr_y + y)
        dungeon_map[curr_x][curr_y] = '.'
        dungeon_map[curr_x + x][curr_y + y] = abrv
        curr_y += y
        curr_x += x

    @classmethod
    def move(cls, dungeon_map, curr_x, curr_y, direction):
        assert type(direction) is str, 'Direction must be string'
        "up", "down", "left" and "right"
        assert direction == 'up' or direction == 'down' \
            or direction == 'left' or direction == 'right',\
            'Direction must be up,down, left or right'
        
        if cls.__name__ == "Dungeon":
            abrv = "H"
        elif cls.__name__ == "Fight":
            abrv = "E"


        if direction == 'up' and is_safe(curr_x - 1, curr_y):
            move_util(abrv, dungeon_map, curr_x, curr_y, -1, 0)
            return True

        elif direction == 'down' and is_safe(curr_x + 1, curr_y):
            move_util(abrv, dungeon_map, curr_x, curr_y, 1, 0)
            return True

        elif direction == 'left' and is_safe(curr_x, curr_y - 1):
            move_util(abrv, dungeon_map, curr_x, curr_y, 0, -1)
            return True

        elif direction == 'right' and is_safe(curr_x, curr_y + 1):
            move_util(abrv, dungeon_map, curr_x, curr_y, 0, 1)
            return True
        return False