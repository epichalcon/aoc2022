from getdata import getdata

content = getdata.getdata('day3')
content = getdata.separarPorLineas(content)

def get_priority(item: str):
    if item.islower():
        return ord(item) - 96
    if item.isupper():
        return ord(item) - 38

def first_star(data: list):

    prioritysum = 0

    for rucksack in data:
        compartment1 = rucksack[:len(rucksack)//2]
        compartment2 = rucksack[len(rucksack)//2:]
        compartment1set = set(compartment1)
        compartment2set = set(compartment2)

        repeted = compartment1set.intersection(compartment2set)
        prioritysum += get_priority(repeted.pop())

    return prioritysum

def second_star(data: list):

    prioritysum = 0

    group_rucksacks = []

    for i, rucksack in enumerate(data):
        rucksack_items = set(rucksack)

        group_rucksacks.append(rucksack_items)

        if i%3 == 2:
            badge = group_rucksacks[0].intersection(group_rucksacks[1]).intersection(group_rucksacks[2])
            prioritysum += get_priority(badge.pop())
            group_rucksacks.clear()

    return prioritysum

print(second_star(content))