from dataclasses import dataclass, field
from typing import List, Set, Tuple

from getdata import getdata

content = getdata.getdata('day12')
content = getdata.separarPorLineas(content)
content = getdata.getMatrizDeStrings(content)


@dataclass
class Node:
    x: int
    y: int
    steps_taken: int
    altitude: str
    weight: int
    path: List[Tuple[int, int]] = field(default_factory=list)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __greater__(self, other):
        return self.weight > other.weight


def get_dest(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'E':
                return (i, j)


def get_origin(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                return (i, j)


def get_heuristic(cell, dest):
    return abs(dest[0] - cell[0]) + abs(dest[1] - cell[1])


def get_next_cells(actual_node, data):
    altitude = actual_node.altitude
    if actual_node.altitude == 'S':
        altitude = 'a'
    for i in range(-1, 2):
        if actual_node.x + i < 0 or actual_node.x + i >= len(data):
            continue
        for j in range(-1, 2):
            if actual_node.y + j < 0 or actual_node.y + j >= len(data[0]):
                continue
            if abs(i) == abs(j):
                continue

            next_altitude = data[actual_node.x + i][actual_node.y + j]
            if next_altitude == 'E':
                next_altitude = 'z'
            # get the ascii value of a char
            if  ord(next_altitude) <= ord(altitude) + 1:
                yield (actual_node.x + i, actual_node.y + j)


def a_star(data: List[List[str]], origin: Tuple[int, int], dest: Tuple[int, int]):
    actual_node: Node
    open_list: List[Node] = []
    close_list: List[str] = []


    open_list.append(Node(origin[0], origin[1], 0, data[origin[0]][origin[1]], get_heuristic(origin, dest)))

    while len(open_list) > 0:
        actual_node = open_list.pop(0)

        if actual_node.x == dest[0] and actual_node.y == dest[1]:
            return actual_node.steps_taken, actual_node.path

        for cell in get_next_cells(actual_node, data):
            if f'{cell[0]},{cell[1]}' not in close_list:
                h = get_heuristic(cell, dest)
                g = actual_node.steps_taken + 1
                f = h + g

                node = Node(cell[0], cell[1], g, data[cell[0]][cell[1]], f, actual_node.path + [cell])
                if node not in open_list:
                    open_list.append(node)

        open_list.sort(key=lambda x: x.weight)

        close_list.append((f'{actual_node.x},{actual_node.y}'))

    return -1



def print_result(content, path):
    for i, step in enumerate(path):
        if i == len(path) - 1:
            break

        # derecha
        if step[0] == path[i + 1][0] and step[1] < path[i + 1][1]:
            content[step[0]][step[1]] = '>'
        # izquierda
        elif step[0] == path[i + 1][0] and step[1] > path[i + 1][1]:
            content[step[0]][step[1]] = '<'

        # arriba
        elif step[1] == path[i + 1][1] and step[1] < path[i + 1][1]:
            content[step[0]][step[1]] = 'v'
        # abajo
        else:
            content[step[0]][step[1]] = '^'

    with open('output.txt', 'w') as f:
        for line in content:
            f.write(''.join(line) + '\n')

def first_star(data):
    origin = get_origin(data)
    dest = get_dest(data)
    return a_star(data, origin, dest)

def second_star(data):
    min_path = -1
    for i in range(len(data)):
        if data[i][0] == 'a' or data[i][0] == 'S':
            aux = -1
            if min_path == -1:
                min_path, path = a_star(data, (i, 0), get_dest(data))
            else:
                aux, path = a_star(data, (i, 0), get_dest(data))
                if aux != -1:
                    min_path = min(min_path, aux)

            print(aux)


    return min_path, path



steps, path = second_star(content)
print(f'Second star: {steps}')
print_result(content, path)

