#GLOBAL VARIABLE
ttt = [[1,'x',3],[4,'x',6],[7,'x',9]]

#PRINTING THE BOARD FUNCTION
def printing():
    print()
    for i , j in enumerate(ttt):
        if i > 0:
            print('---------')
        print(j[0],'|',j[1],'|',j[2])
    print()

#WINNING METHODS
##THIS FUNCTION WILL DETECT IF ARE A MATCH OF THREE X OR O IN A ROW
def winning_row():
    for i in ttt:
        cnt = 0
        aux = i[0]
        for j in i:
            if aux == j:
                cnt += 1
            if cnt == 3 and aux == 'x':
                return 'you win'
            elif cnt == 3 and aux == 'o':
                return 'you lose'
    return 'none'
##THIS FUNCTION WILL DETECT IF ARE A MATCH OF THREE X OR O IN A COLUMN
def winning_column():
    nav1 , nav2 , cnt = 0 , 0 , 0
    while nav2 < 3:
        while nav1 < 2:
            if ttt[nav1][nav2] == ttt[nav1 + 1][nav2]:
                nav1 += 1
                cnt += 1
                if cnt == 2:
                    return win_declaretion(nav1,nav2)
            else:
                nav1 = 0
                break
        nav2 += 1
    return 'none'
##THIS FUNCTION WILL DETECT IF ARE A MATCH OF THREE X OR O IN A DIAGONAL
def winning_diagonal():
    nav1,nav2,cnt = 0,0,0
    while nav1 < 2 and nav2 < 2:
        if ttt[nav1][nav2] == ttt[nav1 + 1][nav2 + 1]:
            cnt += 1
            nav1 += 1
            nav2 += 1
            if cnt == 2:
                return win_declaretion(nav1,nav2)
        else:
            nav1 = 0
            nav2 = len(ttt[nav1]) - 1
            break
    while True:
        if ttt[nav1][nav2] == ttt[nav1 + 1][nav2 - 1]:
            cnt += 1
            nav1 += 1
            nav2 -= 1
            if cnt == 2:
                return win_declaretion(nav1,nav2)
        else:
            break
    return 'none'
###THIS FUNCTION IS TO AVOID REPEATING THE SAME CONSULT IN ALL OF THE WINNING METHODS
def win_declaretion(nav1,nav2):
    if ttt[nav1][nav2] == 'x':
        return 'you win'
    elif ttt[nav1][nav2] == 'o':
        return 'you lose'




if __name__ == "__main__":
    print(winning_column())
