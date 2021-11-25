def sort_positive_negative(numbers):
    j = 0
    for i in range(len(numbers)):
        if (numbers[i] < 0):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
            j += 1
    return numbers


res = sort_positive_negative([1,2,-1,-5,5,-15])
print(res)