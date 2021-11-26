def closestNumbers(arr):
    if len(arr) <= 1: return
 
    # Sort array elements
    
    arr.sort()
    result = list()
     
    
    minDiff = arr[1] - arr[0]
    for i in range(2 , len(arr)):
        minDiff = min(minDiff, arr[i] - arr[i-1])
 
    # Traverse array again and print all
    # pairs with difference as minDiff.
    for i in range(1 , len(arr)):
        if (arr[i] - arr[i-1]) == minDiff:
            print(str(arr[i-1]) + " " + str(arr[i]))
                



closestNumbers([4,2,1,3])