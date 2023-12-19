"""File handling all operations."""
import math

class GcfClass:
    """Class to carry out greatest common factor calculations.
    
    Attributes:
        __number1: input from user.
        __number2: input from user.
    """

    def __init__(self, number1, number2):
        """Constructor, makes new gcf object.
        
        Args:
            number1: user input.
            number2: user input.
        """

        self.__number1 = number1
        self.__number2 = number2

    def gcf(self):
        """Function to calculate Greates common Factor.
        
        Returns:
            String containing step by step solution.
        """

        first = int(self.__number1)
        second = int(self.__number2)
        remainder = 1
        gcf_result = ""
        count = 0
        while remainder != 0:
            count += 1
            difference =  first - second
            if difference < 0:
                first,second = second,first
            else:
                pass
            remainder = first % second
            division = int(first/second)
            gcf_result = gcf_result + "Step " + str(count) + ": " + str(first) + " / " + \
            str(second) + " = " + str(division) + " remainder: " + str(remainder) + "\n"
            if remainder != 0:
                first = second
                second = remainder
        gcf_result = gcf_result + "The Greatest Common Factor is " + str(second)
        return gcf_result

class LcmClass():
    """Class to carry out lowest common multiple calculations.
    
    Attributes:
        __number1: user input.
        __number2: user input.
    """

    def __init__(self, number1, number2):
        """Constructor, makes new lcm object.
        
        Args:
            number1: user input.
            number2: user input.
        """

        self.__number1 = number1
        self.__number2 = number2

    def lcm(self):
        """Function to calculate lcm.
        
        Returns:
            String containing step by step solution.
        """

        first = int(self.__number1)
        second = int(self.__number2)
        gcf_list = list(GcfClass(first,second).gcf().split(" "))
        n = len(gcf_list)
        lcm_is = round((first*second)/(int(gcf_list[n-1])))
        line1 = "Step 1: " + str(first) + " * " + str(second) + " = " + str(first*second)
        line2 = "Step 2: Greatest Common Factor = " + gcf_list[n-1]
        line3 = "Step 3: " + str(first*second) + " / " + gcf_list[n-1] + " = " + str(lcm_is)
        line4 = "The Lowest Common Multiple is " + str(lcm_is)
        lcm_result = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        return lcm_result

class PfClass():
    """Class for finding prime factors.
    
    Attributes:
        __first_num: user input.
    """

    def __init__(self, first_num):
        """Constructor, makes new pf object.
        
        Args: 
            first_num: user input.
        """

        self.__first_num = first_num

    def pf(self):
        """Function for pf.
        
        Returns:
            List of prime factors
        """

        pf_list = []
        n = int(self.__first_num)
        while n % 2 == 0:
            pf_list.append(2)
            n = n / 2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                pf_list.append(i)
                n = n / i
        if n > 2:
            pf_list.append(round(n))
        return pf_list
