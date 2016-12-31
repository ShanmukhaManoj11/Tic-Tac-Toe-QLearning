from board import Board
from player import Player
import pickle

if __name__=='__main__':
    board=Board()
    player1=Player(board,1)
    player2=Player(board,2)
    ## 
    for i in xrange(2000):
        while True:
            if board.is_game_over():
                break
            player1.random_play()
            #print board
            if board.is_game_over():
                break
            player2.random_play()
            #print board
        #print 'player '+str(board.get_winner())+' wins'
        #print '--------------------------------------'
        player1.update_Q()
        player2.update_Q()
        board.reset()
    for i in xrange(2000,4000):
        while True:
            if board.is_game_over():
                break
            player1.play(i/100)
            #print board
            if board.is_game_over():
                break
            player2.random_play()
            #print board
        #print 'player '+str(board.get_winner())+' wins'
        #print '--------------------------------------'
        player1.update_Q()
        player2.update_Q()
        board.reset()
    for i in xrange(4000,6000):
        while True:
            if board.is_game_over():
                break
            player1.random_play()
            #print board
            if board.is_game_over():
                break
            player2.play(i/100)
            #print board
        #print 'player '+str(board.get_winner())+' wins'
        #print '--------------------------------------'
        player1.update_Q()
        player2.update_Q()
        board.reset()
    for i in xrange(6000,10000):
        while True:
            if board.is_game_over():
                break
            player1.play(i/100)
            #print board
            if board.is_game_over():
                break
            player2.play(i/100)
            #print board
        #print 'player '+str(board.get_winner())+' wins'
        #print '--------------------------------------'
        player1.update_Q()
        player2.update_Q()
        board.reset()
    ##
    Q=player1.Q
    with open('Q_1','wb') as f:
        pickle.dump(Q,f,protocol=pickle.HIGHEST_PROTOCOL)
    Q=player2.Q
    with open('Q_2','wb') as f:
        pickle.dump(Q,f,protocol=pickle.HIGHEST_PROTOCOL)
