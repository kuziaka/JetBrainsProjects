# turn test string with X_O to ['X', ' ', 'O']
field = [' ' for x in range(9)]  # creates list with X O and _
cells = [[field[x] for x in range(3)],  # it is a list of lists(rows) to enumerate and define tuple of coordinates
         [field[3 + x] for x in range(3)],
         [field[6 + x] for x in range(3)]]


# create battlefield
def battlefield():
    print("---------")
    print(f"| {cells[0][0]} {cells[0][1]} {cells[0][2]} |")
    print(f"| {cells[1][0]} {cells[1][1]} {cells[1][2]} |")
    print(f"| {cells[2][0]} {cells[2][1]} {cells[2][2]} |")
    print("---------")


# defines strings from winning sequences
def sequences():
    f = cells
    combinations = [f'{f[0][0]}{f[0][1]}{f[0][2]}', f'{f[1][0]}{f[1][1]}{f[1][2]}', f'{f[2][0]}{f[2][1]}{f[2][2]}',
                    # for rows
                    f'{f[0][0]}{f[1][0]}{f[2][0]}', f'{f[0][1]}{f[1][1]}{f[2][1]}', f'{f[0][2]}{f[1][2]}{f[2][2]}',
                    # for cols
                    f'{f[0][0]}{f[1][1]}{f[2][2]}', f'{f[0][2]}{f[1][1]}{f[2][0]}']  # for diagonals
    return combinations


# finds mistakes in test input
def test_validation():
    c = sequences()
    f = field
    if 'XXX' in c:
        return 'X'
    elif 'OOO' in c:
        return 'O'
    elif f.count('X') + f.count('O') == 9:
        return 'Draw'
    else:
        return False


# define occupied cells
def occupied_cells():
    row_index, col_index = 1, 1
    coordinates = []

    # iterate through cells creating tuples with coordinates of occupied cells
    for row in cells:
        for col in row:
            if col != ' ':
                coordinates.append((row_index, col_index))
            col_index += 1
        row_index += 1
        col_index = 1

    return coordinates


# asks and validate user coordinates input
# returns list of occupied cells coordinates
def get_coordinates():
    count = 0
    counter = 0
    while True:
        if count > 1:
            count = 0
        coordinates = input('Enter the coordinates:').split()
        row = coordinates[0]
        col = coordinates[1]
        if not row.isnumeric() or not col.isnumeric():
            print('You should enter numbers!')
        else:
            row = int(row)
            col = int(col)
            if row not in range(1, 4) or col not in range(1, 4):
                print('Coordinates should be from 1 to 3!')
            else:
                coordinates = (row, col)
                if coordinates in occupied_cells():
                    print('This cell is occupied! Choose another one!')
                else:
                    if count == 0:
                        cells[row - 1][col - 1] = 'X'
                        field[counter] = 'X'
                    else:
                        cells[row - 1][col - 1] = 'O'
                        field[counter] = 'O'
                    battlefield()
                    count += 1
                    counter += 1
                    if test_validation() in ('X', 'O'):
                        print(f'{test_validation()} wins')
                        break
                    elif test_validation() == 'Draw':
                        print('Draw')
                        break


# run the game
def main():
    battlefield()
    get_coordinates()