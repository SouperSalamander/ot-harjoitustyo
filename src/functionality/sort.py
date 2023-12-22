"""File for sorting algorithm."""

class SortingAlgorithm():
    """Class to sort lists in ascending order.
    
    Attributes:
        __pf_list: List of prime factors input by user.
    """

    def __init__(self, pf_list):
        """Constructor, makes new sorting algorithm object.
        
        Args:
            pf_list: List of prime factors input by user.
        """

        self.__pf_list = pf_list

    def bubble_sort(self):
        """Function sorts a list of numbers.
        
        Returns:
            List, sorted smallest to largest.
        """

        input_len = len(self.__pf_list)
        swapped = False
        for i in range(input_len-1):
            for j in range(0,input_len-i-1):
                if int(self.__pf_list[j]) > int(self.__pf_list[j+1]):
                    self.__pf_list[j],self.__pf_list[j+1] = self.__pf_list[j+1],self.__pf_list[j]
                    swapped = True
            if not swapped:
                pass
        return self.__pf_list
