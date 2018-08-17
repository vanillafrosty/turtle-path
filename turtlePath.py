import math, pdb
from decimal import Decimal

def turtlePath(path):
    f = open(path, 'r')
    lines = f.readlines()
    num_obs, num_paths = lines[0].split(' ')
    num_obs = int(num_obs)
    num_paths = int(num_paths[0:len(num_paths)-1])
    obs = {}
    for ob in range(1, num_obs+1):
        x,y = lines[ob].split(' ')
        x = int(x)
        y = int(y[0:len(y)-1])
        obs[(x,y)] = True
    curr_pos = (0,0)
    #influences curr_pos delta for reach move based on direction turtle is facing
    curr_dir = (0,1)
    #max straight line distance from the origin
    max_dist = 0
    for l in range(2, len(lines)):
        command = lines[l]
        c_type = command[0]
        if c_type != 'M':
            curr_dir = change_dir(c_type, curr_dir)
        else:
            dist = int(command[2:len(command)-1])
            delta = collision_block(obs, curr_dir, curr_pos, dist)
            curr_pos = (curr_pos[0]+delta[0], curr_pos[1]+delta[1])
            hypotenuse = math.sqrt(curr_pos[0]**2 + curr_pos[1]**2)
            max_dist = hypotenuse if hypotenuse > max_dist else max_dist
    f.close()
    return float(round(Decimal.from_float(max_dist), 2))

def change_dir(c_type, curr_dir):
    if c_type == 'L':
        change = (-1,1)
    elif c_type == 'R':
        change = (1,-1)
    if curr_dir[0] == 0:
        return (curr_dir[1]*change[0], 0)
    elif curr_dir[1] == 0:
        return (0, curr_dir[0]*change[1])

def collision_block(obs, curr_dir, curr_pos, dist):
    x,y = curr_pos
    dx, dy = curr_dir
    for d in range(1, dist+1):
        if dx == 0 and ((x, y+(d*dy)) in obs):
            return (0, (d-1)*dy)
        if dy == 0 and ((x+(d*dx), y) in obs):
            return ((d-1)*dx, 0)
    return (curr_dir[0]*dist, curr_dir[1]*dist)



print(turtlePath("turtle_path.txt"))
