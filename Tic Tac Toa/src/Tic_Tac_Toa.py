import random

class Tic_Tac_Toa:
    def __init__(self):
        self.board = [['?' for _ in range(3)] for _ in range(3)]
        self.choice = ''
        self.computer_choice = ''
    
    def print_board(self):
        for row in self.board:
            print('     '.join(row))
            print()

    def player_choice(self,row_player,column_player,choice):
        if self.board[row_player][column_player]!='?':
            print("This cell is already taken.")
            return False
        self.board[row_player][column_player] = choice
        return True
        
    def computer_option(self):
        if self.choice=='O':
            self.computer_choice='X'
        else:
            self.computer_choice='O'
        print(f'computer choice is {self.computer_choice}')

    def computer_row_column(self):
        while True:
            row_computer=random.randint(0,2)
            column_computer=random.randint(0,2)
            if self.board[row_computer][column_computer]=='?':
                self.board[row_computer][column_computer] = self.computer_choice
                print(f"Computer played at ({row_computer}, {column_computer})")
                break
        
    def win(self,symbol):
        for i in range(3):
            if self.board[i][0]== self.board[i][1]==self.board[i][2]==symbol:
                return True
        for i in range(3):
            if self.board[0][i]==self.board[1][i]==self.board[2][i]==symbol:
                return True
        if  self.board[0][0]==self.board[1][1]==self.board[2][2]==symbol:
                return True
        if self.board[0][2]==self.board[1][1]==self.board[2][0]==symbol:
                return True
        return False

    def play_game(self):
        self.print_board()
        self.choice = input("Choose your symbol (X or O): ").upper()
        
        while self.choice not in ['X', 'O']:
            self.choice = input("Invalid choice. Choose X or O: ").upper()
        
        self.computer_option()
        while True:
            try:
                row_player = int(input("Write your Row (0-2): "))
                column_player = int(input("Write your Column (0-2): "))
                if row_player not in range(3) or column_player not in range(3):
                    print("Row and column must be between 0 and 2.")
                    continue
                if not self.player_choice(row_player, column_player, self.choice):
                    continue
            except ValueError:
                print("Please enter valid integers for row and column.")
                continue     
            self.print_board() 
               
            self.computer_row_column()
            self.print_board()
            
            if self.win(self.choice):
                print("You win!")
                break
            
            
            if self.win(self.computer_choice):
                print("Computer wins!")
                break

if __name__ == "__main__":
    b=Tic_Tac_Toa()
    b.play_game()