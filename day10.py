from typing import List

from getdata import getdata

content = getdata.getdata('day10')
content = getdata.separarPorLineas(content)

def pareser(linea: str):
    splitted_line = linea.split(' ')
    return splitted_line

def calculate_signal_strength(cycles, register):
    if cycles % 40 == 20:
        return register * cycles
    return 0

def first_star(data):
    cycles = 0
    register = 1
    res = 0
    for line in data:
        splited_line = pareser(line)

        if splited_line[0] == 'addx':
            cycles += 1
            res += calculate_signal_strength(cycles, register)
            cycles += 1
            res += calculate_signal_strength(cycles, register)
            register += int(splited_line[1])

        elif splited_line[0] == 'noop':
            cycles += 1
            res += calculate_signal_strength(cycles, register)

    return res

def has_to_draw(cycle, register):
    return register <= cycle % 40 and cycle % 40 <= register + 2

def draw(cycle, register, crt: List[str]):
    if cycle % 40 == 1:
        crt.append('')

    if has_to_draw(cycle, register):
        crt[-1] += '#'
    else:
        crt[-1] += ' '

def second_star(data):
    cycle = 0
    register = 1
    crt: List[str]
    crt = ['']
    for line in data:
        splited_line = pareser(line)

        if splited_line[0] == 'addx':
            cycle += 1
            draw(cycle, register, crt)
            cycle += 1
            draw(cycle, register, crt)
            register += int(splited_line[1])


        elif splited_line[0] == 'noop':
            cycle += 1
            draw(cycle, register, crt)


    return crt



for line in second_star(content):
    print(line)