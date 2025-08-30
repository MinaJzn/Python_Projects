import random
import string
from nltk.corpus import words


def pin_codes(length: int = 8)->str:
    """this function use for generate a password that includes numbers from 0 to 9 and is 8 characters long.
    
    :param length: length of password, defaults to 8
    """
    sim_pas=random.choices(string.digits,k=length)
    return ''.join(sim_pas)

def memorable_password(num_words: int = 10)->str:
    """this is a memorable password.

    :param num_words: number of words in password, defaults to 10
    """
    # nltk.download('words')
    words_list=list(set(words.words()))
    mem_pas=random.sample(words_list,num_words) 
    return '-'.join(mem_pas)

def random_passwords(length: int = 8)->str:
    """this is a random password with letters and digits and symbols.

    :param length: length of password, defaults to 8
    """
    characters=string.ascii_letters + string.punctuation + string.digits
    rand_password=random.choices(characters,k=length)
    return ''.join(rand_password)

def main():
    print('Testing pin code password!')
    print(pin_codes())
    print('Testing memorable password!')
    print(memorable_password())
    print('Testing random password!')
    print(random_passwords())

if __name__=='__main__':
    main()
