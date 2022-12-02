from getdata import getdata

content = getdata.getdata('day1')

def first_star(data: list):
    maximo = 0
    counter = 0
    for line in data:
        if line == '':
            maximo = max(maximo, counter)
            counter = 0
        else:
            counter += int(line)

    return maximo

def insert_in_order(num, maximos):
    aux = maximos.copy()
    for i, maximo in enumerate(aux):
        if maximo < num:
            maximos.insert(i, num)
            break

    maximos.append(num)

    while len(maximos) > 3:
        maximos.pop()


def second_star(data: list):
    maximos = []

    counter = 0
    for line in data:
        if line == '':
            insert_in_order(counter, maximos)
            counter = 0
        else:
            counter += int(line)
    insert_in_order(counter, maximos)
    return sum(maximos)

print(second_star(getdata.separarPorLineas(content)))