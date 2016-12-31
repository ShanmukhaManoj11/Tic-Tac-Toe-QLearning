class Board:
    #initial tiles with 0
    #X->1, O->2
    def __init__(self):
        self.board=[[0,0,0],[0,0,0],[0,0,0]]           
    def update(self,pos,mark):
        assert(mark==1 or mark==2)
        assert(self.board[pos[0]][pos[1]]==0)
        self.board[pos[0]][pos[1]]=mark
    def possible_moves(self):
        moves=[]
        for i in xrange(3):
            for j in xrange(3):
                if self.board[i][j]==0:
                    moves.append((i,j))
        return moves
    def get_winner(self):
        #rows
        for i in xrange(3):
            mark=self.board[i][0]
            if mark==0:
                continue
            elif self.board[i][1]==mark and self.board[i][2]==mark:
                return mark
        #columns
        for i in xrange(3):
            mark=self.board[0][i]
            if mark==0:
                continue
            elif self.board[1][i]==mark and self.board[2][i]==mark:
                return mark
        #diagonals
        mark=self.board[0][0]
        if mark!=0 and self.board[1][1]==mark and self.board[2][2]==mark:
            return mark
        mark=self.board[0][2]
        if mark!=0 and self.board[1][1]==mark and self.board[2][0]==mark:
            return mark
        #if draw
        return 0
    def is_game_over(self):
        if len(self.possible_moves())==0:
            return True
        if self.get_winner():
            return True
        return False
    def reset(self):
        self.board=[[0,0,0],[0,0,0],[0,0,0]]
    def __str__(self):
        return str(self.board[0])+'\n'+str(self.board[1])+'\n'+str(self.board[2])+'\n'
