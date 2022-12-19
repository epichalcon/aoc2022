from getdata import getdata

content = getdata.getdata('day4')
content = getdata.separarPorLineas(content)

def parse_pair(pair: str):
    splitted_pair = pair.split(',')
    first_elf =  [int(num) for num in splitted_pair[0].split('-')]
    second_elf = [int(num) for num in splitted_pair[1].split('-')]
    return first_elf, second_elf

def first_star(data):
    fully_contained_pairs = 0
    for pair in data:
        first_elf, second_elf = parse_pair(pair)
        if (first_elf[0] <= second_elf[0] and first_elf[1] >= second_elf[1]) or\
                (second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1]):
            fully_contained_pairs += 1

    return fully_contained_pairs

def second_star(data):
    overlapping_pairs = 0
    for pair in data:
        first_elf, second_elf = parse_pair(pair)
        if (first_elf[0] <= second_elf[0] <= first_elf[1]) or\
                (first_elf[0] <= second_elf[1] <= first_elf[1]) or\
                (second_elf[0] <= first_elf[0] <= second_elf[1]) or\
                (second_elf[0] <= first_elf[1] <= second_elf[1]):
            overlapping_pairs += 1

    return overlapping_pairs

print(second_star(content))