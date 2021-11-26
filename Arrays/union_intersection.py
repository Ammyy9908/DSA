def findUnionIntersection(arr1,arr2):
    # Union
    union = set(arr1) | set(arr2)
    print("Union: ",union)
    # Intersection
    intersection = set(arr1) & set(arr2)
    print("Intersection: ",intersection)



findUnionIntersection([1,2,3,4,5,6,7,8,9,10],[3,2,3,4,5,6,7,8,11,10])