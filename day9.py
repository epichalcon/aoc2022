import operator
from typing import List

from getdata import getdata

directions = {
    'R': [1,0],
    'L': [-1,0],
    'U': [0,1],
    'D': [0,-1]
}

content = getdata.getdata('day9')
content = getdata.separarPorLineas(content)



def parse(instruction: str):
    separated = instruction.split(' ')
    return separated[0], int(separated[1])

def in_area_1(H_pos: List[int], T_pos: List[int]):
    return H_pos[0] - 2 < T_pos[0] < H_pos[0] + 2 and H_pos[1] - 2 < T_pos[1] < H_pos[1] + 2

def in_area_10(H_pos: List[int], T_pos: List[int]):
    return H_pos[0] - 11 < T_pos[0] < H_pos[0] + 11 and H_pos[1] - 11 < T_pos[1] < H_pos[1] + 11

def get_in_area(H_pos: List[int], T_pos: List[int], direction):
    res = list(map(operator.add, T_pos, directions[direction]))
    if not (H_pos[0] == T_pos[0] or H_pos[1] == T_pos[1]):
        if H_pos[0] - 2 == res[0] or res[0] == H_pos[0] + 2 or H_pos[1] - 2 == res[1] or res[1] == H_pos[1] + 2:
            if direction == 'R' or direction == 'L':
                res[1] = (H_pos[1] + res[1]) // 2
            else:
                res[0] = (H_pos[0] + res[0]) // 2
        else:
            if direction == 'R' or direction == 'L':
                res[1] = H_pos[1]
            else:
                res[0] = H_pos[0]

    return res


def first_star(data):
    H_pos = [0, 0]
    T_pos = [0, 0]
    visited = {'0,0'}
    for instruction in data:
        dir, steps = parse(instruction)
        while steps > 0:
            H_pos = list(map(operator.add, H_pos, directions[dir]))
            if not in_area_1(H_pos, T_pos):
                T_pos = get_in_area(H_pos, T_pos, dir)

            visited.add(f'{T_pos[0]},{T_pos[1]}')
            steps-=1

    return len(visited), visited

def second_star(data):
    rope = [[0,0] for i in range(0,10)]
    visited = {'0,0'}
    for instruction in data:
        dir, steps = parse(instruction)
        while steps > 0:
            rope[0] = list(map(operator.add, rope[0], directions[dir]))
            for i, node in enumerate(rope):
                if i == 0:
                    continue

                if not in_area_1(rope[i-1], node):
                    rope[i] = get_in_area(rope[i-1], node, dir)

            visited.add(f'{rope[-1][0]},{rope[-1][1]}')
            steps-=1

    return len(visited), visited


print(first_star(content))
print(second_star(content))