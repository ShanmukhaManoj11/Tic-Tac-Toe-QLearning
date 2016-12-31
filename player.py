import random

class Player:
    #id=X or O; X->1, O->2
    def __init__(self,board,mark):
        self.board=board
        self.id=mark
        self.Q={}
        self.moves=[]
        self.states=[]
        self.REWARDS=[-2,10,-10] #-2 for draw, 10 for win, -10 for loss
    def Q_value(self,s,a):
        if self.Q.get((s,a)) is None:
            self.Q[(s,a)]=0
        return self.Q[(s,a)]
    #exploiting the fact that game (X,O) w.r.t X is game (O,X) w.r.t O
    def state_wrt_id(self):
        s=[]
        for i in xrange(3):
            for j in xrange(3):
                if self.board.board[i][j]==self.id:
                    c=1
                else:
                    c=2
                if self.board.board[i][j]==0:
                    c=0
                s.append(c)
        return tuple(s)
    def random_play(self):
        s=self.state_wrt_id()
        moves=self.board.possible_moves()
        m=random.choice(moves)
        self.board.update(m,self.id)
        self.moves.append(m)
        self.states.append(s)
    def play(self,g):
        s=self.state_wrt_id()
        moves=self.board.possible_moves()
        if random.random()<0.2/(g+1):
            m=random.choice(moves)
        else:
            q=[self.Q_value(s,move) for move in moves]
            maxQ=max(q)
            if q.count(maxQ)>1:
                best_moves=[i for i in range(len(moves)) if q[i]==maxQ]
                i=random.choice(best_moves)
            else:
                i=q.index(maxQ)
            m=moves[i]
        self.board.update(m,self.id)
        self.moves.append(m)
        self.states.append(s)
    def update_Q(self):
        for i in xrange(len(self.moves)-1,-1,-1):
            s=self.states[i]
            m=self.moves[i]
            if i==len(self.moves)-1:
                winner=self.board.get_winner()
                if winner==self.id:
                    c=1
                else:
                    c=2
                if winner==0:
                    c=0
                r=self.REWARDS[c]
                q=self.Q_value(s,m)
                self.Q[(s,m)]=q+0.8*(r-q)
            else:
                r=0
                q=self.Q_value(s,m)
                s_=self.states[i+1]
                moves=[]
                for j in xrange(3):
                    for k in xrange(3):
                        if s_[3*j+k]==0:
                            moves.append((j,k))
                q_=[self.Q_value(s_,move) for move in moves]
                maxQ=max(q_)
                self.Q[(s,m)]=q+0.8*(r+0.9*maxQ-q)
        self.states=[]
        self.moves=[]
