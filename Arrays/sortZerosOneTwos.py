def sort_zero_one_two(arr):
    l = 0
    m = 0
    h = len(arr) - 1
    while m<=h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m+=1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    return arr


res = sort_zero_one_two([0,1,1,0,2,1,2])

print(res)