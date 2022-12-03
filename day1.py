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

def second_star(data: list):
    maximos = []

    counter = 0
    for line in data:
        if line == '':
            maximos.append(counter)
            maximos.sort(reverse=True)
            if len(maximos)>3:
                maximos.pop()
            counter = 0
        else:
            counter += int(line)
    return sum(maximos)

print(second_star(getdata.separarPorLineas(content)))