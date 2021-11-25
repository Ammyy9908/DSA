class Solution:
    def kthLargest(self,arr, k):
        arr.sort()
        return arr[k-1]


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    k = 5
    print(Solution().kthLargest(arr, k))