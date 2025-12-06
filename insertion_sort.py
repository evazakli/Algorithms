
"""
insertion sort logic:
    https://en.wikipedia.org/wiki/Insertion_sort
    
    arr = [4,7,3,6,2,9]

    we need to select some keys from the array.

    for first key = 7 look (4<7:True) location is good. new arr = [4,7,3,6,2,9]

    for second key = 3 look (7<3:False) shift left   
        look (4<3:False)  sift left location is good new arr = [3,4,7,6,2,9]
               
    for third key = 6 look (7<6:False) shift left, look (4<6:True). 
        new arr = [3,4,6,7,2,9]

    ... it is going like that

    it is an inefficient algorithm in term of time complexity.
    the worst case is O(n^2). (two nested loop)

    space complexity is O(1).

    maybe it is usable for small arrays

"""


def insertion_sort(arr):

    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


#testing
import random

arr = random.sample(range(-100000,150000),7500)
print(arr)
print(insertion_sort(arr))

