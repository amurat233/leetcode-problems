#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
def snail(snail_map):
    a=0
    y=0
    x=0
    new_list = []
    next_direction = False
    try:
        new_list.append(snail_map[y][x])
        snail_map[y][x] = None
    except:
        return new_list
    while True:
        if not(up(snail_map,y,x) or down(snail_map,y,x) or left(snail_map,y,x) or right(snail_map,y,x)):
            return new_list
        if a == 0:
            if right(snail_map, y, x):
                snail_map[y][x] = None
                y,x = right(snail_map,y,x)
                new_list.append(snail_map[y][x])
            else:
                next_direction = True
        elif a == 1:
            if down(snail_map, y, x):
                snail_map[y][x] = None
                y,x = down(snail_map,y,x)
                new_list.append(snail_map[y][x])
            else:
                next_direction = True
        elif a == 2:
            if left(snail_map, y, x):
                snail_map[y][x] = None
                y,x = left(snail_map,y,x)
                new_list.append(snail_map[y][x])
            else:
                next_direction = True
        else:
            if up(snail_map, y, x):
                snail_map[y][x] = None
                y,x = up(snail_map,y,x)
                new_list.append(snail_map[y][x])
            else:
                next_direction = True
        if next_direction:
            a+=1
            next_direction = False
        if a == 4:
            a = 0

def up(map,y,x):
    y-= 1
    try:
        map[y][x]
    except:
        return False
    if map[y][x] == None:
        return False
    return y,x
    
def down(map,y,x):
    y+=1
    try:
        map[y][x]
    except:
        return False
    if map[y][x] == None:
        return False
    return y,x
def right(map,y,x):
    x+=1
    try:
        map[y][x]
    except:
        return False
    if map[y][x] == None:
        return False
    return y,x
def left(map,y,x):
    x-=1
    try:
        map[y][x]
    except:
        return False
    if map[y][x] == None:
        return False
    return y,x
array = [[1]]
print(snail(array))