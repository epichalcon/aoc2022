from getdata import getdata

content = getdata.getdata('day18')
content = getdata.separarPorLineas(content)
max_coords = (0,0,0)

def parse_input(line):
    return tuple(map(int, line.split(',')))


directions = ((1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1))
# calculates ortogonally contected cubes
def adjacent_cubes(coords) -> list:
    x, y, z = coords
    return [(x + dx, y + dy, z + dz) for dx, dy, dz in directions]


def update_max_coords(coords):
    global max_coords
    max_coords = (max(max_coords[0], coords[0]), max(max_coords[1], coords[1]), max(max_coords[2], coords[2]))


def part1(cubes):
    cube_sides = {}
    for line in cubes:
        coords = parse_input(line)
        update_max_coords(coords)
        number_of_adjacent_cubes = 0
        for cube in adjacent_cubes(coords):
            if cube in cube_sides:
                number_of_adjacent_cubes += 1
                cube_sides[cube] -= 1


        cube_sides[coords] = 6 - number_of_adjacent_cubes

    return sum(cube_sides.values()), cube_sides

def part2(cube_sides):
    steam_sides = {}
    next_cubes ={(0,0,0)}
    while len(next_cubes) > 0:
        sides = 6
        actual_steam = next_cubes.pop()
        number_of_adjacent_cubes = 0
        for cube in adjacent_cubes(actual_steam):
            if cube in cube_sides:
                continue
            if cube[0] < -1 or cube[1] < -1 or cube[2] < -1:
                sides -= 1
                continue

            if cube[0] > max_coords[0] or cube[1] > max_coords[1] or cube[2] > max_coords[2]:
                sides -= 1
                continue

            if cube in steam_sides:
                number_of_adjacent_cubes += 1
                steam_sides[cube] -= 1

            else:
                if cube not in steam_sides:
                    next_cubes.add(cube)


        steam_sides[actual_steam] = sides - number_of_adjacent_cubes


    return sum(steam_sides.values())

sides, cube_sides = part1(content)
print(sides)
max_coords = (max_coords[0] + 1, max_coords[1] + 1, max_coords[2] + 1)
print(part2(cube_sides))
