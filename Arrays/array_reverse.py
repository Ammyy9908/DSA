def reverse_array(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


res = reverse_array([1, 2, 3, 4, 5])
print(res)