from connectfour import *
from player import *
from minimax import *
from Tkinter import *
import tkMessageBox 

class MazeGui:
    def __init__(self, root, board, cell_size = 100):
        root.title("Connect Four")
        self.board = board
        self.cell_size = cell_size
        self.rows = 6
        self.cols = 7
        self.maze_height = self.rows * self.cell_size
        self.maze_width = self.cols * self.cell_size
        self.turnCount =1
        self.p1 =Human(playernum=1)
        self.p2 =Human(playernum=2)
     
        

        # text boxes or spinners for the parameters like ply depth
        rlabel = Label(root, text ="Ply Depth:")
        rlabel.grid(row=0,column=0)
        
        self.entry_box = Entry(root, width =5)
        self.entry_box.grid(row=0, column=1)
        

        
        #player 1 Labeling
        rlabel = Label(root, text ="Player1:")
        rlabel.grid(row=0,column=2)

        self.player1_type = StringVar(root)
        options = ["Human", "Random", "MiniMax"]
        self.player1_type.set(options[0])
        self.rowbox = OptionMenu(root, self.player1_type, *options)
        self.rowbox.grid(row=0, column=3)

        #player 2 Labeling
        rlabel = Label(root, text ="Player2:")
        rlabel.grid(row=0,column=4)

        self.player2_type = StringVar(root)
        options = ["Human", "Random", "MiniMax"]
        self.player2_type.set(options[2])
        self.rowbox = OptionMenu(root, self.player2_type, *options)
        self.rowbox.grid(row=0, column=5)
        
    

        #start button labeling
        self.startbtn = Button(root, text="Start", command = self.game_start)
        self.startbtn.grid(row=0, column=6)

        play_col = []
        for i in range(self.cols):
            #play_col.appendButton(root, text ="Col %d"%i, command =lambda col = i)
            #play_col[i].grid(row=2, column=i)
            b = Button(root, text ="Col %d"%i, width=12)
            b.grid(row = 3, column = i)
            b.config(command = lambda key=i: self.btn_click(key))
                            
        self.canvas = Canvas(root, width = self.maze_width + 20, height = self.maze_height + 20, bg="grey")
        self.canvas.grid(row = 1, column = 0, columnspan = self.cols)
        self.canvas.create_line(0,0,10,10,fill='red', width=3);


        self.draw()

    def game_start(self):
        if self.player1_type.get() !="Human" and self.player2_type.get() !="Human" : #error message
            print "THERE MUST BE A HUMAN!"
            tkMessageBox.showinfo(title="ATTENTION", message= "THERE MUST BE A HUMAN!")
            return

        entry = self.entry_box.get()
        if entry.isdigit():
            depth=int(entry)
            if depth  <= 0 or depth > 4:
                print "PLY DEPTH MUSY BE 1-4!"
                tkMessageBox.showinfo(title="ATTENTION", message= "PLY DEPTH MUSY BE 1-4!")
                return
        else:
            print "PLY DEPTH MUSY BE 1-4!"
            tkMessageBox.showinfo(title="ATTENTION", message= "PLY DEPTH MUSY BE 1-4!")
            return
        
        #Human case
        if self.player1_type.get() =="Human" :
           self.p1 = Human(playernum=1)
           #MiniMax case
        elif self.player1_type.get() =="MiniMax" :
            self.p1 = MinimaxPlayer(playernum=1, ply_depth=depth, utility=SimpleUtility(1, 5))
        #random case
        elif self.player1_type.get() =="Random":
            self.p1 = RandomPlayer(playernum =1)

        if self.player1_type.get =="MiniMax" or self.player2_type.get() =="Random":
            print "Machine Player Num: 1" 
            self.p1.play_turn(self.board)
            self.board.print_board()
            self.draw_board()
            self.turnCount = self.turnCount +1

            
            
        #do same thing for p2
            #Human case
        if self.player2_type.get() =="Human":
            self.p2 = Human(playernum =2)
            #MiniMax case
        elif self.player2_type.get() =="MiniMax":
            self.p2 = MinimaxPlayer(playernum=2, ply_depth=depth, utility=SimpleUtility(1, 5))
        #random case
        elif self.player2_type.get() =="Random":
            self.p2 = RandomPlayer(playernum =2)

            #case for letting the computer play first

        #if self.player1_type !="Human":
         #   p2.play_turn(self.board)
        #else p2.play_turn(self.board)
            
