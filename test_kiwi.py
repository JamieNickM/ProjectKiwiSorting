from random import randint, random
from Project_Kiwi_Sorting import BubbleSort, SelectionSort, QuickSort, MergeSort, splitData
from time import time
import pytest
import numpy as np

bestcase = np.sort(np.copy(splitData))
averagecase = np.copy(splitData)
worstcase = np.copy(bestcase)[::-1]

#=================== Bubble Sort Test ====================

def test_space():
    print('')
def test_BubbleWorst():
    start= time()
    assert np.array_equal(BubbleSort(np.copy(worstcase)),bestcase)
    print('')
    print('.'+ str(time()-start))

def test_BubbleBest():
    start= time()
    assert np.array_equal(BubbleSort(np.copy(bestcase)),bestcase)
    print(time()-start)

def test_BubbleAverage():
    start= time()
    assert np.array_equal(BubbleSort(np.copy(averagecase)),bestcase)
    print(time()-start)

#=================== Selection Sort Test ====================

def test_SelectionWorst():
    start= time()
    assert np.array_equal(SelectionSort(np.copy(worstcase)),bestcase)
    print(time()-start)

def test_SelectionBest():
    start= time()
    assert np.array_equal(SelectionSort(np.copy(bestcase)),bestcase)
    print(time()-start)

def test_SelectionAverage():
    start= time()
    assert np.array_equal(SelectionSort(np.copy(averagecase)),bestcase)
    print(time()-start)

#=================== Quick Sort Test ====================

def test_QuickWorst():
    start= time()
    assert np.array_equal(QuickSort(0,len(worstcase)-1,np.copy(worstcase)),bestcase)
    print(time()-start)

def test_QuickBest():
    start= time()
    assert np.array_equal(QuickSort(0,len(bestcase)-1,np.copy(bestcase)),bestcase)
    print(time()-start)

def test_QuickAverage():
    start= time()
    assert np.array_equal(QuickSort(0,len(averagecase)-1,np.copy(averagecase)),bestcase)
    print(time()-start)

#=================== Merge Sort Test ====================

def test_MergeWorst():
    start= time()
    assert np.array_equal(MergeSort(np.copy(worstcase),0,len(worstcase)-1),bestcase)
    print(time()-start)

def test_MergeBest():
    start= time()
    assert np.array_equal(MergeSort(np.copy(bestcase),0,len(bestcase)-1),bestcase)
    print(time()-start)

def test_MergeAverage():
    start= time()
    assert np.array_equal(MergeSort(np.copy(averagecase),0,len(averagecase)-1),bestcase)
    print(time()-start)