class Sorting:

  def mergesort(self, arr):

    if len(arr) <= 1:
      return

    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]

    self.mergesort(left)
    self.mergesort(right)
    
    i = j = k = 0
    while i < len(left) and j < len(right): 
      if left[i] < right[j]: 
        arr[k] = left[i]
        i += 1
        k += 1
      else: 
        arr[k] = right[j]    
        j += 1 
        k += 1
    while i < len(left): 
      arr[k] = left[i]  
      i += 1
      k += 1
    while j < len(right): 
      arr[k] = right[j]
      j += 1
      k += 1

  def quickSelect(self, arr, k): 
    return self._quickSelect(arr, len(arr)-1, 0, k)

  def _quickSelect(self, arr, hi, lo, k):
    if lo == hi: 
      return lo 

    pivot = self.partition(arr, hi, lo)   #pivot index
    
    if pivot == k-1: 
      return pivot
    
    if pivot > k-1: 
      return self._quickSelect(arr, pivot-1, lo, k)

    else: 
      return self._quickSelect(arr, hi, pivot+1, k)
    
  def swap(self, arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

  def partition(self, arr, hi, lo):
    pIndex = lo
    pivot = hi
    i = lo

    while i < hi-1:
      if arr[i] < arr[pivot]: 
        self.swap(arr, i, pIndex)
        pIndex+=1
      i+=1
    
    self.swap(arr, pIndex, pivot)
    return pIndex
