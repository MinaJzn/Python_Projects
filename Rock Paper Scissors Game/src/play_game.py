"""Author:Mina Jazini
Subject:Rock_Paper_Scissors Game
"""
from random import choice as rc


class RockPaperScissors:
    def __init__(self,ch:str,rc:str):
        """
        :param ch: User choice
        :param rc: Computer choice
        """
        self.ch=ch
        self.rc=rc
        
    def game_role(self):
        """This is the role of game and if return True means: it is the benefit of User.
        and if return False means: it is the benefit of Computer.
        """
        if (self.ch=='rock' and self.rc=='scissors') or (self.ch=='paper' and self.rc=='rock') or (self.ch=='scissors' and self.rc=='paper'):
            return True
        elif self.ch==self.rc:
            return 'Equal'
        else:
            return False
   
        
class Conclusion:
    """Who is winner?!"""
    def __init__(self,user:str,comp:str):
        self.user=user
        self.comp=comp
        
    def winner(self):
        if self.user>self.comp:
            return 'User is winner!'
        elif self.comp>self.user:
            return 'Computer is winner!'
        else:
            return 'The game is currently a draw...'


def main():
    user_score=0
    computer_score=0
    count_of_round=1
    while True:
        computer_choice=rc(['rock','paper','scissors'])
        print(computer_choice)
        
        while True:
            your_choice=input('your choice is:')
            if your_choice.lower() not in ['rock','paper','scissors']:
                print('please write your choice among of ("rock","paper","scissors") :')
                continue
            break
        
        c=RockPaperScissors(your_choice,computer_choice) 
        if c.game_role() is True:
            user_score+=1
        elif c.game_role() is False:
            computer_score+=1
        
        win=Conclusion(user_score,computer_score)
        print(f'user_score:{user_score} and computer_score:{computer_score} in {count_of_round} rounds!\n{win.winner()}')
        answer=input('Do you want to continue?(y/n)')
        if answer.lower() not in ['y','yes']:
            print('I hope to enjoy this game...\nBye\nSee you soon') 
            break
        count_of_round+=1
        continue
    

if __name__=='__main__':
    main()