from typing import List, Tuple

from getdata import getdata

content = getdata.getdata('day15')
content = getdata.separarPorLineas(content)


def parse_data(data: List[str]):
    for line in data:
        line = line.replace('Sensor at x=', '')
        line = line.replace(' closest beacon is at x=', '')
        splitted_lines = line.split(':')

        sensor = tuple(map(int, splitted_lines[0].split(', y=')))
        beacon = tuple(map(int, splitted_lines[1].split(', y=')))

        yield sensor, beacon


def first_star(data, solution_row=10):
    intervals = []

    beacon_in_solution_row = False

    for sensor, beacon in data:
        if beacon[1] == solution_row:
            beacon_in_solution_row = True

        manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        if sensor[1] - manhattan_distance <= solution_row <= sensor[1] + manhattan_distance:
            horizontal_distance_left = manhattan_distance - abs(solution_row - sensor[1])

            left_margin = sensor[0] - horizontal_distance_left

            right_margin = sensor[0] + horizontal_distance_left + 1
            intervals.append((left_margin, right_margin))

    intervals.sort()

    joint_interval = []

    for left, right in intervals:
        if not joint_interval:
            joint_interval.append((left, right))
            continue

        if joint_interval[-1][1] < left:
            joint_interval.append((left, right))
        else:
            joint_interval[-1] = (joint_interval[-1][0], max(joint_interval[-1][1], right))

    if beacon_in_solution_row:
        return joint_interval[-1][1] - joint_interval[-1][0] - 1
    else:
        return joint_interval[-1][1] - joint_interval[-1][0]


def second_star(data):
    y = 0
    set_of_no_possible = set()

    for i in range(4000000):
        print(i)
        intervals = []

        for sensor, beacon in data:

            manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

            if sensor[1] - manhattan_distance <= i <= sensor[1] + manhattan_distance:
                horizontal_distance_left = manhattan_distance - abs(i - sensor[1])

                left_margin = sensor[0] - horizontal_distance_left

                right_margin = sensor[0] + horizontal_distance_left + 1
                intervals.append((left_margin, right_margin))

        intervals.sort()

        joint_interval = tuple()

        for left, right in intervals:
            if not joint_interval:
                joint_interval = (left, right)
                continue

            if joint_interval[1] < left:
                print(joint_interval)
                return joint_interval[1] * 4000000 + i
            else:
                joint_interval = (joint_interval[0], max(joint_interval[1], right))


data = list(parse_data(content))
print(second_star(data))