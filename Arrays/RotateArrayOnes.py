def rotateArrayOne(arr, d):
    for i in range(d):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
    return arr


res = rotateArrayOne([1, 2, 3, 4, 5], 5)
print(res)



