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

if __name__ == "__main__":
    print(winning_row())
