from getdata import getdata

content = getdata.getdata('day14')
content = getdata.separarPorLineas(content)


def rock_path(node_pair):
    if node_pair[0][0] == node_pair[1][0]:
        if node_pair[0][1] < node_pair[1][1]:
            for i in range(node_pair[0][1], node_pair[1][1] + 1):
                yield (node_pair[0][0], i)
        else:
            for i in range(node_pair[1][1], node_pair[0][1] + 1):
                yield (node_pair[0][0], i)
    elif node_pair[0][1] == node_pair[1][1]:
        if node_pair[0][0] < node_pair[1][0]:
            for i in range(node_pair[0][0], node_pair[1][0] + 1):
                yield (i, node_pair[0][1])
        else:
            for i in range(node_pair[1][0], node_pair[0][0] + 1):
                yield (i, node_pair[0][1])


def create_topology(data):
    '''
    Creates a topology of the data and calculates the beginning and end of the topology
    :param data: list of rockpaths in the form of [x1,y2 -> x2,y2 -> ... -> xn,yn, ...,]
    :return: the topology [[(x1,y1), (x2,y2), ...], ...] and the beginning and end of the topology
    '''
    topology_start = float('inf')
    topology_end = 0
    floor_level = 0
    topology: set = set()
    for line in data:
        line = line.split(' -> ')
        for i, node in enumerate(line):
            node = node.split(',')
            topology_start = min(topology_start, int(node[0]))
            topology_end = max(topology_end, int(node[0]))
            floor_level = max(floor_level, int(node[1]))
            if i == len(line)-1:
                continue
            end_node = line[i+1].split(',')
            node_pair = ((int(node[0]), int(node[1])),
                         (int(end_node[0]), int(end_node[1])))

            for coords in rock_path(node_pair):
                topology.add(coords)




    return topology, topology_start, topology_end, floor_level + 2


def sand_move(sand_position, topology, floor=None):
    '''
    Calculates the next position of the sand
    :param sand_position: the current position of the sand
    :param topology: the topology of the rocks
    :return: the next position of the sand
    '''
    if floor is not None:
        if sand_position[1] == floor - 1:
            return sand_position

    if (sand_position[0], sand_position[1] + 1) in topology:
        if (sand_position[0] - 1, sand_position[1] + 1) in topology and \
                (sand_position[0] + 1, sand_position[1] + 1) in topology:
            return sand_position
        else:
            if (sand_position[0] - 1, sand_position[1] + 1) not in topology:
                return sand_position[0] - 1, sand_position[1] + 1
            else:
                return sand_position[0] + 1, sand_position[1]
    else:
        return sand_position[0], sand_position[1] + 1


def first_star(topology, start, end):
    '''
    Calculates the first star
    :param topology: the topology of the rocks
    :param start: the beginning of the topology
    :param end: the end of the topology
    :return: return the number of sand grains until they fall to the void
    '''

    sand_start = (500, 0)
    sand_grains_fallen = 0
    sand_in_topology = True

    while sand_in_topology:
        sand_position = (sand_start[0], sand_start[1])
        sand_in_motion = True
        while sand_in_motion:
            next_sand_position = sand_move(sand_position, topology)
            if not start < next_sand_position[0] < end:
                return sand_grains_fallen

            if sand_position == next_sand_position:
                topology.add(next_sand_position)
                sand_in_motion = False
            else:
                sand_position = next_sand_position
        sand_grains_fallen += 1


def second_star(topology, floor):
    sand_start = (500, 0)
    sand_grains_fallen = 0
    sand_positions = []

    while True:
        sand_position = (sand_start[0], sand_start[1])
        sand_in_motion = True
        while sand_in_motion:
            next_sand_position = sand_move(sand_position, topology, floor)
            if next_sand_position == sand_start:
                return sand_grains_fallen + 1


            if sand_position == next_sand_position:
                topology.add(next_sand_position)
                sand_positions.append(next_sand_position)
                sand_in_motion = False
            else:
                sand_position = next_sand_position
        sand_grains_fallen += 1




topology, start, end, floor = create_topology(content)

print(second_star(topology, floor))