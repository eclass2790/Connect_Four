from connectfour import *
from player import *
from minimax import *

def play_game(board, player1, player2):
    """
    Alternates calling play_turn for players 1 and 2.  In between moves, checks for a winning
    board position.  If a winning position is found, prints a message saying who is the winner
    and returns.
    """
    while True:
        player1.play_turn(board)
        w = board.is_game_over()
        if w != None:
            print "Congradulations Player %i, you won!" % w
            return

        player2.play_turn(board)
        w = board.is_game_over()
        if w != None:
            print "Congradulations Player %i, you won!" % w
            return

board = ConnectFour()
p1 = Human(playernum=1)
p2 = MinimaxPlayer(playernum=2, ply_depth=4, utility=SimpleUtility(1, 5))
#p1 = MinimaxPlayer(playernum=1, ply_depth=3, utility=SimpleUtility(1, 5))
#p2 = MinimaxPlayer(playernum=2, ply_depth=2, utility=WithColumnUtility(5, 10, [1, 2, 3, 4, 3, 2, 1]))
play_game(board, p1, p2)
board.print_board()
