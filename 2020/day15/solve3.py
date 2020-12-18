import collections
from collections import deque

import parse

from utils import *


def convert_to_coords(data):

    goblins = []
    elves = []
    elements = {}

    for i, line in enumerate(data):
        for j, cell in enumerate(line):
            if cell == '#':
                elements[(i, j)] = '#'

            elif cell == 'G':
                goblins.append([i, j, 200, 'G'])
                elements[(i, j)] = 'G'

            elif cell == 'E':
                elves.append([i, j, 200, 'E'])
                elements[(i, j)] = 'E'

    return goblins, elves, elements


def find_closest_target(coords, target, elements):
    previous_move = {}
    distance = {}

    to_visit = deque()
    for incr in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        coords_ = (coords[0] + incr[0], coords[1] + incr[1])
        to_visit.append(coords_)
        previous_move[coords_] = tuple(coords)
        distance[coords_] = 1

    closest = None
    while len(to_visit) > 0:

        new_coords = to_visit.popleft()

        if elements.get(new_coords) == target:
            closest = new_coords
            break

        if new_coords in elements:
            continue

        for incr in [(-1, 0), (0, -1), (0, 1), (1, 0)]:

            coords_ = (new_coords[0] + incr[0], new_coords[1] + incr[1])
            if coords_ not in previous_move:
                previous_move[coords_] = new_coords
                distance[coords_] = distance[new_coords] + 1

                to_visit.append(coords_)

    if closest is None:
        return None, None, None

    position = closest
    next_move = previous_move[closest]
    while next_move != tuple(coords):
        position = next_move
        next_move = previous_move[position]

    return closest, position, distance[closest]


def move_once(fighter, elements):
    if fighter[3] == 'E':
        target = 'G'
    else:
        target = 'E'
    closest, next_coords, distance = find_closest_target(
        fighter[:2], target, elements
    )

    if next_coords is None:
        return

    if distance < 2:
        return

    old = elements.pop((fighter[0], fighter[1]))

    fighter[0] = next_coords[0]
    fighter[1] = next_coords[1]
    elements[(fighter[0], fighter[1])] = old


def select_target(fighter, goblins, elves):
    if fighter[3] == 'E':
        targets = goblins
    elif fighter[3] == 'G':
        targets = elves

    min_hit_score = 201
    low = None

    for coords in [
        (fighter[0] - 1, fighter[1]),
        (fighter[0], fighter[1] - 1),
        (fighter[0], fighter[1] + 1),
        (fighter[0] + 1, fighter[1]),
    ]:
        for target in targets:
            if (
                tuple(target[:2]) == coords
                and target[2] > 0
                and target[2] < min_hit_score
            ):
                min_hit_score = target[2]
                low = target

    return low


def play_one_round(goblins, elves, elements, elf_attack=3):
    fighters = sorted(goblins + elves)

    for fighter in fighters:
        # If someone died during this round, ignore him
        if fighter[2] <= 0:
            continue

        move_once(fighter, elements)
        target = select_target(fighter, goblins, elves)
        if target:
            if fighter[3] == 'E':
                target[2] -= elf_attack
            else:
                target[2] -= 3

            # If the target died, remove him from the map
            if target[2] <= 0:
                del elements[(target[0], target[1])]

    # After a round, remove dead fighters from the lists
    goblins = [goblin for goblin in goblins if goblin[2] > 0]
    elves = [elf for elf in elves if elf[2] > 0]
    return goblins, elves, elements


def show_map(goblins, elves, elements):
    max_line = max(coord[0] for coord in elements.keys())
    max_column = max(coord[1] for coord in elements.keys())

    for i in range(max_line + 1):
        print(''.join(elements.get((i, j), '.') for j in range(max_column + 1)))

    print('Goblins', len(goblins), goblins)
    print('Elves', len(elves), elves)


def part1(data, elf_attack=3):
    goblins, elves, elements = convert_to_coords(data)
    show_map(goblins, elves, elements)

    round_ = 0
    while len(goblins) > 0 and len(elves) > 0:
        goblins, elves, elements = play_one_round(
            goblins, elves, elements, elf_attack
        )
        round_ += 1
        print('-' * 30)
        print('Round', round_)
        show_map(goblins, elves, elements)

    return (round_ - 1) * sum(fighter[2] for fighter in goblins + elves)


def part2(data):
    goblins, elves, elements = convert_to_coords(data)
    show_map(goblins, elves, elements)

    elf_count = len(elves)

    elf_attack = 4
    while True:
        goblins, elves, elements = convert_to_coords(data)
        round_ = 0
        while len(goblins) > 0 and len(elves) == elf_count:
            goblins, elves, elements = play_one_round(
                goblins, elves, elements, elf_attack=elf_attack
            )
            round_ += 1
        if elf_count == len(elves):
            return (
                elf_attack,
                round_ - 1,
                (round_ - 1) * sum(fighter[2] for fighter in goblins + elves),
            )

        print(
            'Trying',
            elf_attack,
            len(elves),
            elf_count,
            round_,
            round_ * elf_attack,
        )
        elf_attack += 1


s = input()
data_real = []
while s != "done":
    data_real.append(s)
    s = input()

print('Solution of 1 is', part1(data_real))
print('Solution of 2 is', part2(data_real))

# 215496
# 193140
# 193464
# 190777


# 20
# 19