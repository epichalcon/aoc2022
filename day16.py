import re
from dataclasses import dataclass

from getdata import getdata
import networkx as nx
import matplotlib.pyplot as plt

content = getdata.getdata('day16')
content = getdata.separarPorLineas(content)


class GraphVisualization:
    def __init__(self):
        self.visual = []

    nodes = []

    def addEdge(self, a, b):
        for node in b:
            temp = [a, node]
            self.visual.append(temp)


    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G, with_labels=True, node_color='green', node_size=5, font_size=10, font_color='black')
        plt.show()


@dataclass
class Valve:
    name: str
    flowrate: int
    tunnels: list

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def __hash__(self):
        return ord(self.name[0]) + ord(self.name[1])


def parse_data(data):
    for line in data:
        line = re.split('; tunnels? leads? to valves? ', line)
        valve = line[0].replace('Valve ', '').split(' has flow rate=')[0]
        flowrate = line[0].replace('Valve ', '').split(' has flow rate=')[1]
        tunnels = line[1].split(', ')

        yield valve, flowrate, tunnels






def shortest_paths(valves):
    matrix = [[float('inf') for j, _ in enumerate(valves)] for i, _ in enumerate(valves)]

    for i, valve_row in enumerate(valves):
        for j, valve_col in enumerate(valves):
            if i == j:
                matrix[i][j] = 0
                continue

            if valve_col in valves[valve_row].tunnels:
                matrix[i][j] = 1

    for k, _ in enumerate(valves):
        for i, _ in enumerate(valves):
            colum_value = matrix[k][i]
            if colum_value == float('inf'):
                continue
            for j, _ in enumerate(valves):
                row_value = matrix[k][j]
                if row_value == float('inf'):
                    continue

                combination_value = matrix[i][j]
                matrix[i][j] = min(combination_value, colum_value + row_value)

    shortest_path = {}

    for i, valve_row in enumerate(valves.keys()):
        current_paths = {}
        for j, valve_col in enumerate(valves.keys()):
            current_paths[valve_col] = matrix[i][j]

        shortest_path[valve_row] = current_paths

    return shortest_path

def dfs2(valve, time_left, pressure_released, visited_valves: set):
    best_path = []

    visited_valves.add(valve)

    if time_left <= 0:
        best_path = [valve]
        return pressure_released, best_path

    best_pressure = 0

    for next_valve in valves_with_presure:
        if valves[next_valve] in visited_valves:
            continue

        next_time = time_left - shortest_paths_dict[valve.name][next_valve] -1

        preasure, path = dfs2(valves[next_valve], next_time , pressure_released + valves[next_valve].flowrate * next_time, visited_valves.copy())

        if best_pressure < preasure:
            best_pressure = preasure
            best_path = path.copy()

    pressure_released = max(pressure_released, best_pressure)

    best_path.append(valve)
    return pressure_released, best_path


def dfs(valve, time_left, pressure_released, visited_valves: set):
    best_preasure = 0
    best_path = []

    # you open valve XX
    time_left, pressure_released = pass_time(1, time_left, pressure_released, visited_valves)
    visited_valves.add(valve)

    # if the time has finished return the pressure
    if time_left <= 0:
        best_path = [valve]
        return pressure_released, best_path

    # if we have opened all the valves
    if len(visited_valves) - 1 == len(valves_with_presure):
        time_left, pressure_released = pass_time(time_left, time_left, pressure_released, visited_valves)
        best_path = [valve]
        return pressure_released, best_path


    # for every valve we havent visited
    for next_valve in valves_with_presure:
        if valves[next_valve] in visited_valves:
            continue


        # we move to the valve
        prov_time_left, prov_pressure_released = pass_time(shortest_paths_dict[valve.name][next_valve], time_left,
                                                           pressure_released, visited_valves)

        if prov_time_left == 0:
            best_path.append(valve)
            return prov_pressure_released, best_path

        preasure, path = dfs(valves[next_valve], prov_time_left, prov_pressure_released, visited_valves.copy())

        if preasure > best_preasure:
            best_preasure = preasure
            best_path = path.copy()

    '''
        best_preasure = max(preasure, best_preasure)
        if best_preasure == preasure:
            best_path = path.copy()
    '''

    best_path.append(valve)

    return best_preasure, best_path

def pass_time(time_steps, time_left, pressure_released, valves_opened):
    for i in range(time_steps):
        time_left -= 1
        for opened_valve in valves_opened:
            pressure_released += opened_valve.flowrate
        if time_left == 0:
            break


    return time_left, pressure_released

def first_star(valves):
    return dfs2(valves['AA'], 30, 0, set())


G = GraphVisualization()

valves = {}
valves_with_presure = set()
for valve, flowrate, tunnels in parse_data(content):
    valves[valve] = Valve(valve, int(flowrate), tunnels)
    G.addEdge(valve, tunnels)
    if int(flowrate) != 0:
        valves_with_presure.add(valve)

G.visualize()

shortest_paths_dict = shortest_paths(valves)


print(first_star(valves))