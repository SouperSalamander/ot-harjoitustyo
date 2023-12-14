"""number theory calculator"""
import math

class GcfClass:
    """class to carry out gcf"""
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def gcf(self):
        """function to carry out gcf"""
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
    """class to carry out lcm"""
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def lcm(self):
        """function to carry out lcm"""
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
    """class for finding prime factors"""
    def __init__(self, first_num):
        self.__first_num = first_num

    def pf(self):
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
