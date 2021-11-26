def minimum_difference_sum(arr):
    arr.sort()
    result = 0
    result += abs(arr[0] - arr[1])
    result += abs(arr[len(arr) - 1] - arr[len(arr) - 2]);
         
    
    for i in range(1, len(arr) - 1):
        result += min(abs(arr[i] - arr[i - 1]),
                  abs(arr[i] - arr[i + 1]))
             
    
    return result


print(minimum_difference_sum([5,1,3,7,3]))