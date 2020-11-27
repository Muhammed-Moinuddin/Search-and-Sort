print("Program by Muhammad Moinuddin")

import math

def array(length):
    array = []

    for a in range(length):
        array.append(int(input('Please enter the value: ')))
    return array

print("linear search")
def linear_search(array):
    x = float(input("Enter required number: "))
    index = 0
    for element in array:
        if element == x:
            return f'index of required number in list is {index}.'
        elif index < len(array)-1:
            index += 1
        elif index == len(array)-1:
            return "Required number not present in list"        
print(linear_search(array(7)))  
  
print("bubble sort")
def bubble_sort(array):
    for b in range(len(array)):
        for a in range(len(array)-1):
            if array[a] > array[a+1]:
                array[a], array[a+1] = array[a+1], array[a]
    return f'Array with bubble sort is {array}'              
print(bubble_sort(array(7)))    

print("selection sort")
def selection_sort(array):
    for a in range(len(array)):
        current = array[a]
        current_index = a
        for b in range(a, len(array)):
            if current > array[b]:
                current = array[b]
                current_index = b
        array[current_index], array[a] = array[a], current
    return array 

              
print(selection_sort(array(7)))

print("binary search")
def binary_search(array):
    selection_sort(array)
    x = float(input("Please Enter required number: "))
    low = 0
    high = len(array) - 1
    while True:
        mid = math.ceil((low + high)/2)
        if mid == len(array):
            return "Required number not present"
        elif array[mid] == x:
            return f'index of required number in list is {mid}.'
        elif low == high:
            return "Required number not present"
        elif array[mid] < x:
            low = mid+1
        elif array[mid] > x:
            high = mid-1
                        
print(binary_search(array(7)))    