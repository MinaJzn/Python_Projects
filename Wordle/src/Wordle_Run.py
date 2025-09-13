from choose_and_geuss import computer_word,guess_word

def wordle()-> str:
    """Main game loop for the Wordle game.
       The user has 6 attempts to guess the randomly selected word.
       Gives feedback after each guess.
    """
    score=6
    computer_wordle=computer_word()
    guessed_correctly = False
    
    while score>0:
        guess_wordle=guess_word()
        
        if computer_wordle['random_word']==guess_wordle['your_word']:
            guessed_correctly = True
            print(f'🥳 Congratulations!\nYour geuss correced with {score} score.')
            break
        
        else:
            right_characters=[]
            rc_in_wrong_place=[]
            for i in range(5):
                if computer_wordle['random_word_list'][i]==guess_wordle['your_word_list'][i]:
                    right_characters.append(guess_wordle['your_word_list'][i])
                    
                elif guess_wordle['your_word_list'][i] in computer_wordle['random_word_list']:
                    rc_in_wrong_place.append(guess_wordle['your_word_list'][i])
                    
            right_characters and print(f'👌 {" , ".join(right_characters)} is correct.')
            rc_in_wrong_place and print(f'👀 {" , ".join(rc_in_wrong_place)} is correct but in wrong place.')
            score-=1
            print(f'Your score is {score}')
            continue

    if not guessed_correctly:
        print('☹️ Sorry...\nYou lost your chance!')
            
if __name__=='__main__':
    wordle()