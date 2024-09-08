# def win_checker(player, grid):


def main():
    tuple1 = (1,0,1,1,0,0,1,1,0)
    # x o x
    # x o o
    # x x o
    # columns:
    # 0, 3, 6
    # 1, 4, 7
    # 2, 5, 8
    # rows:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    # diagonals:
    # 0, 4, 8
    # 2, 4, 6

    column_win1 = tuple1[0] == tuple1[3] == tuple1[6]
    column_win2 = tuple1[1] == tuple1[4] == tuple1[7]
    column_win3 = tuple1[2] == tuple1[5] == tuple1[8]

    # for i in range(3):
    #     for j in range(i,len(tuple1),3):
    #         print(tuple1[j])

    row_win1 = tuple1[0] == tuple1[1] == tuple1[2]
    row_win2 = tuple1[3] == tuple1[4] == tuple1[5]
    row_win3 = tuple1[6] == tuple1[7] == tuple1[8]

    diagonal_win1 = tuple1[0] == tuple1[4] == tuple1[8]
    diagonal_win2 = tuple1[2] == tuple1[4] == tuple1[6]


    # horizontalwin = tuple1[0] == tuple1[1] == tuple1[2]
    # diagonalwin1 = tuple1[0] == tuple1[4] == tuple1[8]
    # diagonalwin2 = tuple1[2] == tuple1[4] == tuple1[6]

    # for i in tuple1:




    return


main()
