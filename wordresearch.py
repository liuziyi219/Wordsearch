def exist(board,word):
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j]==word[0]:
                board[i][j]="no"
                if findnext(i,j,word[1:]):
                    return True
    return False
def findnext(i,j,str):
    if len(str)==0:
        return True
    if nboard[i][j+1]==str[0]:  #right
        nboard[i][j+1]="no"
        if findnext(i,j+1,str[1:]):
            return True
    if nboard[i][j-1]==str[0]: #left
        nboard[i][j-1]="no"
        if findnext(i,j-1,str[1:]):
            return True
    if nboard[i+1][j]==str[0]: #down
        nboard[i+1][j]="no"
        if findnext(i+1,j,str[1:]):
            return True
    if nboard[i-1][j]==str[0]: #up
        nboard[i-1][j]="no"
        if findnext(i-1,j,str[1:]):
            return True
    return False
        

if __name__ == '__main__':
    board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

    nboard=[[0]*(len(board[0])+2) for _ in range(len(board)+2)]
    for m in range(1,len(board)+1):
        for n in range(1,len(board[0])+1):
                       nboard[m][n]=board[m-1][n-1]
    word = "ABCB"
    print(exist(nboard,word))
