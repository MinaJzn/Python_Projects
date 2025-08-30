def bubble_sorting(list_of_number : list):
    """ Sorts a list using Bubble Sort algorithm
    
    :param l: List of your number
    :return: The sorted list
    """
    for _ in range(len(list_of_number) - 1):
        for i in range(0,len(list_of_number)-1): 
            if list_of_number[i]>list_of_number[i+1]:
                list_of_number[i],list_of_number[i+1]=list_of_number[i+1],list_of_number[i]
    return(list_of_number)   


if __name__=='__main__':
   print(bubble_sorting([1,4,2,5,3,1]))