##
##        #case if eother player 1 or 2 pick a machine opponent
##        if self.player1_type == "MiniMax":
##            p1 =
##        elif self.player1_type == "Random":
##            p1 = 
##
##        elif self.player2_type == "MiniMax":
##            p2 = 
##        elif self.player2_type == "Random":
##            p2 =
##        

    def btn_click(self, col):
        playerNum = self.turnCount %2
        if playerNum == 0:
            playerNum =2

        print "ColumnPressed: " +str(col) +" Player Num: " +str(playerNum)
        self.board.play_turn(playerNum,col)
        self.board.print_board()
        self.draw_board()

        
        w = self.board.is_game_over()
        if w != None:
            print "Congradulations Player %i, you won!" % w 
            print self.board.w_move
            tkMessageBox.showinfo(title="Congrats", message= "Player %i, you won!" % w)
            return

        self.turnCount = self.turnCount +1
        nextPlayerNum=self.turnCount%2
        if nextPlayerNum == 0:
            nextPlayerNum =2
        print "Next Player Num: " +str(nextPlayerNum)
        
        #if player 1 or player 2 is not a Human player


        if self.player1_type.get()  != "Human" and nextPlayerNum==1:
            print "Machine Player Num: " +str(nextPlayerNum)
            self.p1.play_turn(self.board)
            self.board.print_board()
            self.draw_board()
        elif self.player2_type.get() != "Human" and nextPlayerNum==2: 
            print "Machine Player Num: " +str(nextPlayerNum)
            self.p2.play_turn(self.board)
            self.board.print_board()
            self.draw_board()
            
        w = self.board.is_game_over()
        if w != None:
            print "Congradulations Player %i, you won!" % w
            print self.board.w_move
            tkMessageBox.showinfo(title="Congrats", message= "Player %i, you won!" % w)
            return

        self.turnCount = self.turnCount +1

        
            

#def generate(self):
# self.maze = random_maze(rows, cols)
# self.draw(self.maze)

    def draw_circle(self, row, col, player):
        pos_row = 10 + row * self.cell_size
        pos_col = 10 + col * self.cell_size
        if player == 1:
            self.canvas.create_oval(pos_col,pos_row, pos_col + self.cell_size, pos_row + self.cell_size, fill = "red")
        else:
            self.canvas.create_oval(pos_col,pos_row, pos_col + self.cell_size, pos_row + self.cell_size, fill = "blue")
    def draw_win_line(self, row, col, player):
        self.canvas.create_line(10,10,200,50);

    def draw(self):
        self.canvas.delete(ALL)
        # Upper-Left corner of the maze is at (10,10)
        startx = 10
        starty = 10

        # Draw the border of the maze
        self.canvas.create_rectangle(startx, starty, \
        startx + self.cols * self.cell_size, \
        starty + self.rows * self.cell_size)
        self.draw_board()

    def draw_board(self):
        for row in range(5,-1,-1):
            for col in range(7):
                p = self.board.get_position(row, col)
                if p == 1 or p == 2: #printing out if there are circles
                    #based on if player 1 or 2 is filling the position
                    pos = 5-row #reversing the position of the player data
                    self.draw_circle(pos, col, p) #prints circles
               
    def play_game(self,board, player1, player2):
        """
                Alternates calling play_turn for players 1 and 2.  In between moves, checks for a winning
        board position.  If a winning position is found, prints a message saying who is the winner
        and returns.
        """
        player1.play_turn(board)
        draw_board(board)
        w = board.is_game_over()
        if w != None:
            print "Congradulations Player %i, you won!" % w
            tkMessageBox.showinfo(title="Congrats", message= "Player %i, you won!" % w)
            return

        player2.play_turn(board)
        draw_board(board)
        w = board.is_game_over()
        if w != None:
            print "Congradulations Player %i, you won!" % w
            tkMessageBox.showinfo(title="Congrats", message= "Player %i, you won!" % w)
            return

#board = ConnectFour()
#board.play_turn(1,2)
#board.play_turn(2,2)
#board.print_board()
#p1 = Human(playernum=1)
#p2 = MinimaxPlayer(playernum=2, ply_depth=4, utility=SimpleUtility(1, 5))
#p1 = MinimaxPlayer(playernum=1, ply_depth=3, utility=SimpleUtility(1, 5))
#p2 = MinimaxPlayer(playernum=2, ply_depth=2, utility=WithColumnUtility(5, 10, [1, 2, 3, 4, 3, 2, 1]))

#board.print_board()
board = ConnectFour()
root = Tk()
mgui = MazeGui(root,board)
root.mainloop()
#root.after(2000, mgui.play_game(board, p1, p2)


