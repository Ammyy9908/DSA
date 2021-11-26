from Stack import Stack

def findNextGreater(arr):
    s = Stack()
    s.push(arr[0])
    for i in range(1, len(arr)):
        if arr[i]>s.items[-1]:
            s.pop()
            s.push(arr[i])
        if arr[i]<s.items[-1]:
            s.push(arr[i])
    return s.items[0]



res = findNextGreater([11, 13, 21, 3])
print(res)