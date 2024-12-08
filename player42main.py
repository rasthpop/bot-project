#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
"""
import math
from logging import DEBUG, debug, getLogger

# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can hovever do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    l = input()
    _, height, width = l.split()
    height = int(height)
    width = int(width.rstrip(':'))
    return height, width
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
    move = None
    _ = input()
    field = []
    for i in range(height):

        l = input()
        debug(f"Field: {l}")
        field.append(l[4:])
    return field


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    l = input().split()

    height, width = int(l[1]), int(l[2][:-1])
    figure = []
    for _ in range(height):
        l = input()
        figure.append(l)
    return height, width, figure

def possible_moves(field: list[str], fig: list[str], player:int) -> set[tuple[int, int]]:
    '''
    finds all of the free spaces on the board
    '''
    possible_cords = set()

    h_fig = len(fig)
    w_fig = len(fig[0])

    fig_spaces = set()
    enemy_spaces = set()
    for y, row in enumerate(field):
        for x, column in enumerate(row):
            if column.lower() == 'o' if player == 1 else column.lower() == 'x':
                fig_spaces.add((y, x))
            elif column.lower() == 'x' if player == 1 else column.lower() == 'o':
                enemy_spaces.add((y, x))

    for field_y in range(len(field) - h_fig + 1):
        for field_x in range(len(field[0]) - w_fig + 1):

            fig_stars = set()
            for y_fig in range(h_fig):
                for x_fig in range(w_fig):
                    if fig[y_fig][x_fig] == '*':
                        fig_stars.add((y_fig + field_y, x_fig + field_x))
            if len(fig_stars & fig_spaces) == 1 and len(fig_stars & enemy_spaces) == 0:
                possible_cords.add((field_y, field_x))

    return (possible_cords, enemy_spaces)

def shortest_distance(moves_enemy: tuple[set[tuple[int, int]], set[tuple[int, int]]]):
    '''finds the best move to place a figure closest to the enemy'''
    def calculate_path(y1:int, x1:int, y2:int, x2:int):
        '''calculates the shortest path between two points'''
        return math.sqrt(((x1 - x2) ** 2) + (y1 - y2)** 2)

    distance_min = math.inf
    res = ''

    for move in moves_enemy[0]:
        for point in moves_enemy[1]:
            distance = calculate_path(move[0], move[1], point[0], point[1])
            if distance < distance_min:
                distance_min = distance
                res = move
    return res

def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """

    move = None
    h_field, w_field = parse_field_info()

    debug(f'Field: {h_field}, {w_field}')
    field = parse_field(h_field)
    h_fig, w_fig, figure = parse_figure()
    debug(f'piece info {h_fig}, {w_fig}, {figure}')
    pos_move = shortest_distance(possible_moves(field, figure, player))
    # pos_move = possible_moves(field, figure, player).pop()
    if move is None:
        move = pos_move
    assert move is not None
    debug(f'Full field: {field}')
    debug(f'MOVE_MOVE: {move}')
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
    Повертає номер гравця
    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
