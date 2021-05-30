positions = []
x_winner, o_winner = False, False
for _ in range(9):
    positions.append(' ')
coordinates = (['1', '1'], ['1', '2'], ['1', '3'],
               ['2', '1'], ['2', '2'], ['2', '3'],
               ['3', '1'], ['3', '2'], ['3', '3'])
print(f'''---------
| {positions[0]} {positions[1]} {positions[2]} |
| {positions[3]} {positions[4]} {positions[5]} |
| {positions[6]} {positions[7]} {positions[8]} |
---------''')
move = 0
while True:
    player_move = input('Enter position: ')
    player_move = player_move.split()
    if player_move not in coordinates:
        if len(player_move[0]) != 1 or len(player_move[1]) != 1:
            print('You should enter numbers!')
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        for a in range(9):
            if player_move == coordinates[a]:
                if positions[a] != ' ':
                    print('This cell is occupied! Choose another one!')
                    break
                else:
                    if move % 2 == 0:
                        positions[a] = 'X'
                    else:
                        positions[a] = 'O'
                    move += 1
                    print(f'''---------
| {positions[0]} {positions[1]} {positions[2]} |
| {positions[3]} {positions[4]} {positions[5]} |
| {positions[6]} {positions[7]} {positions[8]} |
---------''')
    lines = [[positions[0], positions[1], positions[2]],
             [positions[3], positions[4], positions[5]],
             [positions[6], positions[7], positions[8]],
             [positions[0], positions[3], positions[6]],
             [positions[1], positions[4], positions[7]],
             [positions[2], positions[5], positions[8]],
             [positions[0], positions[4], positions[8]],
             [positions[2], positions[4], positions[6]]]
    for i in range(8):
        if lines[i].count("X") == 3:
            x_winner = True
        elif lines[i].count("O") == 3:
            o_winner = True
    if x_winner:
        print("X wins")
        break
    elif o_winner:
        print("O wins")
        break
    elif ' ' not in positions:
        print('Draw')
        break
