from sorting import Sorting

k = 6
arr = [4,1,6,7,8,2,65,143,5]
#arr = [1]
print(arr)
if k > len(arr): 
  print("Error: k larger than array")
  exit() 

sort = 'qsel'
#sort = 'merge'

#-----------------test mergesort implementation------------------------
if sort == 'merge':
  print('\nMerge-sorting...')
  Sorting().mergesort(arr)
  print(arr)
  print('The kth smallest element is: ', arr[k-1])


#------------------test quickselect-----------------------------------

else:
  print('\nQuick-selecting...')
  pivot = Sorting().quickSelect(arr, k)
  print(arr)
  print('The kth smallest element is: ', arr[pivot])
