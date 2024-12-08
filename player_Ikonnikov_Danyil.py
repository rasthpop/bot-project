#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from logging import DEBUG, debug, getLogger
import math


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    field_info = input()[:-1].split()
    return int(field_info[1])


def parse_field(height: int):
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowecase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:
    перша строка відкидається
    відкинути перші 4 символи в кожн рядку
    for i in range height
    return матрицю
        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player int: Represents whether we're the first or second player
    """
    _ = input()
    field = []
    for _ in range(height):
        field += [list(input()[4:])]
    return field


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 3 2:
    **
    ..
    ..
    """
    figure = []
    h = int(input().split()[1])
    for _ in range(h):
        figure += [list(input())]
    return figure


def valid_placement(field: list, figure: list, coords: tuple, friendly: str, enemy: str):
    """
    Check if the figure can be placed at the given coordinates without leaving the field.
    """
    x, y = coords
    figure_height = len(figure)
    figure_width = max(len(row) for row in figure)
    allied_overlap = 0

    for i in range(figure_height):
        for j in range(figure_width):
            if x + i >= len(field) or y + j >= len(field[0]):
                return False
            if figure[i][j] == '*':
                if field[x + i][y + j] == friendly:
                    allied_overlap += 1
                if field[x + i][y + j] == enemy or allied_overlap > 1:
                    return False
    if allied_overlap == 0:
        return False
    return True


def compute_move(player: int, field: list, figure: list):
    """
    Compute the next move for the player.
    """
    friendly_fig = 'O' if player == 1 else 'X'
    enemy_fig = 'X' if player == 1 else 'O'

    min_distance = float('inf')
    min_distance_coords = None

    enemy_cells = []
    vacant_cells = []

    for i, _ in enumerate(field):
        for j, _ in enumerate(field[0]):
            if field[i][j] == enemy_fig:
                enemy_cells.append((i, j))
            if valid_placement(field, figure, (i, j), friendly_fig, enemy_fig):
                vacant_cells.append((i, j))

    for free_coords in vacant_cells:
        for enemy_coords in enemy_cells:
            distance = math.sqrt((free_coords[0] - enemy_coords[0]) ** 2 + \
(free_coords[1] - enemy_coords[1]) ** 2)
            if distance < min_distance:
                min_distance = distance
                min_distance_coords = free_coords

    return min_distance_coords


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    height = parse_field_info()
    field = parse_field(height)
    figure = parse_figure()
    move = compute_move(player, field, figure)

    return move


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
