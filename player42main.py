#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

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

    debug(f"Description of the field: {l}")
    _, height, width = l.split()
    height = int(height)
    width = int(width.rstrip(':'))
    # debug(f'{height} {width}')
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
    #     if move is None:
    #         c = l.lower().find("o" if player == 1 else "x")
    #         if c != -1:
    #             move = i - 1, c - 4
    # assert move is not None
    # debug(f'Full field: {field}')
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
    # debug(f"Piece: {l}")
    height, width = int(l[1]), int(l[2][:-1])
    figure = []
    for _ in range(height):
        l = input()
        # debug(f"Piece: {l}")
        figure.append(l)
    return height, width, figure

def possible_moves(field: list[str]) -> set[tuple[int, int]]:
    '''
    finds all of the free spaces on the board
    '''
    free_spaces = set()
    for x, row in enumerate(field):
        for y, column in enumerate(row):
            if column == '.':
                free_spaces.add(x, y)



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

    for j, row in enumerate(figure):
        fig_x, fig_y = j, row.lower().find("*")

    if move is None:
        for i, row in enumerate(field):
            c = row.lower().find("o" if player == 1 else "x")
            if c != -1:
                debug(f'c: {c}')
                move = i-fig_x, c-fig_y
                break
                # move = i - 1, c - 4
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
