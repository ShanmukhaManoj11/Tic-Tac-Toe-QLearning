from player import Player
from board import Board
import pickle
import random

board=Board()
s=[]
for i in xrange(3):
    for j in xrange(3):
        s.append(board.board[i][j])

def human_play(b,f):
    m,n=input()
    if f=='human':
        b.update((m,n),1)
    else:
        b.update((m,n),2)

if __name__=='__main__':
    first_togo='human'
    if random.random()<=0.5:
        first_togo='AI'
    if first_togo=='human':
        player=Player(board,2)
        with open('Q_2','rb') as f:
            player.Q=pickle.load(f)
        while True:
            if board.is_game_over():
                break
            human_play(board,first_togo)
            print board
            if board.is_game_over():
                break
            player.play(200)
            print board
    else:
        player=Player(board,1)
        with open('Q_1','rb') as f:
            player.Q=pickle.load(f)
        while True:
            if board.is_game_over():
                break
            player.play(200)
            print board
            if board.is_game_over():
                break
            human_play(board,first_togo)
            print board
    print 'player '+str(board.get_winner())+' wins'
