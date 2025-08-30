def insetion_sorting(list_of_number : list):
    """Sorts a list using Insertion Sort algorithm

    :return: The sorted list
    :rtype: list
    """
    for i in range(1, len(list_of_number)):
        key = list_of_number[i]
        j = i - 1
        while j >= 0 and key < list_of_number[j]:
            list_of_number[j + 1] = list_of_number [j]
            j -= 1
        list_of_number[j + 1] = key
        
    return list_of_number 
  
  
  
if __name__=='__main__':    
    print(insetion_sorting([5,3,2,6]))
    print(insetion_sorting([1,5,12,2,6]))