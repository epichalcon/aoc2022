from typing import List

from getdata import getdata
content = getdata.getdata('day8')
content = getdata.separarPorLineas(content)

matriz = getdata.getMatrizDeNumeros(content)

def is_seen(data, row, col):
    # seen from top
    i = col
    while i == col or data[row][i] < data[row][col]:
        if i == 0:
            return True
        i -= 1

    i = col
    # seen from bot
    while i == col or data[row][i] < data[row][col]:
        if i == len(data)-1:
            return True
        i += 1

    i = row
    # seen from right
    while i == row or data[i][col] < data[row][col]:
        if i == len(data[0])-1:
            return True
        i += 1

    i = row
    # seen from left
    while i == row or data[i][col] < data[row][col]:
        if i == 0:
            return True
        i -= 1

def scenic_score(data, row, col):
    score = 1

    # seen from top
    partial_score = 0
    i = col - 1
    while i >= 0 and data[row][i] < data[row][col]:
        partial_score += 1
        i -= 1

    if i > 0:
        partial_score += 1

    score *= partial_score

    if score == 0:
        return 0

    # seen from bot
    partial_score = 0
    i = col + 1
    while i < len(data) and data[row][i] < data[row][col]:
        partial_score += 1
        i += 1

    if i < len(data):
        partial_score += 1

    score *= partial_score

    if score == 0:
        return 0

    # seen from left
    partial_score = 0
    i = row - 1
    while i >= 0 and data[i][col] < data[row][col]:
        partial_score += 1
        i -= 1

    if i > 0:
        partial_score += 1

    score *= partial_score

    if score == 0:
        return 0

    # seen from right
    partial_score = 0
    i = row + 1
    while i < len(data[0]) and data[i][col] < data[row][col]:
        partial_score += 1
        i += 1

    if i < len(data[0]):
        partial_score += 1

    score *= partial_score

    if score == 0:
        return 0

    return score

def first_star(data: List[List[str]]):
    final_sum = 0
    for i, row in enumerate(data):
        for j, hight in enumerate(row):
            if is_seen(data, i, j):
                final_sum += 1
    return final_sum

def second_star(data: List[List[str]]):
    max_score = 0
    for i, row in enumerate(data):
        for j, hight in enumerate(row):
            max_score = max(max_score, scenic_score(data, i, j))

    return max_score

print(second_star(matriz))