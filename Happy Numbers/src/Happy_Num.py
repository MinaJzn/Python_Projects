def Happy_Number(Input_number:int):
    """Checks whether a given number is happy or not.

    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum
    of the squares of its digits in base-ten, and repeat the process
    until the number either equals 1 (where it will stay), or it loops
    endlessly in a cycle that does not include 1. Those numbers for
    which this process ends in 1 are happy numbers.

    :returns: (Yeah! "Input_number" is Happy Number!) if the number is a happy number,
    (Oops..." Input_number " is not Happy Number!) otherwise
    

    :Example:

    >>> is_happy(19)
    True

    >>> is_happy(2)
    False
    """
    seen=set()
    number=Input_number
    while True:
        digits=list(str(number))
        square_list=[]
        for i in digits:
            num=int(i)**2
            square_list.append(num)
        number=sum(square_list)
        if number==1:
            print(f'Yeah!\n"{Input_number}" is Happy Number!')
            break
        elif number in seen:
            print(f'Oops...\n"{Input_number}" is not Happy Number!')
            break
        else:
            seen.add(number)


if __name__=='__main__':
    Happy_Number(7)
    Happy_Number(44)
    Happy_Number(45)
