import collections
from itertools import count
def repeated_numbers(numbers):
    if(type(numbers) is list):
        for i in range(len(numbers)):
            if(numbers.count(numbers[i])>1):
                print(i)
                break
    else:
        print("Please Enter correct list of numbers")
a = [9,2,3,2,1,5,6,5,5,5]
repeated_numbers(a)