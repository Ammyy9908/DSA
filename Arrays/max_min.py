def findMinMax(arr,n):
    min = 0
    max = 0

    # if there is only one element in the array
    if(len(arr)==1):
        min = arr[0]
        max = arr[0]
    #if there are two elements

    if(arr[0]<arr[1]):
        min = arr[0]
        max = arr[1]
    else:
        min = arr[1]
        max = arr[0]
        
    
    # if there are more than two elements assume that the first two elements are the min and max
    for i in range(2,n):
        if(arr[i]<min):
            min = arr[i]
        if(arr[i]>max):
            max = arr[i]
    return (max,min)



max_min = findMinMax([1,2,3,4,5,6,7,15,8,9,10],11)

print(max_min)