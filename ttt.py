import random


#GLOBAL VARIABLE
ttt = [[1,2,3],[4,5,6],[7,8,9]]

#PRINTING THE BOARD FUNCTION
def printing():
    print()
    for i , j in enumerate(ttt):
        if i > 0:
            print('---------')
        print(j[0],'|',j[1],'|',j[2])
    print()

#RESET THE BOARD
## WITH THIS FUNCTION THE USER CAN RESET BOARD TO PLAY AGAIN
## THIS FUNCTION WORKS FILLING THE LIST IN ORDER FROM ONE TO NINE 
def reset_board():
    nav1 , nav2 , cnt = 0 , 0 , 1
    while nav1 < 3:
        while nav2 < 3:
            if ttt[nav1][nav2] != cnt:
                ttt[nav1][nav2] = cnt
            cnt += 1
            nav2 +=1
        nav2 = 0
        nav1 +=1

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
    return False
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
    return False
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
    return False

###THIS FUNCTION IS TO AVOID REPEATING THE SAME CONSULT IN ALL OF THE WINNING METHODS
def win_declaretion(nav1,nav2):
    if ttt[nav1][nav2] == 'x':
        return 'you win'
    elif ttt[nav1][nav2] == 'o':
        return 'you lose'


#USER OPTION
def selection(opt):
    nav1 , nav2 = 0 , 0
    while nav1 < 3:
        while nav2 < 3:
            if opt == ttt[nav1][nav2]:
                ttt[nav1][nav2] = 'x'
                find = True
                return find
            else:
                find = False
            nav2 += 1
        nav2 = 0
        nav1 += 1
    return find
#THIS FUNCTION WILL SELECT RANDOMLY A OPTION FOR THE CPU
##WITHOUT THE METHODS OF WINNING IN THE MAIN FUNCTION THE GAME WILL CRASH
##BECAUSE AT THE END IT WILL ENTER IN A INFINITE LOOP LOOKING FOR A AVAILABLE SPOT
def cpu_option():
    while True:
        nav1 , nav2 = 0 , 0
        cpu_opt = random.randint(1,9)
        while nav1 < 3:
            while nav2 < 3:
                if cpu_opt == ttt[nav1][nav2]:
                    ttt[nav1][nav2] = 'o'
                    find = True
                    return find
                nav2 += 1
            nav2 = 0
            nav1 += 1

def end_game(final):
    if final == 'you win':
        print('congratulations you win!')
        return True
    elif final == 'you lose':
        print('how sad, you lose :(')
        return True


if __name__ == "__main__":
    on = True
    flag = False
    while on:
        printing()
        option = int(input('Select a spot of the board: '))
        while not selection(option):
            print('that spot is occupied')
            printing()
            option = int(input('Select a spot of the board: '))
        if not flag:
            flag = winning_row()
        if not flag:
            flag = winning_column()
        if not flag: 
            flag = winning_diagonal()
        if flag:
            printing()
            end_game(flag)
            on = False

        cpu_option()