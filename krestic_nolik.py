from queue import Empty
from tkinter import *
from turtle import heading, width
# tODO change import method, to from tkinter import module

# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = 200
RATIO = CANVAS_SIZE//FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

# Players setup
X = 'player 1'
O = 'player 2'
FIRST_PLAYER = X


class Board(Tk):    
    
    def chenge_player(self):
        if self.current_player == X:
            self.current_player = O
        else: self.current_player = X
        

    def check_draw(self, board):
        for row in board:
             if EMPTY in row:
                 return False
        return True
    
    def check_win(self, board, player):
        for y in range(3):
            if board[y] == [player, player, player]:
                return True
        for x in range(3):
            if board[0][x] == board[1][x] == board[2][x] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
                
    def update_board(self, x, y):
        c_player = self.current_player
        self.board[x][y] = c_player
        print(self.board[x][y])
        if self.check_win(self.board, c_player):
            self.winner(c_player)
        if self.check_draw(self.board):
            self.winner(player = None)
        
    
    def make_move(self, x, y):
        position = {0 : 0, 1 : 200, 2 : 400}
        current_player = self.current_player
        
        if self.board[x][y] == EMPTY:
            self.update_board(x, y)
            self.chenge_player()
            
        if current_player == X :
             self.render_cross(position[x], position[y])
        elif current_player == O :
            self.render_circle(position[x], position[y])
        print(self.board)
        
        
    def build_grid(self, grid_color):
            x = CANVAS_SIZE // RATIO
            y1 = 0
            y2 = CANVAS_SIZE
            for _ in range(2):
                self.canvas.create_line(x, y1, x, y2, fill=grid_color)
                self.canvas.create_line(y1, x, y2, x, fill=grid_color)
                x += CANVAS_SIZE//RATIO

    def render_cross(self, posX, posY, cross_color = 'red'):
        x = posX
        y = posY
        y1 = FIGURE_SIZE
        x1 = x + y1
        y2 = y + y1
        self.canvas.create_line(x, y, x1, y2, fill = cross_color, width = 5)
        self.canvas.create_line(x1, y, x, y2, fill = cross_color, width = 5)
        
    def render_circle(self, posX, posY):
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline = 'blue', width = 5)
        
    def winner(self, player = None):
        self.game_status = False
        center = CANVAS_SIZE // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        self.canvas.create_text(center, center, text = text, fill = 'white', font = 'Arial 50')
        self.canvas.unbind('<Button-1>')

    def click_event(self, event):
        x_coord = event.x // FIGURE_SIZE
        y_coord = event.y // FIGURE_SIZE
        self.make_move(x_coord, y_coord)
        
        if self.game_status:
            self.ai_best_move()
    
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE, bg = BG_COLOR)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
        self.game_status = True
        
    def ai_best_move(self):
        best_score = float("-inf")
        board_len = range(len(self.board))
        board = self.board[:]    
        for i in board_len:
            for j in board_len:
                if board[i][j]==EMPTY:
                    board[i][j] = O
                    score = self.minimax(board, False)
                    board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = i, j
        self.make_move(move[0], move[1])   
        
        
    def minimax(self, board, isMax):
        """Monimax https://en.wikipedia.org/wiki/Minimax"""
        board_len = range(len(self.board))
        
        if self.check_win(board, O):
            return 1
        elif self.check_win(board, X):
            return -1
        elif self.check_draw(board):
            return 0
        
        if isMax:
            best_score = float('-inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = O
                        score = self.minimax(board, False)
                        board[i][j] = EMPTY
                        best_score = max(score, best_score)
        else:
            best_score = float('inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = X
                        score = self.minimax(board, True)
                        board[i][j] = EMPTY
                        best_score = min(score, best_score)
        return best_score
                        
                    
        
game_v1 = Board(start_player = FIRST_PLAYER)
game_v1.build_grid('blue')

game_v1.mainloop()

