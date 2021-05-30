import ttc_tactics

game = True
positions = {
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' '
}
rows = {
    1: [1, 2, 3],
    2: [4, 5, 6],
    3: [7, 8, 9]
}
taken_positions = []
available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f' 1 | 2 | 3\n---|---|---\n'
      f' 4 | 5 | 6\n---|---|---\n'
      f' 7 | 8 | 9')

for moves in range(1, 6):
    move = int(input('Choose a position: '))
    if positions[move] == ' ':
        positions[move] = 'X'
        taken_positions.append(move)
        available_positions.remove(move)
    elif positions[move] == 'X' or positions[move] == 'O':
        new_move = move
        while positions[new_move] != ' ':
            new_move = int(input('Please choose a new position. This one is already taken. '))
            if positions[new_move] == ' ':
                positions[new_move] = 'X'
                taken_positions.append(new_move)
                available_positions.remove(new_move)
                break
    print(
        f' {positions[1]} | {positions[2]} | {positions[3]}\n---|---|---\n'
        f' {positions[4]} | {positions[5]} | {positions[6]}\n---|---|---\n'
        f' {positions[7]} | {positions[8]} | {positions[9]}')
    print("You've played!\n")
    game1 = ttc_tactics.check_game_no_diagonals(positions)
    game2 = ttc_tactics.check_game_diagonal(positions)
    if game1 is None or game2 is None:
        game1 = game2 = True
    if not game1 or not game2:
        play_again = input('Game has ended! Would you like to play again? y/n ')
        if play_again == 'n':
            print('Ok!')
            break

    if positions[5] == 'X':
        comp_position = ttc_tactics.if_center_taken(available_positions, taken_positions, game)
        positions[comp_position] = 'O'
        taken_positions.append(comp_position)
        try:
            available_positions.remove(comp_position)
        except ValueError:
            pass
    else:
        comp_position = ttc_tactics.if_center_not_taken(available_positions, positions)
        positions[comp_position] = 'O'
        taken_positions.append(comp_position)
        try:
            available_positions.remove(comp_position)
        except ValueError:
            pass
    print(
        f' {positions[1]} | {positions[2]} | {positions[3]}\n---|---|---\n'
        f' {positions[4]} | {positions[5]} | {positions[6]}\n---|---|---\n'
        f' {positions[7]} | {positions[8]} | {positions[9]}')
    print('Computer has played!\n')
