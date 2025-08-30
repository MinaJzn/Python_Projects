def selection_sorting(list_of_number : list):
    """ Sorts a list using Selection Sort algorithm

        :return: The sorted list
    """
    for i in range(len(list_of_number)):
        min_index = i
        for j in range(i + 1, len(list_of_number)):
            if list_of_number[j] < list_of_number[min_index]:
                min_index = j
        list_of_number[i], list_of_number[min_index] = list_of_number[min_index], list_of_number[i]
    return list_of_number


if __name__=='__main__':  
    print(selection_sorting([5,1,45,12,3]))