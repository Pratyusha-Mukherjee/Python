def secondLarge(arr):
    size = len(arr)
    first = second  = 0
    if size < 2:
            print("Invalid Input")
    for i in range(size):  
        if arr[i]>first: 
            second = first
            first = arr[i]
        elif arr[i]>second and arr[i]!=first: 
            second = arr[i]
    print("Second large element is :-",second)      

array = [10,2,34,67,90,21,6,32]
secondLarge(array)
        