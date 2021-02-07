from connect4 import Connect4
import random

class Rand:
    def choice(self):
        return random.randint(1,7)

class MinMax:
    def check_three(self, board):
        score = 0
        checked_pos = set()
        b = board.get_board()
        cols = board.get_columns()
        for c in range(7):
            for r in range(6):
                if (r, c) not in checked_pos:
                    if all(b[r][c+i] == 1 if board.in_board(r,c+i) else False for i in range(3)):
                        pass
                    elif all(b[r+i][c] == 1 if board.in_board(r+i,c) else False for i in range(3)):
                        pass
                    elif all(b[r+i][c-i] == 1 if board.in_board(r+i,c-i) else False for i in range(3)):
                        pass
                    elif all(b[r+i][c+i] == 1 if board.in_board(r+i, c+i) else False for i in range(3)):
                        pass
        return
    
    def check_two(self, board):
        return
    
    def check_single(self,board):
        return
    
    def evalPos(self, board):
        if board.is_full():
            return 0
        res = board.is_over()
        if res == 1:
            return float('inf')
        elif res == 2:
            return float('-inf')
        else:
            pass
            
        return
    
    def minmax(self, pos, depth, maximizingPlayer, alpha, beta):
        return
    
    def choice(self):
        return 