import numpy as np
import time
import matplotlib.pyplot as plt


    # Opens the Kiwidata.txt file
with open('kiwidata.txt') as file:
    # Reads the Kiwidata.txt file
    data = file.read()
splitData = data.split(',')
splitData.remove('')

splitData = np.array(splitData).astype(np.float64)
   # Creating an array of the values for the x axis
xValues = [0]*len(splitData)
for i in range(len(splitData)):
    xValues[i] = i


#=================== SR4 Bubble Sort ===================

def BubbleSort (nums):
    # Loop which does swapping (internal)
    for i in range(len(nums)-1,0,-1):
    # Loop which checks the total number of elements (external)
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    return nums


#=================== SR5 Selection Sort ===================

def SelectionSort (nums):
    # Search min value from low to high index - low = 0 high = 5 
    for i in range (len(nums)):
    # variable that holds the min position
        minpos = i
    # make the range of array smaller
        for j in range(i +1 ,len(nums)):
            if nums[j] <nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

    return nums


#=================== SR6 Merge Sort ====================
 

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def MergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr
 
 
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()


#=================== Quick Sort ====================

def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def QuickSort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        QuickSort(l, pi-1, nums)  # Recursively sorting the left values
        QuickSort(pi+1, r, nums)  # Recursively sorting the right values
    return nums
     

#=================== Sorting and Printing ====================

# quickSort = np.copy(splitData)
# quickSort = QuickSort(0,len(quickSort)-1,quickSort)
# print(*quickSort)
    
# sortedBubble = np.copy(splitData)
# sortedBubble = BubbleSort(sortedBubble)
# print(*sortedBubble)

selectionSort = np.copy(splitData)
selectionSort = SelectionSort(selectionSort)
print(*selectionSort)

#=================== SR10 Plotting Graphs ====================

# Sorted Data Displayed on Graph
plt.title('Kiwi Weights')
plt.yticks(np.arange(min(selectionSort),max(selectionSort),0.5))
plt.scatter(xValues, selectionSort)
plt.show()

# Unsorted Data Displayed on Graph
plt.title('Kiwi Weights')
plt.yticks(np.arange(min(splitData),max(splitData),0.5))
plt.scatter(xValues, splitData)
plt.show()