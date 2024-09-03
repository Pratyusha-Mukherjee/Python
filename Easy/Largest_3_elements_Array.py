def largeelement(arr):
    size = len(arr)
    first = second = third = 0
    if size < 3:
            print("Invalid Input")
    for i in range(size):  
        if arr[i]>first: 
            third = second
            second = first
            first = arr[i]
        elif arr[i]>second and arr[i]!=first: 
            third = second
            second = arr[i]
        elif arr[i]>third and arr[i]!=first and arr[i]!=second: 
            third = arr[i] # type: ignore

    print ("Three largest numbers are:-",first,second,third)



array = [10,2,34,67,90,21,6,32]
largeelement(array)
    