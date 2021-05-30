from random import shuffle


def check_game_no_diagonals(positions):
    rows = {
        1: [1, 2, 3],
        2: [4, 5, 6],
        3: [7, 8, 9]
    }
    columns = {
        1: [1, 4, 7],
        2: [2, 5, 8],
        3: [3, 6, 9]
    }
    checker = {
        1: rows,
        2: columns
    }
    for r in range(1, 3):
        x = o = 0
        for t in range(1, 4):
            trying = checker[r]
            for i in trying[t]:
                if positions[i] == 'X':
                    x = x + 1
                elif positions[i] == 'O':
                    o = o + 1
            if x == 3 or o == 3:
                return False


def check_game_diagonal(positions):
    x = o = 0
    diagonals = {
        1: [1, 5, 9],
        2: [3, 5, 7]
    }
    for k in range(1, 3):
        for s in diagonals[k]:
            x = o = 0
            if positions[s] == 'X':
                x = x + 1
            elif positions[s] == 'O':
                o = o + 1
        if x == 3 or o == 3:
            return False


def if_center_taken(available_positions, taken_positions, game):
    try:
        corners = [1, 3, 7, 9]
        for x in taken_positions:
            if x in corners:
                corners.remove(x)
        shuffle(corners)
        return corners[0]
    except IndexError:
        if game:
            shuffle(available_positions)
            return available_positions[0]


def if_center_not_taken(available_positions, positions):
    if positions[5] == ' ':
        positions[5] = 'O'
        return positions[5]
    else:
        shuffle(available_positions)
        return available_positions[0]
