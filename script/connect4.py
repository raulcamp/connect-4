import random
from copy import deepcopy

def printer(board):
    for row in board:
        print(("+" + " - ") * 7 + "+")
        s = "| "
        for c in row:
            s += str(c) + " | "
        print(s)
    print(("+" + " - ") * 7 + "+")
    s = ""
    for i in range(7):
        s += "  " + str(i+1) + " "
    print(s)
    print()

class Connect4:
    def __init__(self):
        """Initializes the game.
        
        Creates an empty 7x6 board and randomly chooses which player goes first.
        """
        self.board = [['O' for _ in range(7)] for _ in range(6)]
        self.player = random.randint(1,2)
        
    def get_player(self):
        """Returns which player is next"""
        return self.player
    
    def in_board(self, r, c):
        """Determines whether (r,c) is within the board"""
        return False if (r < 0 or r > 5) or (c < 0 or c > 6) else True
    
    def get_pos(self, r, c):
        """Returns the position of (r,c) in the board"""
        return self.board[r][c] if self.in_board(r,c) else None
    
    def set_pos(self, r, c, player):
        """Places disc at (r,c) if possible"""
        if self.in_board(r,c):
            self.board[r][c] = player
    
    def get_board(self):
        """Returns a copy of the current board"""
        return deepcopy(self.board)
    
    def get_columns(self):
        """Returns a copy of the columns of the current board"""
        return list(zip(*self.get_board()))
    
    def is_full(self):
        """Checks if the current board is full"""
        b = self.get_board()
        for c in range(7):
            for r in range(6):
                if b[r][c] == 'O':
                    return False
        return True
    
    def is_over(self):
        """Checks if the game is over

        Returns:
            int: 1 or 2 depending on who won, 0 if game is not over, or -1 if tie
        """
        if self.is_full():
            return -1
        
        b = self.get_board()
        for p in (1,2):
            for c in range(7):
                for r in range(6):         
                    if (all(b[r][c+i] == p if self.in_board(r,c+i) else False for i in range(4)) or
                        all(b[r+i][c] == p if self.in_board(r+i,c) else False for i in range(4)) or
                        all(b[r+i][c-i] == p if self.in_board(r+i,c-i) else False for i in range(4)) or
                        all(b[r+i][c+i] == p if self.in_board(r+i, c+i) else False for i in range(4))):
                        return p
        return 0
        
    def place_disc(self, player, column):
        """Places player's disc in specified column if possible"""
        c = self.get_columns()[column-1][::-1]
        for i in range(len(c)):
            if c[i] == 'O':
                self.set_pos(5-i, column-1, player)
                return (5-i, column-1)
        
    def play(self):
        """Play a game of Connect 4 in console."""
        while not self.is_over():
            printer(self.get_board())
            player = self.get_player()
            choice = input("Player " + str(player) + ", which column do you want to place the disc in? ")
            print()
            if choice == "quit":
                print("Player " + str(player) + " quit the game.\n")
                return
            elif int(choice) < 1 or int(choice) > 7 or not choice.isdigit():
                print("That is not a column. Try again.\n")
                continue
            result = self.place_disc(player, int(choice))
            if not result:
                print("That column is full, please pick a different column.\n")
                continue
            self.player = 2 if player == 1 else 1
            
        printer(self.get_board())
        if self.is_over() == -1:
            print("There was a tie...\n")
        else:
            print("Congratulations Player " + str(self.is_over()) + ", you won! Thanks for playing!\n")
        rematch = input("Rematch? (y/n) ")
        if rematch == 'y':
            self.board = [['O' for _ in range(7)] for _ in range(6)]
            self.player = random.randint(1,2)
            self.play()
           
if __name__ == '__main__':
    c4 = Connect4()
    c4.play()