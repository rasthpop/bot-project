'''me'''
import math
def possible_moves(field: list[str], fig: list[str], player:int) -> set[tuple[int, int]]:
    '''
    finds all of the free spaces on the board
    '''
    possible_cords = set()

    # friend_fig = 'o' if player == 1 else 'x'

    h_fig = len(fig)
    w_fig = len(fig[0])

    # free_spaces = set()
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

    return possible_cords

def shortest_distance(field: list[str], moves: set[tuple[int, int]], player: int):
    '''finds the best move to place a figure closest to the enemy'''
    def calculate_path(y1:int, x1:int, y2:int, x2:int):
        '''calculates the shortest path between two points'''
        return math.sqrt(((x1 - x2) ** 2) + (y1 - y2)** 2)

    enemy_points = set()
    distance_min = math.inf
    res = ''


    for y, row in enumerate(field):
        for x, column in enumerate(row):
            if column.lower() == 'x' if player == 1 else column.lower() == 'o':
                enemy_points.add((y, x))
    for move in moves:
        distance = 0
        for point in enemy_points:
            distance += calculate_path(move[0], move[1], point[0], move[1])
        if distance < distance_min:
            distance_min = distance
            res = move

    return res

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
    field2 = ['........................................',
              '........................................',
              '........................................',
              '..OOO...................................',
              '....O...................................',
              '....OOO.................................',
              '....OO..................................',
              '....O...................................',
              '...OOOO.................................',
              '......O.................................',
              '.....OOO................................',
              '.OOOOOOOOOOOO.OOOOO.............XXX.....',
              '.OOOOOOOOOOOOOOOOOOOO...........XX......',
              '.OO.OOOOO..O...OOOOO...XXXXXXXXXXXXXX...',
              '.OOOOO...................XXXXXXXXXXXX...',
              '..........................XXXXXXXXXX....',
              '...........................XXX...X......',
              '.............................XX.........',
              '.............................XXXX.......',
              '...............................XX.......',
              '........................................',
              '........................................',
              '........................................',
              '........................................']
    move = None
    h_field, w_field = len(field), len(field[0])

    print(f'Field: {h_field}, {w_field}')
    h_fig, w_fig = len(figure), len(figure[0])
    print(f'piece info {h_fig}, {w_fig}, {figure}')
    pos_move = shortest_distance(field, possible_moves(field, figure, player), player)

    if move is None:
        move = pos_move
    assert move is not None
    print(f'Full field: {field}')
    print(f'MOVE_MOVE: {move}')
    return move

step(2)
