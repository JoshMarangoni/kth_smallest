class Sorting:
    def mergesort(arr): 
        mergesort(arr, 0, len(arr)-1)

    def mergesort(arr, lo, hi):
        if hi - lo == 0: 
            return
        mid = hi + lo / 2
        mergesort(arr, 0, mid)
        mergesort(arr, mid+1, hi)
        C = merge(arr[lo:mid}, arr[mid+1:hi])
        return C

    def merge(a, b):
        c = [len(a) + len(b)]
        i=0
        j=0
        k=0
        while i < len(a) and j < len(b): 
            if a[i] < b[j]: 
                c[k] = a[i]
                i = i+1
                k = k+1
            else: 
                c[k] = b[j]
                j = j+1 
                k = k+1
        while i < len(a): 
            c[k] = a[i]
            k = k+1
            i = i+1
        while j < len(b): 
            c[k] = b[j]
            k = k+1
            j = j+1
        return c

arr = [7, 3, 4, 1]
new = mergesort(arr)
print('arr = ', arr)
print("sorted = ", new)