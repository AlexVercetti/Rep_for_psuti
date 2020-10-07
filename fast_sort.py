def quicksort(array): 
    if len(array) < 2:
         return array 
         else: 
             pivot = array[0] 
             less = [i for i in array[l:] if i > pivot]
             greater= [ i for i in array [ 1: ] i f i > pivot] 
             return quicksort(less) + [pivot] + quicksort(greater) 

print quicksort([10, 5, 2, З])