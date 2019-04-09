#! /usr/bin/python3.7
"""

This is implementation of Quick Sort in Python 3.7
Input: comma separated integer list
Output: comma separated sorted integer list
Time Complexity: O(nlogn), n being number of integers in the list
Author: Anurag Daware 
Copyright: Anurag Daware 2019

"""
import sys
import traceback
# this method find pivotIndex where it needs to place pivotValue
# after placing pivtoValue at rightful pivotIndex, left of pivotValue are the values lesser than it (not necessarily in sorted order)
# and right of pivotValue are the values greater than it (not necessarily in sorted order)
def partition(arr, start, end):
    pivotIndex = start
    pivotValue = arr[end]
    #print('Partition before pivotIndex: ', pivotIndex)
    i = start
    while i < end:
        if arr[i] < pivotValue:
            temp = arr[i]
            arr[i] = arr[pivotIndex]
            arr[pivotIndex] = temp
            pivotIndex += 1
            #print('pivotTemp: ', pivotIndex)
        i += 1
    #endWhile
    temp = arr[pivotIndex]
    arr[pivotIndex] = arr[end]
    arr[end] = temp
    print("after pivotIndex: ", pivotIndex)
    return pivotIndex

def quick_sort(arr, start, end):
    print(arr, " start: ", start, " end: ", end)
    if(start >= end):
        return arr
    pivotIndex = partition(arr, start, end)
    quick_sort(arr, start, pivotIndex -1)
    quick_sort(arr, pivotIndex + 1, end)
    return arr

if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter input array to be sorted: ").split()))
        print(arr)
        arr_len = len(arr)
        print("array length: ", arr_len)
        arr = quick_sort(arr, 0, len(arr)-1)
        print("Sorted array: ", arr)
        #sys.exit()
    except Exception as e:
        print('ok ok: ', str(e))
        print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.__traceback__)))
