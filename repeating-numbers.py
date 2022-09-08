import collections
from itertools import count
def reapited_numbers(numbers):
    count = collections.Counter(numbers).items(1)
    print(count)

a = [1,2,3,2,1,5,6,5,5,5]
reapited_numbers(a)