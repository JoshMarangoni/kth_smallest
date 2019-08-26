class Sorting:
  def mergesort(self, arr):
    if len(arr) <= 1: 
      return arr

    mid = len(arr) // 2
    
    left = self.mergesort(arr[:mid])
    right = self.mergesort(arr[mid:])
    
    return self.merge(left, right)

  def merge(self, a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b): 
      if a[i] < b[j]: 
        c.append(a[i])
        i += 1
      else: 
        c.append(b[j])    
        j += 1 
    while i < len(a): 
      c.append(a[i])  
      i += 1
    while j < len(b): 
      c.append(b[j])  
      j += 1
    return c

  # find the kth smallest using quickselect
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



arr = [1,7,3,2,6,8,4]

