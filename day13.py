import functools

from getdata import getdata

content = getdata.getdata('day13')
content = content.replace('\n\n', '\n')
content = getdata.separarPorLineas(content)


def separate_pairs(content):
    return [content[i:i + 2] for i in range(0, len(content), 2) if content[i] != '']

def in_order(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return in_order([x], y)
    else:
        if type(y) == int:
            return in_order(x, [y])

    for a, b in zip(x, y):
        comp = in_order(a, b)
        if comp:
            return comp

    return len(x) - len(y)

def first_star(data):
    index_in_order = []
    for i, pair in enumerate(data):

        if in_order(eval(pair[0]), eval(pair[1])) < 0:
            index_in_order.append(i + 1)

    return sum(index_in_order)

def second_star(data):

    data.append('[[2]]')
    data.append('[[6]]')

    data = list(map(eval, data))

    data.sort(key=functools.cmp_to_key(in_order))

    return (data.index([[2]]) + 1) * (data.index([[6]]) + 1)



print(first_star(separate_pairs(content)))

print(second_star(content))