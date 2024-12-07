import copy
def possible_moves(field: list[str], fig: list[str], player:int) -> set[tuple[int, int]]:
    '''
    finds all of the free spaces on the board
    '''
    possible_cords = set()

    friend_fig = 'o' if player == 1 else 'x'

    h_fig = len(fig)
    w_fig = len(fig[0])

    height_f = len(field)
    width_f = len(field[0])

    free_spaces = set()
    fig_spaces = set()
    for y, row in enumerate(field):
        for x, column in enumerate(row):
            if column == '.':
                free_spaces.add((y, x))
            elif column.lower() == friend_fig:
                fig_spaces.add((y, x))

    for field_y in range(height_f - h_fig + 1):
        for field_x in range(width_f - w_fig + 1):

            fig_stars = set()
            for y_fig in range(h_fig):
                for x_fig in range(w_fig):
                    if fig[y_fig][x_fig] == '*':
                        fig_stars.add((y_fig + field_y, x_fig + field_x))
            if len(fig_stars & fig_spaces) == 1:
                possible_cords.add((field_y, field_x))


    return possible_cords


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    figure = [
        '...*.', 
        '..**.', 
        '.**.*', 
        '..***'
        ]
    field = [
        '........................................',
        '........................................',
        '........................................',
        '...OO...................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '.................................XX.....',
        '................................XX......',
        '................................X.......',
        '........................................',
        '........................................',
        '........................................',
        '........................................'
        ]
    move = None
    h_field, w_field = len(field), len(field[0])

    print(f'Field: {h_field}, {w_field}')
    h_fig, w_fig = len(figure), len(figure[0])
    print(f'piece info {h_fig}, {w_fig}, {figure}')
    result = possible_moves(field, figure, player)

    for j, row in enumerate(figure):
        fig_x, fig_y = j, row.lower().find("*")

    if move is None:
        for i, row in enumerate(field):
            c = row.lower().find("o" if player == 1 else "x")
            if c != -1:
                print(f'x: {c}, y: {i}')
                move = i-fig_x, c-fig_y
                break
                # move = i - 1, c - 4
    assert move is not None
    print(f'Full field: {field}')
    print(f'MOVE_MOVE: {move}')
    return move

step(1)
