from functools import reduce
from typing import List

from getdata import getdata

content = getdata.getdata('day0')
content = getdata.separarPorLineas(content)


class Monkey:
    name: int
    items = List[int]
    operation: str
    test: int
    if_true: int
    if_false: int

    n_inspections: int = 0

    def __init__(self, name, operation='', test=0, if_true=0, if_false=0, n_inspections=0):
        self.name = name
        self.items = []
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

    def __repr__(self):
        return f'Monkey {self.name}'

    def __str__(self):
        return f'Monkey {self.name}: {self.items}'

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def load_monkeys(data: List[str]) -> List[Monkey]:
    monkeys = []
    for line in data:
        if line.__contains__('Monkey'):
            i = line.find(':')
            monkeys.append(Monkey(line[i - 1]))

        elif line.__contains__('items'):
            i = line.find(':')
            items = [int(x) for x in line[i + 1:].replace(' ', '').split(',')]
            monkeys[-1].items = items

        elif line.__contains__('Operation'):
            i = line.find(':')
            monkeys[-1].operation = line[i + 1:].replace(' ', '').replace('new=', '').replace('old', 'item')

        elif line.__contains__('Test'):
            i = line.find(':')
            monkeys[-1].test = int(''.join(x for x in line[i + 1:] if x.isdigit()))

        elif line.__contains__('If true'):
            i = line.find(':')
            monkeys[-1].if_true = int(''.join(x for x in line[i + 1:] if x.isdigit()))

        elif line.__contains__('If false'):
            i = line.find(':')
            monkeys[-1].if_false = int(''.join(x for x in line[i + 1:] if x.isdigit()))

    return monkeys


def first_star(monkeys):
    for i in range(20):
        for monkey in monkeys:
            copy = monkey.items.copy()
            for item in copy:
                monkey.items.remove(item)
                monkey.n_inspections += 1
                operation = monkey.operation
                result = eval(operation)
                result = result // 3
                if result % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(result)
                else:
                    monkeys[monkey.if_false].items.append(result)

        print(i)
        for monkey in monkeys:
            print(monkey)
        print()


def calculate_multiplo(monkeys):
    multiplicacion = 1
    for monkey in monkeys:
        multiplicacion *= monkey.test

    return multiplicacion


def second_star(monkeys):
    multiplo = calculate_multiplo(monkeys)
    for i in range(10000):
        print(i)
        for monkey in monkeys:
            copy = monkey.items.copy()
            for item in copy:
                monkey.items.remove(item)
                monkey.n_inspections += 1
                operation = monkey.operation
                result = eval(operation)
                result = result % multiplo
                if result % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(result)
                else:
                    monkeys[monkey.if_false].items.append(result)

        for monkey in monkeys:
            print(monkey)

    interactions = [x.n_inspections for x in monkeys]
    interactions.sort()
    print(interactions)
    return interactions[-1] * interactions[-2]





print(second_star(load_monkeys(content)))