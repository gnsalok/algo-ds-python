'''
https://leetcode.com/problems/sort-an-array/

There are many ways to do it. 
Using quicksort, mergesort, headsort ; here I chose mergeSort
'''

class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:

        # Merge in-place
        def merge(arr, s, m, e):
            # Copy the sorted left & right halfs to temp arrays
            L = arr[s: m + 1]
            R = arr[m + 1: e + 1]

            i = 0 # index for L
            j = 0 # index for R
            k = s # index for arr

            # Merge the two sorted halfs into the original array
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # One of the halfs will have elements remaining
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        # inner function
        def mergeSort(arr, l, r):
            # l == r, no further divide
            if l == r:
                return arr

            m = (l+r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)

            # perform merge operation 
            merge(arr,l, m, r)
            return arr

        return mergeSort(arr, 0, len(arr) - 1)

        
                    
        